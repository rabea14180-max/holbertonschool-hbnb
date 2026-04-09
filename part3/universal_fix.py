import sqlite3
import os
from pathlib import Path

instance_dir = Path(r"c:\Users\REBEA\holbertonschool-hbnb\part3\instance")

def check_and_fix(db_name):
    db_path = instance_dir / db_name
    if not db_path.exists():
        print(f"File not found: {db_name}")
        return
    
    print(f"\nChecking {db_name}...")
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check count
        cursor.execute("SELECT count(*) FROM places")
        count = cursor.fetchone()[0]
        print(f"Current count in {db_name}: {count}")
        
        if count != 4:
            print(f"Purging {db_name} and marking for re-seed...")
            cursor.execute("DELETE FROM reviews")
            cursor.execute("DELETE FROM place_amenity")
            cursor.execute("DELETE FROM places")
            conn.commit()
            print(f"✅ {db_name} purged.")
        conn.close()
    except Exception as e:
        print(f"❌ Error on {db_name}: {e}")

if __name__ == "__main__":
    check_and_fix("development.db")
    check_and_fix("hbnb.db")
    
    print("\nStarting re-seed process...")
    # Run seed_data.py from part3
    import subprocess
    part3_path = Path(r"c:\Users\REBEA\holbertonschool-hbnb\part3")
    res = subprocess.run(["python", "seed_data.py"], cwd=str(part3_path), capture_output=True, text=True)
    print(res.stdout)
