from cloudmesh.config.cm_config import get_mongo_db, DBConnFactory
from mongoengine import *

class VirtualCluster(Document):
    vuser = StringField(required=True)
    vname = StringField(required=True)
    vworkers = IntField()
    vcloud = StringField()
    vimage = StringField()
    vflavor = StringField()
    meta = {'allow_inheritance': True}
    get_mongo_db("cloudmesh", DBConnFactory.TYPE_MONGOENGINE)
