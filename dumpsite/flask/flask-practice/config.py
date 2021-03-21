import os

class Config(object):
    DEBUG=False

class ProductionConfig(Config):
    SECRET_KEY=os.environ.get('SECRET_KEY', 'thisisasupersecretkey')