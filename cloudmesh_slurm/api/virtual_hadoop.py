from __future__ import print_function
import cloudmesh
from cloudmesh_common.logger import LOGGER
from cloudmesh_slurm.api.hadoop_instance import VirtualHadoop
from subprocess import call

log = LOGGER(__file__)
mesh = cloudmesh.mesh("mongo")
username = cloudmesh.load().username()

class virtual_hadoop:

    #This function can not be used because cluster command is not callable
    # use the cluster command to create a cluster
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
        #DeployHadoop(name,cloud)
        
        
        return
    def Delete(self,name,cloud):
        for myhdp in VirtualHadoop.objects(user=username,group=name):
            print("deleted {0}".format(name))
            myhdp.delete()
        return
    def Info(self, name):
        for myhdp in VirtualHadoop.objects(user=username,group=name):
            print("master is {0} \n".format(myhdp.masterip))
        return

    def DeployHadoop(self, name, login, cloud):
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
                    nodecount += 1
            except:
                pass
        if nodecount < 2:
            print("Warning:Group name does not exist or group has"
                  " less than 2 VMs")
            return
        for myhdp in VirtualHadoop.objects(user=username,group=name):
            print("Hadoop already deployed, login to master")
            print(myhdp.masterip)
            return
        print("deploy hadoop")
        ip = ""
        for serverid in mesh.servers(clouds=[cloud],
                                     cm_user_id=username)[cloud].keys():
            server =  mesh.servers(clouds=[cloud],
                                   cm_user_id=username)[cloud][serverid]
            try:
                if server["metadata"]["cm_group"] == name:
                    ip=server['addresses']['private'].pop(1)['addr']
                    print(ip)
                    call(["scp","hadoop/hadoop-chef.sh", 
                          "{0}@{1}:hadoopsh".format(login,ip)])
                    print("installing hadoop  on {0}".format(ip))
                    mesh.ssh_execute(ipaddr=ip, command="chmod +x hadoopsh")
                    mesh.ssh_execute(ipaddr=ip, command="sudo cp "
                                     "hadoopsh /usr/bin/")
                    mesh.ssh_execute(ipaddr=ip, command="sudo hadoopsh "+login)
                    mesh.ssh_execute(ipaddr=ip, command="sudo rm "
                                     "/usr/bin/hadoopsh")
                    mesh.ssh_execute(ipaddr=ip, command="sudo rm hadoopsh")
            except:
                pass
        mip = ip
        VirtualHadoop(user=username,group=name,ln=login,masterip=ip).save()
        # template = open("hadoop/hadoop.rb.template","r")
        # temp = str(template.read()).format(manager=mip)
        # template.close()
        # hadooprb = open("hadoop/hadoop.rb","w")
        # hadooprb.write(temp)
        # hadooprb.close()
        template = open("hadoop/solo.rb.template","r")
        temp = str(template.read()).format(login)
        template.close()
        solorb = open("hadoop/solo.rb","w")
        solorb.write(temp)
        solorb.close()
        for serverid in mesh.servers(clouds=[cloud],
                                     cm_user_id=username)[cloud].keys():
            server =  mesh.servers(clouds=[cloud],
                                   cm_user_id=username)[cloud][serverid]
            try:
                if server["metadata"]["cm_group"] == name:
                    ip=server['addresses']['private'].pop(1)['addr']
                    if ip != mip:
                       call (["scp","hadoop/hadoop.rb", 
                              "{0}@{1}:".format(login,ip)])
                       mesh.ssh_execute(ipaddr=ip, command=" "
                       "sed -i 's/manager/{0}/g' hadoop.rb".format(mip))

                       mesh.ssh_execute(ipaddr=ip, command="sudo cp "
                                        "hadoop.rb chef-repo/roles/")
                       call (["scp","hadoop/java.rb", 
                              "{0}@{1}:".format(login,ip)])
                       mesh.ssh_execute(ipaddr=ip, command="sudo cp "
                                        "java.rb chef-repo/roles/")
                       call (["scp","hadoop/solo.rb", 
                              "{0}@{1}:".format(login,ip)])
                       mesh.ssh_execute(ipaddr=ip, command="sudo cp "
                                        "solo.rb chef-repo/")
                       call (["scp","hadoop/worker.json", 
                              "{0}@{1}:".format(login,ip)])
                       mesh.ssh_execute(ipaddr=ip, command="sudo cp "
                                        "worker.json chef-repo/")
                       mesh.ssh_execute(ipaddr=ip, command="sudo chef-solo "
                                        "-j worker.json -c solo.rb")
                    else:
                        call (["scp","hadoop/hadoop.rb", 
                               "{0}@{1}:".format(login,ip)])
                        mesh.ssh_execute(ipaddr=mip, command=" "
                                         "sed -i 's/manager/{0}/g' "
                                         "hadoop.rb".format(mip))

                        mesh.ssh_execute(ipaddr=mip, command="sudo cp "
                                         "hadoop.rb chef-repo/roles/")
                        call (["scp","hadoop/java.rb", 
                               "{0}@{1}:".format(login,ip)])
                        mesh.ssh_execute(ipaddr=mip, command="sudo cp "
                                         "java.rb chef-repo/roles/")
                        call (["scp","hadoop/solo.rb", 
                               "{0}@{1}:".format(login,ip)])
                        mesh.ssh_execute(ipaddr=mip, command="sudo cp "
                                         "solo.rb chef-repo/")
                        call (["scp","hadoop/manager.json", 
                               "{0}@{1}:".format(login,ip)])
                        mesh.ssh_execute(ipaddr=mip, command="sudo cp "
                                         "manager.json chef-repo/")
                        mesh.ssh_execute(ipaddr=mip, command="sudo chef-solo "
                                         "-j manager.json -c solo.rb")
                        mesh.ssh_execute(ipaddr=mip, command="echo -e 'Y' |"
                                         "sudo /etc/init.d/"
                                         "hadoop-hdfs-namenode init")
                        
                        mesh.ssh_execute(ipaddr=mip, command="sudo "
                                         "/usr/lib/hadoop/libexec/init-hdfs.sh")
            except:
                pass
        return

