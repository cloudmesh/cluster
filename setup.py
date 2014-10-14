<<<<<<< HEAD
#!/usr/bin/env python

#from distutils.core import setup


from setuptools import setup, find_packages
from setuptools.command.install import install
import glob
import os

# try:
#     from fabric.api import local
# except:
#     os.system("pip install fabric")
#     from fabric.api import local

home = os.path.expanduser("~")

class InstallFancy(install):
    """Test of a custom install."""
    def run(self):
        print 70* '+'
        print "Install Fancy"
        print 70* '+'        
        install.run(self)


setup(
    name='cloudmesh_cluster',
    version=__import__('cloudmesh').version(),
    description='An add on to cloudmesh to manage a virtual clouster on cloud environments',
    # description-file =
    #    README.rst
    author='Cloudmesh Team',
    author_email='laszewski@gmail.com',
    url='http://github.org/cloudmesh/cluster',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Clustering',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Boot',
        'Topic :: System :: Systems Administration',
        'Framework :: Flask',
        'Environment :: OpenStack',
    ],
    packages=find_packages(),
    include_package_data=True,
#    data_files=[
#        (home + '/.cloudmesh', [
#            'etc/FGLdapCacert.pem',
#            'etc/india-havana-cacert.pem',
#            'etc/cloudmesh_flavor.yaml']),
#        (home + '/.cloudmesh/etc', [
#            'etc/cloudmesh.yaml',
#            'etc/me-none.yaml',
#            'etc/cloudmesh.yaml',
#            'etc/cloudmesh_server.yaml',
#            'etc/cloudmesh_rack.yaml',
#            'etc/cloudmesh_celery.yaml',
#            'etc/cloudmesh_mac.yaml',
#            'etc/cloudmesh_flavor.yaml',
#            'etc/ipython_notebook_config.py']),
#    ],
#    entry_points={'console_scripts': [
#        'cm-cluster = cloudmesh.cluster.cm_shell_cluster:main',
#    ]},
    cmdclass={
        'install': InstallFancy,
        },
)
=======
"""FutureGrid: Creating a SLURM virtual Cluster via euca2tools

This project creates a virtual cluster with the help of euca
tools. The cluster uses SLURM as resource manager. A simple MPI
program is included to test the functionality. of teh virtual cluster.
"""

from setuptools import setup, find_packages
import sys, os

version = '0.3.0'

# due to a bug we are not including VERION.py yet
# execfile('VERSION.py)

classifiers = """\
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Topic :: Database
Topic :: Software Development :: Libraries :: Python Modules
Operating System :: POSIX :: Linux
Programming Language :: Python :: 2.7
Operating System :: MacOS :: MacOS X
Topic :: Scientific/Engineering
Topic :: System :: Clustering
Topic :: System :: Distributed Computing
"""

if sys.version_info < (2, 7):
    _setup = setup
    def setup(**kwargs):
        if kwargs.has_key("classifiers"):
            del kwargs["classifiers"]
        _setup(**kwargs)

doclines = __doc__.split("\n")


setup(
    name='fgvirtualcluster',
    version=version,
    description = doclines[0],
    classifiers = filter(None, classifiers.split("\n")),
    long_description = "\n".join(doclines[2:]),
    keywords='FutureGrid OpenStack virtual cluster',
    maintainer='Gregor von Laszewski, Xiuwen Yang',
    maintainer_email="laszewski@gmail.com",
    author='Gregor von Laszewski, Xiuwen Yang',
    author_email='laszewski@gmail.com',
    url='https://github.com/futuregrid/virtual-cluster',
    license='Apache 2.0',
    package_dir = {'': '.'},
    packages = find_packages(exclude=['ez_setup', 'examples', 'tests']),
    
    #include_package_data=True,
    #zip_safe=True,
    #install_requires=[
    #    # -*- Extra requirements: -*-
    #],

    
    entry_points={
        'console_scripts': [
                'fg-cluster = fgvirtualcluster.FGCluster:commandline_parser',
                'fg-csh = fgvirtualcluster.FGShell:main',
             ]},

    install_requires = [
             'setuptools',
             'pip',
             'fabric',
             'boto',
             ],
    )

>>>>>>> old/master
