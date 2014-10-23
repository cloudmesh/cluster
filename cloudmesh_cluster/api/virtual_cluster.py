import cloudmesh
from cloudmesh_common.logger import LOGGER

log = LOGGER(__file__)
username = cloudmesh.load().username()

class virtual_cluster:
      
   def delete (self, name):
        print username
        print "delete {0}".format(name)
        log.info("VM CLUSTER: delete {0}".format(name))
        pass
   
   def delete_all (self):
        print username
        print "delete all"
        log.info("VM CLUSTER: delete all")
        pass
   
   def info (self, name):
        print username
        print "info {0}".format(name)
        pass
	
	def clean(self):
        print username
        print "clean vm"
		
 