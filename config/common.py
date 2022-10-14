from constants.database import LOGIN, PASSWORD, NAME

PRODUCTION = False

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{LOGIN}:{PASSWORD}@localhost/{NAME}'
SQLALCHEMY_ECHO = True
