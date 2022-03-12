import os
####
class Config(object):
    ###
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY ='Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')  
    #SQLALCHEMY_DATABASE_URI='postgresql://ujdfdgbvpynvxl:df7d7be9238484017aef112502528d6b80a11bb45e74aafe4d7a4bef816db709@ec2-54-145-249-177.compute-1.amazonaws.com:5432/d2d8u8ek7hfoqj'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = './uploads'
    ######3set DATABASE_URL=postgresql://info3180-project1:info3180-project1@localhost/info3180-project1

class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True


class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False
