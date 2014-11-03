from cloudmesh.config.cm_config import get_mongo_db, DBConnFactory
from mongoengine import *

class VirtualSlurm(Document):
    user = StringField(required=True)
    name = StringField(required=True)
    workers = IntField()
    cloud = StringField()
    image = StringField()
    flavor = StringField()
    servers = ListField(StrinField())
    ips = ListField(StrinField())
    meta = {'allow_inheritance': True}
    get_mongo_db("cloudmesh", DBConnFactory.TYPE_MONGOENGINE)
