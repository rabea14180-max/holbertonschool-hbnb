import os
import sys
from pathlib import Path

# Add the part3 directory to the Python path
part3_path = Path(r"c:\Users\REBEA\holbertonschool-hbnb\part3").resolve()
sys.path.append(str(part3_path))

from app import create_app, db
from app.models.place import Place
from app.models.review import Review
from config import DevelopmentConfig

def reset_and_seed():
    app = create_app(DevelopmentConfig)
    with app.app_context():
        print("=" * 50)
        print("HBnB - Database Refinement (Final Attempt)")
        print("=" * 50)
        
        # 1. Clear existing Data using direct SQL for reliability
        print("🗑️ Clearing existing reviews and places...")
        try:
            # We use text() to execute raw SQL to ensure order and avoid ORM issues
            from sqlalchemy import text
            db.session.execute(text("DELETE FROM reviews"))
            db.session.execute(text("DELETE FROM place_amenity"))
            db.session.execute(text("DELETE FROM places"))
            db.session.commit()
            print("✅ Current data cleared via SQL.")
        except Exception as e:
            print(f"❌ Error clearing data: {e}")
            db.session.rollback()
            return

        # 2. Re-seeding via our updated seed_data.py but imported directly
        print("🌱 Re-seeding with diverse properties...")
        try:
            # Instead of subprocess, let's just use the logic from seed_data.py 
            # or just run it as a script from this context.
            import seed_data
            # Since seed_data runs on import if __name__ == "__main__" is not used correctly, 
            # I'll just check if it has a functions. 
            # Actually, seed_data.py has everything inside `with app.app_context():` 
            # but it creates its own app.
            
            # I'll just run it as a subprocess from the CORRECT directory
            import subprocess
            res = subprocess.run([sys.executable, "seed_data.py"], cwd=str(part3_path), capture_output=True, text=True)
            print(res.stdout)
            if res.returncode != 0:
                print(f"❌ Error: {res.stderr}")
        except Exception as e:
            print(f"❌ Execution error: {e}")

if __name__ == "__main__":
    reset_and_seed()
