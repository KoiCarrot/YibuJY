import os
class Config(object):
    SECRET_KEY = '\xe2\xae\xd7\xef\xc8\x0e\xff\xad\x0c\xbf\xbf\x8e\xe0\x9d'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}