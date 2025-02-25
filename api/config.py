from api.settings import POSTGRES_CONFIG

def postgres_config():
    return {
        "host": POSTGRES_CONFIG.get("host"),
        "database": POSTGRES_CONFIG.get("database"),
        "user": POSTGRES_CONFIG.get("user"),
        "password": POSTGRES_CONFIG.get("password"),
        "application_name": "incident-fastapi-psycopg2"
    }
