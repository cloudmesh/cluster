from __future__ import print_function
import cloudmesh
from cloudmesh_common.logger import LOGGER
from cloudmesh.cm_mongo import cm_mongo
# from cloudmesh.config.cm_config import get_mongo_db
from cloudmesh_slurm.api.slurm_instance import VirtualSlurm
from subprocess import call

'''collection = "cloudmesh"
dbconn = get_mongo_db(collection)
cm=cm_mongo()'''
log = LOGGER(__file__)
username = cloudmesh.load().username()
vclock = cloudmesh.util.stopwatch.StopWatch()
cloudmanage = cloudmesh.iaas.cm_cloud.CloudManage()
mesh = cloudmesh.mesh("mongo")
mesh.activate(username)

class virtual_slurm:
    def delete(self, name):
        print ("deleted {name}".format(name=name))
        for myvc in VirtualSlurm.objects(user=username, name=name):
            servers = myvc.servers
            # print servers
            for i, server in enumerate(servers):
                mesh.delete(myvc.cloud, server, username)
            myvc.delete()
        log.info("VM CLUSTER: delete {0}".format(name))
        # vclock.start(username)
        pass

    def delete_all(self):
        print ("deleted all clusters of {user}".format(user=username))
        for myvc in VirtualSlurm.objects(user=username):
            servers = myvc.servers
            for i, server in enumerate(servers):
                mesh.delete(myvc.cloud, server, username)
            myvc.delete()
        log.info("VM CLUSTER: delete all of {user}".format(user=username))
        # print vclock.get(username)
        pass

    def info(self, name):
        for vc in VirtualSlurm.objects(name=name):
            print ("name= {0} "
                   "cloud= {1} "
                   "workers= {2} "
                   "image={3} "
                   "flavor={4}".format(vc.name,
                                       vc.cloud,
                                       vc.workers,
                                       vc.image,
                                       vc.flavor))
        pass

        #
        # # vclock.stop(username)
        #  satest={"name" : "tester", "text":"my first document"}
        # #  print dbconn.insert(satest)
        # #  print dbconn.find_one({"name" : "tester"})
        #  for item in dbconn.find():
        #     print item
        # pass

    def info_all(self):
        for vc in VirtualSlurm.objects:
            print("name= {0} cloud= {1} "
                  "workers= {2} image={3} flavor={4}".format(vc.name,
                                                             vc.cloud,
                                                             vc.workers,
                                                             vc.image,
                                                             vc.flavor))
        pass

    def list_clusters(self):
        # call(["ls","-alrt"])
        for vc in VirtualSlurm.objects:
            print("{0}").format(vc.name)
        pass

    def defaults(self, name, workers, cloud, image, flavor):
        pass

    def create_defaults(self):
        pass

    def create(self, vc_name, vc_workers, vc_cloud, vc_image, vc_flavor):
        clouds = cloudmesh.load().cloudnames()
        if vc_cloud not in clouds:
            print("cloud {c} does not exit".format(c=vc_cloud))
            return
        flavors = mesh.flavors(cm_user_id=username, clouds=[vc_cloud])
        vc_flavor_flag = True
        for key in flavors[vc_cloud].values():
            if vc_flavor == key["name"]:
                vc_flavor_flag = False
        if vc_flavor_flag  and vc_flavor != "None":
            print("flavor {f} does not exit".format(f=vc_flavor))
            return
        images = mesh.images(clouds=[vc_cloud], cm_user_id=username)
        vc_image_flag = True
        for key in images[vc_cloud].values():
            if vc_image == key["name"]:
                vc_image_flag = False
        if vc_image_flag and vc_image != "None":
            print("image {i} does not exit".format(i=vc_image))
            return
        myvc = VirtualSlurm(user=username,
                              name=vc_name,
                              workers=vc_workers,
                              cloud=vc_cloud,
                              image=vc_image,
                              flavor=vc_flavor).save()
        for vm in range(0, int(vc_workers)):
            if vc_flavor == "None" or vc_image == "None":
                result = mesh.start(cloud=vc_cloud, cm_user_id=username)
            else:
                result = mesh.start(cloud=vc_cloud,
                                    cm_user_id=username,
                                    flavor=vc_flavor,
                                    image=vc_image)
            # print result
            server = result['server']['id']
            # print server
            myvc.servers.append(server)
            ip = mesh.assign_public_ip(vc_cloud, server, username)
            myvc.ips.append(ip)
            myvc.save()
        '''for serverid in mesh.servers(clouds=["india"],
                   cm_user_id=username)["india"].keys():
            server =  mesh.servers(clouds=["india"],
            cm_user_id=username)["india"][serverid]
            print server['name']'''
        
            
        print ("create name={0}workers={1} "
               "cloud={2} image={3} flavor={4}".format(vc_name,
                                                       vc_workers,
                                                       vc_cloud,
                                                       vc_image,
                                                       vc_flavor))
        # for mycloud in cloudmanage.get_clouds(username):
        #     print mycloud['cm_cloud']
        # for myimage in cloudmanage.get_images(True):
        #     print myimage['name']
        # if mycloud in cloudmanage.get_coulds(username)
        pass
