# part3/config.py
import os
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parent / ".env")
except ImportError:
    pass


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key_for_hbnb_app_2026')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key_for_hbnb_app_2026_please_override')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///development.db')

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
