import os
import sys
# Ensure we can import from the current directory
sys.path.append(os.getcwd())

from app import create_app, db
from app.models.place import Place
from app.models.review import Review
from config import DevelopmentConfig
import subprocess

def reset_and_seed():
    app = create_app(DevelopmentConfig)
    with app.app_context():
        print("=" * 50)
        print("HBnB - Database Refinement (Target: 4 Places)")
        print("=" * 50)
        
        # 1. Clear existing Places and Reviews
        print("🗑️ Clearing existing reviews and places...")
        try:
            Review.query.delete()
            Place.query.delete()
            db.session.commit()
            print("✅ Current data cleared.")
        except Exception as e:
            print(f"❌ Error clearing data: {e}")
            db.session.rollback()
            return

        # 2. Run seed_data.py to populate the new diverse set
        print("🌱 Re-seeding with the 4 diverse properties...")
        try:
            # We run it as a subprocess to ensure it uses the updated file content on disk
            result = subprocess.run([sys.executable, "seed_data.py"], capture_output=True, text=True)
            print(result.stdout)
            if result.returncode != 0:
                print(f"❌ Seed script failed: {result.stderr}")
            else:
                print("✅ Seeding completed successfully.")
        except Exception as e:
            print(f"❌ Execution error: {e}")

if __name__ == "__main__":
    reset_and_seed()
