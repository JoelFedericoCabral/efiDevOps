import os

class Settings:
    # Configuración general
    DEBUG = True
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')

    # Configuración de SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



