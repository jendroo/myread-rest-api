from .dev import *

import environ


env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(str(BASE_DIR / ".env_prod"))

SECRET_KEY = env.str("SECRET_KEY")
DEBUG = env.bool("DEBUG")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env.str("DB_NAME"),
        "USER": env.str("DB_USER"),
        "PASSWORD": env.str("DB_PWD"),
        "HOST": env.str("DB_HOST"),
        "PORT": env.str("DB_PORT"),
    }
}