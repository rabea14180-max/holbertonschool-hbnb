import os
import sys
from pathlib import Path

# Add the part3 directory to the Python path
part3_path = Path(r"c:\Users\REBEA\holbertonschool-hbnb\part3").resolve()
sys.path.append(str(part3_path))

from app import create_app, db
from config import DevelopmentConfig

def find_db():
    app = create_app(DevelopmentConfig)
    with app.app_context():
        print(f"SQLALCHEMY_DATABASE_URI: {app.config['SQLALCHEMY_DATABASE_URI']}")
        
        # Try to get the engine URL
        try:
            from sqlalchemy import inspect
            engine = db.engine
            print(f"Engine URL: {engine.url}")
        except Exception as e:
            print(f"Error getting engine url: {e}")

if __name__ == "__main__":
    find_db()
