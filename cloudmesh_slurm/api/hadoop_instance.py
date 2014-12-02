from cloudmesh.config.cm_config import get_mongo_db, DBConnFactory
from mongoengine import *

class VirtualHadoop(Document):
    user = StringField(required=True)
    groupname = StringField(required=True)
    nodes = IntField()
    managerip = StringField()
    workerips = ListField(StringField())
    meta = {'allow_inheritance': True}
    get_mongo_db("cloudmesh", DBConnFactory.TYPE_MONGOENGINE)
