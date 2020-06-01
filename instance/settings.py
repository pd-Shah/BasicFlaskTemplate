from os import environ
from os.path import (
    abspath,
    dirname,
    join
)
BASE_DIR = abspath(dirname(__file__))
SQLALCHEMY_DATABASE_URI = environ.get(
    key="DATABASE_URI",
    default="sqlite:///{0}".format(join(BASE_DIR, "bd.db"))
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
