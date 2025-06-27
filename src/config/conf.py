import os
from dotenv import load_dotenv

load_dotenv()

class BaseConf():
    def getBoolEnv(var_name, default=False):
        val = os.getenv(var_name, str(default))
        return val.lower() in ('true', '1', 't', 'yes', 'y')
    
    APP_NAME = os.getenv("APP_NAME")
    APP_VERSION = os.getenv("APP_VERSION")
    HOST = os.getenv("HOST")
    PORT_API = os.getenv("PORT_API")
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = getBoolEnv("DEBUG")
    TESTING = getBoolEnv("TESTING")
    ENV_DEV = getBoolEnv("ENV_DEV")

    MONGODB_USER = os.getenv("MONGODB_USER")
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD")
    MONGODB_HOST = os.getenv("MONGODB_HOST")
    MONGODB_PORT = os.getenv("MONGODB_PORT")
    MONGODB_DB = os.getenv("MONGODB_DB")
    MONGODB_ACTIVE = getBoolEnv("MONGODB_ACTIVE")

    # SMTP_HOST = os.getenv("SMTP_HOST")
    # SMTP_PORT = os.getenv("SMTP_PORT")
    # SMTP_USER = os.getenv("SMTP_USER")
    # SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

    # GOOGLE_AUTENTICATION_CLIENT_ID = os.getenv("GOOGLE_AUTENTICATION_CLIENT_ID")
    # GOOGLE_AUTHENTICATION_CLIENT_SECRET = os.getenv("GOOGLE_AUTHENTICATION_CLIENT_SECRET")

    # CODE_URL_API_COMPILATOR = os.getenv("CODE_URL_API_COMPILATOR")
    # CODE_COMPILATOR_CLIENT_ID = os.getenv("CODE_COMPILATOR_CLIENT_ID")
    # CODE_COMPILATOR_CLIENT_SECRET = os.getenv("CODE_COMPILATOR_CLIENT_SECRET")

    CODE_IA_API_KEY = os.getenv("CODE_IA_API_KEY")
    CODE_IA_CLIENT_ID = os.getenv("CODE_IA_CLIENT_ID")
    CODE_IA_CLIENT_SECRET = os.getenv("CODE_IA_CLIENT_SECRET")

    PUBLISHER_URL = os.getenv("PUBLISHER_URL") # En aca va el url de la api para guardar codigo
    PUBLISHER_USER = os.getenv("PUBLISHER_USER")
    PUBLISHER_PASSWORD = os.getenv("PUBLISHER_PASSWORD")

class DevConf(BaseConf):
    pass

class ProdConf(BaseConf):
    DEBUG = os.getenv("DEBUG")
    TESTING = os.getenv("TESTING")
    pass