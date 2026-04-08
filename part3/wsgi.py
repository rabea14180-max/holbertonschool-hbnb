"""
WSGI entry for production servers.

    gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

Run from the part3 directory (or set PYTHONPATH).
"""
from run import app
