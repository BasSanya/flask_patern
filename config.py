import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or \
                 '1YrZ69cfWb0rYHll1NhOmAdSSdCqzt4LJrJMIkgj238Hzoxzqdmdv62kB0dndfu7HPZPVYMmwzMZ1hP'
    SQLALCHEMY_TRACK_MODIFICATION = False

    # config for email, smtp server
    MAIL_SERVER = ''
    MAIL_PORT = 0
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or ''
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or ''
    MAIL_DEFAULT_SENDER = MAIL_USERNAME


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI') or \
                              'postgresql+psycopg2://flask_user:Qq123456789@localhost:5432/programmer_blog'


class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI') or \
                              ''

class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI') or \
                              ''
