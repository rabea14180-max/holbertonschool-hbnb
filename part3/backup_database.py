"""
Create a timestamped copy of the SQLite database and verify integrity.

Usage (from part3 folder):
    python backup_database.py

Backups go to: part3/backups/hbnb_backup_YYYYMMDD_HHMMSS.db
"""
from __future__ import annotations

import shutil
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

if load_dotenv:
    load_dotenv(Path(__file__).resolve().parent / ".env")


def sqlite_file_from_url(database_url: str) -> Path | None:
    from sqlalchemy.engine.url import make_url

    u = make_url(database_url)
    if u.drivername != "sqlite" or not u.database:
        return None
    p = Path(u.database)
    if not p.is_absolute():
        p = Path(__file__).resolve().parent / p
    p = p.resolve()
    if p.is_file():
        return p
    # Often created under instance/ when running from Flask app cwd
    alt = Path(__file__).resolve().parent / "instance" / Path(u.database).name
    if alt.is_file():
        return alt.resolve()
    return p


def main() -> int:
    import os

    url = os.getenv("DATABASE_URL", "sqlite:///development.db")
    src = sqlite_file_from_url(url)
    if src is None:
        print("backup_database.py: only sqlite DATABASE_URL is supported.", file=sys.stderr)
        return 1
    if not src.is_file():
        print(f"No database file at: {src}", file=sys.stderr)
        return 1

    conn = sqlite3.connect(str(src))
    try:
        row = conn.execute("PRAGMA integrity_check").fetchone()
        if not row or str(row[0]).lower() != "ok":
            print(f"Integrity check failed: {row}", file=sys.stderr)
            return 1
    finally:
        conn.close()

    backup_dir = Path(__file__).resolve().parent / "backups"
    backup_dir.mkdir(exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dest = backup_dir / f"hbnb_backup_{stamp}.db"
    shutil.copy2(src, dest)
    print(f"OK: {src.name} -> {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
