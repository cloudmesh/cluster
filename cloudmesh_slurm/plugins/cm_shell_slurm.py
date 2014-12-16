from cmd3.shell import command
from cloudmesh_common.logger import LOGGER
import cloudmesh
from cloudmesh_slurm.api.virtual_slurm import virtual_slurm

log = LOGGER(__file__)


class cm_shell_slurm:
    """Creating a slurm cluster"""

    def activate_cm_shell_slurm(self):
        self.register_command_topic('platform', 'slurm')
        pass

    @command
    def do_slurm(self, args, arguments):
        """
        Usage:
            slurm info [GROUPNAME]
            slurm deploy GROUPNAME LOGINNAME
            slurm delete GROUPNAME

        Manages a slurm cluster on a cloud

        Arguments:

          GROUPNAME  The name of the slurm cluster
          


        Options:

           -v       verbose mode

        """
        log.info(arguments)

        # if(arguments["create"] and
        #    arguments["GROUPNAME"] and
        #    arguments["DATANODES"]):
        #    virtual_slurm().create("{GROUPNAME}".format(**arguments),
        #                            "{DATANODES}".format(**arguments),
        #                            "india")
        #    return
        if(arguments["deploy"] and
           arguments["GROUPNAME"] and
           arguments["LOGINNAME"]):
            virtual_slurm().DeploySlurm("{GROUPNAME}".format(**arguments),
                                        "{LOGINNAME}".format(**arguments),
                                          "india")
            return
        if(arguments["delete"] and
           arguments["GROUPNAME"]):
            virtual_slurm().Delete("{GROUPNAME}".format(**arguments),
                                          "india")
            return
        return
