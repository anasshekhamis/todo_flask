# Configuration

class Config(object):
    """Config class which holds the general configuration"""
    DEBUG = False
    TESTING = False
    # username and password could be fetched from an environment file, but skipped simplicity
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/todo_flask'


class ProductionConfig(Config):
    """Production configuration where debug should be turned off"""
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configuration where debug should be turned on"""
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
