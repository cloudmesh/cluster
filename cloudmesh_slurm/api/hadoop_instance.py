from cloudmesh.config.cm_config import get_mongo_db, DBConnFactory
from mongoengine import *

class VirtualHadoop(Document):
    user = StringField(required=True)
    group = StringField(required=True)
    ln = StringField(required=True)
    masterip = StringField()
    meta = {'allow_inheritance': True}
    get_mongo_db("cloudmesh", DBConnFactory.TYPE_MONGOENGINE)
