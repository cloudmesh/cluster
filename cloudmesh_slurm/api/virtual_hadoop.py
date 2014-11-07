from __future__ import print_function
import cloudmesh
from cloudmesh_common.logger import LOGGER

log = LOGGER(__file__)


class virtual_hadoop:

    def create(self, name, datanodes):
        print ("create hadoop cluster {0}"
               "with {1} datanodes".format(name, datanodes))
        r = cloudmesh.shell("cluster create --count={0}"
                            "--group={1} "
                            "--ln=ubuntu".format(datanodes, name))
        print (r)
        return
