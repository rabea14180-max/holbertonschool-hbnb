import sqlite3
import os

db_path = 'part3/instance/development.db'

if not os.path.exists(db_path):
    print(f"Database not found at {db_path}")
    # Try alternate path if called from different directory
    alternate_path = 'instance/development.db'
    if os.path.exists(alternate_path):
        db_path = alternate_path
    else:
        print("Could not find database file.")
        exit(1)

print(f"Opening database at {db_path}...")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

try:
    print("Checking for location_link column in places table...")
    cursor.execute("PRAGMA table_info(places)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'location_link' not in columns:
        print("Adding location_link column...")
        # Use simple ALTER TABLE. For SQLite, this works for adding columns.
        cursor.execute("ALTER TABLE places ADD COLUMN location_link VARCHAR(512)")
        conn.commit()
        print("Successfully added location_link column.")
    else:
        print("Column location_link already exists.")
        
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
