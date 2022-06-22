import os

REDIS_BROKER_URL = os.getenv('REDIS_BROKER_URL', 'redis://localhost:6379/0')
REDIS_BACKEND_URL = os.getenv('REDIS_BACKEND_URL', 'redis://localhost:6379/1')

MONGO_DB_LINK = os.getenv("MONGO_DB_LINK", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DB_NAME", "FakeUserGeneration")

LOGGING_URL = os.getenv("LOGGING_URL", "http://localhost:9880")
HTTP_LOGGING = os.getenv("HTTP_LOGGING", False)
