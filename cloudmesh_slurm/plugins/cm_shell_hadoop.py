from cmd3.shell import command
from cloudmesh_common.logger import LOGGER
import cloudmesh
from cloudmesh_slurm.api.virtual_hadoop import virtual_hadoop

log = LOGGER(__file__)


class cm_shell_hadoop:
    """Creating a hadoop cluster"""

    def activate_cm_shell_hadoop(self):
        self.register_command_topic('platform', 'hadoop')
        pass

    @command
    def do_hadoop(self, args, arguments):
        """
        Usage:
            hadoop info GROUPNAME
            hadoop deploy GROUPNAME LOGINNAME
            hadoop delete GROUPNAME

        Manages a hadoop cluster on a cloud

        Arguments:

          GROUPNAME  The name of the hadoop cluster
          DATANODES  The number of datanodes in the hadoop cluster


        Options:

           -v       verbose mode

        """
        log.info(arguments)

        
        if(arguments["deploy"] and
           arguments["GROUPNAME"] and
           arguments["LOGINNAME"]):
            virtual_hadoop().DeployHadoop("{GROUPNAME}".format(**arguments),
                                          "{LOGINNAME}".format(**arguments),
                                          "india")
            return
        if(arguments["info"] and
           arguments["GROUPNAME"]):
            virtual_hadoop().Info("{GROUPNAME}".format(**arguments))
            return
        if(arguments["delete"] and
           arguments["GROUPNAME"]):
            virtual_hadoop().Delete("{GROUPNAME}".format(**arguments),
                                          "india")
            return
        return
