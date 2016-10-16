import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  SECRET_KEY = 'bj68t3uybeh49u3dxhf4ui433h'
  MONGODB_DB = 'eduequip'
  MONGODB_USERNAME = 'ravingupta2309'
  MONGODB_PASSWORD = 'RavinGupta2309'
  MONGODB_REPLICASET = None
  MONGODB_HOST = 'mongodb://ravingupta2309:RavinGupta2309@ds013916.mlab.com:13916/eduequip'
  MONGODB_PORT = 13916

class ProductionConfig(Config):
  DEBUG = False

class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True