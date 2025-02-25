import os

POSTGRES_CONFIG = {
    "host": os.getenv("POSTGRESQL_HOST"),
    "database": os.getenv("POSTGRESQL_DATABASE"),
    "user": os.getenv("POSTGRESQL_USER"),
    "password": os.getenv("POSTGRESQL_PASSWORD")
}
