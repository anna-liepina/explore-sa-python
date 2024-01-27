import os
import dotenv
from peewee import *

import logging
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

dotenv.load_dotenv()

_host = os.environ.get('DB_HOSTNAME')
_user = os.environ.get('DB_USERNAME')
_password = os.environ.get('DB_PASSWORD')
_port = int(os.environ.get('DB_PORT'))
_name = os.environ.get('DB_NAME')
_dialect = os.environ.get('DB_DIALECT')

replicaHost = os.environ.get('DB_REPLICA_HOSTNAME')
replicaUsername = os.environ.get('DB_REPLICA_USERNAME')
replicaPassword = os.environ.get('DB_REPLICA_PASSWORD')

db = MySQLDatabase(_name, user=_user, password=_password, host=_host, port = _port)

class BaseModel(Model):
    class Meta:
        database = db