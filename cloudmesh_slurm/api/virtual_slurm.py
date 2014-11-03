import cloudmesh
from cloudmesh_common.logger import LOGGER
from cloudmesh.cm_mongo import cm_mongo
#from cloudmesh.config.cm_config import get_mongo_db
from cloudmesh_slurm.api.slurm_instance import VirtualSlurm

'''collection = "cloudmesh"
dbconn = get_mongo_db(collection)
cm=cm_mongo()'''
log = LOGGER(__file__)
username = cloudmesh.load().username()
vclock=cloudmesh.util.stopwatch.StopWatch()
cloudmanage = cloudmesh.iaas.cm_cloud.CloudManage()
mesh = cloudmesh.mesh("mongo")
#mesh.activate(username)

class virtual_slurm:
      
   def delete (self, name):
        print username
        print "delete {0}".format(name)
        log.info("VM SLURM: delete {0}".format(name))
        vclock.start(username)
        pass
   
   def delete_all (self):
        print username
        print "delete all"
        log.info("VM SLURM: delete all")
        print vclock.get(username)
        pass
   
   def info (self, name):
        print username
        print "info {0}".format(name)
        for vc in VirtualSlurm.objects:
            print "cloud {0} workers {1}".format(vc.vcloud,vc.vworkers)
        '''#vclock.stop(username)
        satest={"name" : "tester", "text":"my first document"}
        #print dbconn.insert(satest)
        #print dbconn.find_one({"name" : "tester"})
        for item in dbconn.find():
            print item'''
        pass

   def create(self, name,workers,cloud,image,flavor):
        clouds = cloudmesh.load().cloudnames()
        if cloud in clouds:
           print "cloud {c} exits".format(c=cloud)
        flavors = mesh.flavors(cm_user_id=username, clouds=[cloud])
        if flavor in flavors[cloud]:
           print flavor
        images = mesh.images(clouds=[cloud],cm_user_id=username)
        if image in images[cloud]:
           print image
        VirtualSlurm(vuser=username,
                       vname=name,
                       vworkers=workers,
                       vcloud=cloud,
                       vimage=image,
                       vflavor=flavor).save()
        '''for serverid in mesh.servers(clouds=["india"],cm_user_id=username)["india"].keys():
            server =  mesh.servers(clouds=["india"],cm_user_id=username)["india"][serverid]
            print server['name']'''
        print "create name={n} workers={w} cloud={c} image={i} flavor={f}".format(n=name,
                                                                                  w=workers,
                                                                                  c=cloud,
                                                                                  i=image,
                                                                                  f=flavor)
        #for mycloud in cloudmanage.get_clouds(username):
        #    print mycloud['cm_cloud']
        #for myimage in cloudmanage.get_images(True):
        #    print myimage['name']
        #if mycloud in cloudmanage.get_coulds(username)
        pass
