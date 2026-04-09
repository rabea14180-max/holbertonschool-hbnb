import sqlite3
import os
from pathlib import Path

def scatter_marker(root_path):
    admin_id = "60e13da9-945f-44a0-9a8e-e4da8aff96cd" # Known Admin ID from API response
    
    for path in Path(root_path).rglob("*.db"):
        print(f"Targeting {path}...")
        try:
            conn = sqlite3.connect(path)
            cursor = conn.cursor()
            
            # Check if places table exists
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='places'")
            if not cursor.fetchone():
                print(f"   No places table in {path.name}")
                continue
            
            cursor.execute("INSERT INTO places (id, title, description, price, latitude, longitude, owner_id) VALUES (?, ?, ?, ?, ?, ?, ?)",
                          (str(os.urandom(16).hex()), "SCATTER_MARKER_" + path.name, "Scatter test", 1.0, 0.0, 0.0, admin_id))
            conn.commit()
            print(f"   ✅ Marker added to {path}")
            conn.close()
        except Exception as e:
            print(f"   ❌ Error: {e}")

if __name__ == "__main__":
    scatter_marker(r"c:\Users\REBEA\holbertonschool-hbnb\part3")
