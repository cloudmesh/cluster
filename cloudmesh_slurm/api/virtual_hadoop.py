from __future__ import print_function
import cloudmesh
from cloudmesh_common.logger import LOGGER
from subprocess import call

log = LOGGER(__file__)

class virtual_hadoop:
    def create(self, name, datanodes):
        print ("create hadoop cluster {0}"
               "with {1} datanodes".format(name, datanodes))
        return

