from __future__ import print_function
import cloudmesh
from cloudmesh_common.logger import LOGGER
from cloudmesh_slurm.api.slurm_instance import VirtualSlurm
from subprocess import call

log = LOGGER(__file__)
mesh = cloudmesh.mesh("mongo")
username = cloudmesh.load().username()

class virtual_slurm:

    #This function can not be used because cluster command is not callable
    # use the cluster command to create a cluster
    def create(self, name, datanodes, cloud):
        print("create slurm cluster {0}"
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
        #r = cloudmesh.shell("cluster create --count={0}"
        #                    "--group={1} "
        #                    "--ln=ubuntu".format(datanodes, name))
        #print(r)
        print("cluster created, deploying slurm");
        #deploy slurm on cluster
        #DeploySlurm(name,cloud)
        
        
        return

    def Info(self,name):
        for myslurm in VirtualSlurm.objects(user=username,group=name):
            print("master is {0} \n".format(myslurm.masterip))
            r = mesh.ssh_execute(ipaddr=myslurm.masterip, command="sinfo")
            print(r)
        return

    def Delete(self,name,cloud):
        for myslurm in VirtualSlurm.objects(user=username,group=name):
            print("deleted {0}".format(name))
            myslurm.delete()
        return

    def DeploySlurm(self, name, login, cloud):
        print("Attempting to deploy slurm on cluster"
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
        for myslurm in VirtualSlurm.objects(user=username,group=name):
            print("slurm already deployed, login to master")
            # myslurm.delete()
            print(myslurm.masterip)
            return
        print("deploy slurm")
        ip = ""
        mastername = ""
        for serverid in mesh.servers(clouds=[cloud],
                                     cm_user_id=username)[cloud].keys():
            server =  mesh.servers(clouds=[cloud],
                                   cm_user_id=username)[cloud][serverid]
            
            try:
                if server["metadata"]["cm_group"] == name:
                    ip=server['addresses']['private'].pop(1)['addr']
                    #print(ip)
                    print("installing slurm  on {0}".format(ip))
                    mastername = server["name"].replace("_","-")
                    mesh.ssh_execute(ipaddr=ip, command="echo -e 'Y' |sudo "
                                     "apt-get install slurm-llnl")
                    
            except:
                pass
        VirtualSlurm(user=username,group=name,ln=login,masterip=ip).save()
        # for myslurm in VirtualSlurm.objects(user=username):
        #    print(myslurm.masterip)
        template = open("slurm/slurm.conf.template","r")
        temp = template.read().format(mastername,ip,login)
        masterip = ip
        template.close()
        conf = open("slurm/slurm.conf","w")
        conf.write(temp)
        conf.close()

        conf = open("slurm/slurm.conf","a")
        nodes = ""
        for serverid in mesh.servers(clouds=[cloud],
                                     cm_user_id=username)[cloud].keys():
            server =  mesh.servers(clouds=[cloud],
                                   cm_user_id=username)[cloud][serverid]
            
            try:
                if server["metadata"]["cm_group"] == name:
                    ip=server['addresses']['private'].pop(1)['addr']
                    if ip != masterip:
                        worker = "NodeName={0} NodeAddr={1}\n"
                        worker = worker.format(server["name"].replace("_","-"),
                                               ip)
                        conf.write(worker)
                        nodes = nodes + server["name"].replace("_","-") + ","
                        w = "{0}@{1}:".format(login,ip)
                        call(["scp","slurm/slurmworker",w])
                        mesh.ssh_execute(ipaddr=ip, command="sudo chmod +x"
                                         " slurmworker")
                        mesh.ssh_execute(ipaddr=ip, command="sudo cp"
                                         " slurmworker /usr/bin/")
                        call(["scp","slurm/slurmworker2",w])
                        mesh.ssh_execute(ipaddr=ip, command="sudo chmod +x"
                                         " slurmworker2")
                        mesh.ssh_execute(ipaddr=ip, command="sudo cp"
                                         " slurmworker2 /usr/bin/")
                    else:                 
                        w = "{0}@{1}:".format(login,masterip)
                        call(["scp","slurm/slurmmaster",w])
                        call(["scp","slurm/slurmmaster2",w])
                        mesh.ssh_execute(ipaddr=masterip, command="sudo "
                                         " chmod +x slurmmaster")
                        print("here1")
                        mesh.ssh_execute(ipaddr=masterip, command="sudo "
                                         " chmod +x slurmmaster2")
                        mesh.ssh_execute(ipaddr=masterip, command="sudo cp"
                                         " slurmmaster /usr/bin/")
                        mesh.ssh_execute(ipaddr=masterip, command="sudo cp"
                                         " slurmmaster2 /usr/bin/")
                        print("here2")
                        mesh.ssh_execute(ipaddr=masterip, command="echo -e "
                                         "'N' |sudo slurmmaster")
                        print("here3")
                        mesh.ssh_execute(ipaddr=masterip, command=" "
                                         "/etc/init.d/munge start")
                        
                        # mesh.ssh_execute(ipaddr=masterip, command="sudo "
                        #                  "cp /etc/munge/munge.key 
                        print("here4")
                        call(["scp",w+"/etc/munge/munge.key","slurm/"+name])
            except:
                pass
        nodes = nodes[:-1]
        nodes = "PartitionName=debug Nodes=" + nodes
        nodes = nodes + " Default=YES MaxTime=INFINITE State=UP\n"
        conf.write(nodes)
        conf.write("\n")
        conf.close()
        for serverid in mesh.servers(clouds=[cloud],
                                     cm_user_id=username)[cloud].keys():
            server =  mesh.servers(clouds=[cloud],
                                   cm_user_id=username)[cloud][serverid]
            
            try:
                if server["metadata"]["cm_group"] == name:
                    ip=server['addresses']['private'].pop(1)['addr']
                    if ip != masterip:
                        w = "{0}@{1}:".format(login,ip)
                        call(["scp","slurm/slurm.conf",w])
                        call(["scp","slurm/"+name,w+"munge.key"])
                        mesh.ssh_execute(ipaddr=ip, command="sudo cp"
                                         " munge.key /etc/munge/")
                        mesh.ssh_execute(ipaddr=ip, command="sudo "
                                         "slurmworker ")
                        mesh.ssh_execute(ipaddr=ip, command=" "
                                         "/etc/init.d/munge start")
                        mesh.ssh_execute(ipaddr=ip, command="sudo cp"
                                         " slurm.conf /etc/slurm-llnl/")
                        mesh.ssh_execute(ipaddr=ip, command="sudo "
                                         "slurmworker2 ")
                    else:
                        w = "{0}@{1}:".format(login,masterip)
                        call(["scp","slurm/slurm.conf",w])
                        mesh.ssh_execute(ipaddr=masterip, command="sudo cp"
                                         " slurm.conf /etc/slurm-llnl/")
                        mesh.ssh_execute(ipaddr=masterip, command="sudo "
                                         "slurmmaster2")
            except:
                pass
        return
