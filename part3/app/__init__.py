from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from sqlalchemy import event
from sqlalchemy import text

# Instances
db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()


def _register_sqlite_pragmas(app):
    """WAL + foreign keys + busy timeout for safer concurrent reads / fewer lock errors."""

    uri = app.config.get("SQLALCHEMY_DATABASE_URI") or ""
    if not str(uri).startswith("sqlite"):
        return

    with app.app_context():

        @event.listens_for(db.engine, "connect")
        def _on_sqlite_connect(dbapi_connection, connection_record):
            import sqlite3

            if not isinstance(dbapi_connection, sqlite3.Connection):
                return
            cur = dbapi_connection.cursor()
            cur.execute("PRAGMA journal_mode=WAL")
            cur.execute("PRAGMA foreign_keys=ON")
            cur.execute("PRAGMA busy_timeout=5000")
            cur.close()


def create_app(config_class="config.DevelopmentConfig"):
    """
    Application Factory
    """
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(config_class)

    # Enable CORS
    CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

    # Initialize extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    _register_sqlite_pragmas(app)

    @app.route("/health")
    def health():
        """Liveness + DB connectivity (for monitoring or quick checks)."""
        try:
            db.session.execute(text("SELECT 1"))
        except Exception:
            return {"status": "unhealthy", "database": "error"}, 503
        return {"status": "ok", "database": "ok"}, 200

    _register_api_error_handlers(app)

    return app


def _register_api_error_handlers(app):
    """Consistent JSON errors for /api routes (cleaner clients + monitoring)."""

    @app.errorhandler(404)
    def handle_404(e):
        if request.path.startswith("/api"):
            return jsonify({"error": "Not found"}), 404
        return "Not Found", 404

    @app.errorhandler(405)
    def handle_405(e):
        if request.path.startswith("/api"):
            return jsonify({"error": "Method not allowed"}), 405
        return "Method Not Allowed", 405

    @app.errorhandler(500)
    def handle_500(e):
        if request.path.startswith("/api"):
            return jsonify({"error": "Internal server error"}), 500
        raise e
