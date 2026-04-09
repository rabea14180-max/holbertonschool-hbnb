import os
import sys
# Add part3 to path so we can import app
sys.path.append(os.path.abspath('part3'))

from part3.app import create_app, db
from part3.app.models.place import Place
from part3.config import DevelopmentConfig

def cleanup():
    app = create_app(DevelopmentConfig)
    with app.app_context():
        # Titles to find and delete
        titles = [
            "Desert Oasis Luxury Villa - Dubai",
            "Traditional Riad - Marrakech"
        ]
        
        for title in titles:
            place = Place.query.filter_by(title=title).first()
            if place:
                print(f"Deleting: {place.title}")
                # Reviews will be deleted automatically if cascade is set, 
                # or we delete them manually. Let's trust the models.
                db.session.delete(place)
                db.session.commit()
                print(f"✅ Deleted {title}")
            else:
                print(f"ℹ️  Not found: {title}")

if __name__ == "__main__":
    cleanup()
