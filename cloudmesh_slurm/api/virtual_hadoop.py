from __future__ import print_function
import cloudmesh
from cloudmesh_common.logger import LOGGER
from cloudmesh_slurm.api.hadoop_instance import VirtualHadoop
from subprocess import call

log = LOGGER(__file__)
mesh = cloudmesh.mesh("mongo")
username = cloudmesh.load().username()

class virtual_hadoop:

    def create(self, name, datanodes, cloud):
        print("create hadoop cluster {0}"
               " with {1} datanodes".format(name, datanodes))
        # check if groupname already exits
        for serverid in mesh.servers(clouds=[cloud],
                                     cm_user_id=username)[cloud].keys():
            server =  mesh.servers(clouds=[cloud],
                                   cm_user_id=username)[cloud][serverid]
            try:
                if server["metadata"]["cm_group"] == name:
                    print("Group Name {0} already exits".format(name))
                    return
            except:
                pass
        #create a virtual cluster
        try:
            nodes = int(datanodes)
        except:
            print("DATANODES should be an integer")
            return
        nodes = nodes + 1
        print("creating a cluster with {0} nodes".format(str(nodes)))
        r = cloudmesh.shell("cluster create --count={0}"
                            "--group={1} "
                            "--ln=ubuntu".format(datanodes, name))
        #print(r)
        print("created");
        #deploy hadoop on cluster
        DeployHadoop(name,cloud)
        
        
        return
    def DeployHadoop(self, name, cloud):
        print("Attempting to deploy hadoop on cluster"
              " group {0}".format(name))
        
        # Check if groupname is valid
        nodecount = 0
        for serverid in mesh.servers(clouds=[cloud],
                                     cm_user_id=username)[cloud].keys():
            server =  mesh.servers(clouds=[cloud],
                                   cm_user_id=username)[cloud][serverid]
            try:
                if server["metadata"]["cm_group"] == name:
                    # print("Group Name {0} already exits".format(name))
                    nodecount += 1
            except:
                pass
        if nodecount < 2:
            print("Warning:Group name does not exist or group has"
                  " less than 2 VMs")
            return
        print("deploy hadoop")
        for serverid in mesh.servers(clouds=[cloud],
                                     cm_user_id=username)[cloud].keys():
            server =  mesh.servers(clouds=[cloud],
                                   cm_user_id=username)[cloud][serverid]
            try:
                if server["metadata"]["cm_group"] == name:
                    ip=server['addresses']['private'].pop(1)['addr']
                    print(ip)
                    call(["scp","hadoop/hadoop-chef.sh", 
                          "ubuntu@{0}:hadoop".format(ip)])
                    print("installing hadoop  on {0}".format(ip))
                    mesh.ssh_execute(ipaddr=ip, command="chmod +x hadoop")
                    mesh.ssh_execute(ipaddr=ip, command="sudo cp "
                                     "hadoop /usr/bin/")
                    mesh.ssh_execute(ipaddr=ip, command="sudo hadoop")
                    mesh.ssh_execute(ipaddr=ip, command="sudo rm "
                                     "/usr/bin/hadoop")
                    mesh.ssh_execute(ipaddr=ip, command="sudo rm hadoop")
            except:
                pass
        return

