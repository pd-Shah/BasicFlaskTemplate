from os import environ


class Config:
    DEBUG = False
    TESTING = False


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
