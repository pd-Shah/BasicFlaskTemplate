from os import environ
from os.path import (
    abspath,
    dirname,
    join
)


class Config:
    DEBUG = False
    TESTING = False
    SMTP_SERVER = environ.get("SMTP_SERVER")
    SMTP_USERNAME = environ.get("SMTP_USERNAME")
    SMTP_PASSWROD = environ.get("SMTP_PASSWROD")
    SMTP_USE_TLS = environ.get("SMTP_USE_TLS")
    SMTP_PORT = environ.get("SMTP_PORT")
    SOURCE_SERVER_NAME = environ.get("SOURCE_SERVER_NAME")
    SECRET_KEY = environ.get("SECRET_KEY")
    ADMIN = environ.get("ADMIN")
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    BASE_DIR = abspath(dirname(__file__))


class ProductionConfig(Config):
    UPLOAD_DIR = None


class DevelopmentConfig(Config):
    DEBUG = True
    UPLOAD_DIR = join(Config.BASE_DIR, 'app/packages/authentication/static/images')


class TestConfig(Config):
    TESTING = True
    UPLOAD_DIR = None


configs = {
    "development": "settings.DevelopmentConfig",
    "testing": "settings.TestConfig",
    "production": "settings.ProductionConfig",
}

config = configs[environ.get('FLASK_ENV', default="production")]
