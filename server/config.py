import os

# Define if the application is running in debug mode
# Expected value = Boolean
DEBUG = True

# Manual configuration for testing environment
# Expected value = Boolean
TEST_ENV = False

# Define port to run the application on
# Expected value = Integer

# ======================================================================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# ======================================================================

# Defining application credentials
__DATABASE_CRED_SERVER = {
    'USER': 'root',
    'PASSWORD': 'sauran_1993',
    'HOST': 'localhost',
    'PORT': 3306,
    'DB': 'test',
    'CHARSET': 'UTF8'}

__DATABASE_CRED_LOCAL = {
    'USER': 'root',
    'PASSWORD': 'qwerty',
    'HOST': 'localhost',
    'PORT': 3306,
    'DB': 'test',
    'CHARSET': 'UTF8'}

__SERVER_CONFIG_DEV = {
    'PORT': 5500,
    'DEBUG': True,
    'HOST': 'localhost'
}

HASH_SALT_SECRET = "somegarbagewhichhassomeawesomeprice"

DATABASE_CRED = __DATABASE_CRED_LOCAL
SERVER_CONFIG = __SERVER_CONFIG_DEV
