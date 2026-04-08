#part3/run.py
import importlib

from app import create_app, db
from app.api import create_api
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)
api = create_api(app)

with app.app_context():
    # Must not use "import app.models" here: name `app` is the Flask instance.
    importlib.import_module("app.models")
    db.create_all()

if __name__ == "__main__":
    # use_reloader=False avoids a second process and SQLite quirks while developing.
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

