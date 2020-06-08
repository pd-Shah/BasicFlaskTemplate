from os import environ


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
    IMAGE_UPLOAD_FOLDER = '/images'
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


configs = {
    "development": "settings.DevelopmentConfig",
    "testing": "settings.TestConfig",
    "production": "settings.ProductionConfig",
}

config = configs[environ.get('FLASK_ENV', default="production")]
