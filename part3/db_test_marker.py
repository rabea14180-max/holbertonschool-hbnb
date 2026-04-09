import os
import sys
from pathlib import Path

# Add the part3 directory to the Python path
part3_path = Path(r"c:\Users\REBEA\holbertonschool-hbnb\part3").resolve()
sys.path.append(str(part3_path))

from app import create_app, db
from app.models.place import Place
from app.models.user import User
from config import DevelopmentConfig

def test_db():
    app = create_app(DevelopmentConfig)
    with app.app_context():
        print("🔍 Testing database targeting...")
        admin = User.query.filter_by(email="admin@hbnb.io").first()
        if not admin:
            print("❌ Admin not found")
            return
            
        test_place = Place(
            title="DATABASE_TEST_MARKER",
            description="If you see this, I am hitting this DB",
            price=1.0,
            latitude=0.0,
            longitude=0.0,
            owner_id=admin.id
        )
        db.session.add(test_place)
        db.session.commit()
        print("✅ Added DATABASE_TEST_MARKER")

if __name__ == "__main__":
    test_db()
