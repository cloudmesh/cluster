from fabric.api import task, local
from cloudmesh_install.util import banner

import os


@task
def dir():
    """clean the dirs"""
    banner("CLEAN DIR")
    local("rm -rf *.egg")
    local('find . -name "*~" -exec rm {} \;  ')
    local('find . -name "*.pyc" -exec rm {} \;  ')
    local("rm -rf build dist *.egg-info *~ #*")
    # local("cd docs; make clean")
    local("rm -rf *.egg-info")
    local("rm -f *.dump")

