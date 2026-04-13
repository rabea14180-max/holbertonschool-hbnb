"""
seed_data.py -- populate the database with realistic data
Usage:
    python seed_data.py
"""
import importlib
from config import DevelopmentConfig
from app import create_app, db
from app.models.user import User
from app.models.amenity import Amenity
from app.models.place import Place
from app.models.review import Review

app = create_app(DevelopmentConfig)

with app.app_context():
    # Import all models to register tables
    importlib.import_module("app.models")

    # Create tables if they do not exist (without deleting current data)
    db.create_all()

    print("=" * 50)
    print("  HBnB - Populating realistic data")
    print("=" * 50)

    # ------------------------------------------------------------------
    # 1. Admin user
    # ------------------------------------------------------------------
    admin = User.query.filter_by(email="admin@hbnb.io").first()
    if not admin:
        admin = User(
            first_name="Admin",
            last_name="HBnB",
            email="admin@hbnb.io",
            password="Admin1234!",
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print(f"✅ Admin created: admin@hbnb.io / Admin1234!")
    else:
        print(f"ℹ️  Admin already exists: admin@hbnb.io")

    # ------------------------------------------------------------------
    # 2. Regular users
    # ------------------------------------------------------------------
    users_data = [
        {"first_name": "Sarah", "last_name": "Johnson", "email": "sarah.johnson@email.com", "password": "Pass1234!"},
        {"first_name": "Mohammed", "last_name": "Al-Rashid", "email": "m.alrashid@email.com", "password": "Pass1234!"},
        {"first_name": "Emily", "last_name": "Chen", "email": "emily.chen@email.com", "password": "Pass1234!"},
        {"first_name": "Carlos", "last_name": "Garcia", "email": "carlos.garcia@email.com", "password": "Pass1234!"},
        {"first_name": "Aisha", "last_name": "Ndiaye", "email": "aisha.ndiaye@email.com", "password": "Pass1234!"},
    ]

    created_users = []
    for ud in users_data:
        existing = User.query.filter_by(email=ud["email"]).first()
        if not existing:
            user = User(**ud)
            db.session.add(user)
            db.session.commit()
            created_users.append(user)
            print(f"✅ User created: {ud['email']}")
        else:
            created_users.append(existing)
            print(f"ℹ️  User exists: {ud['email']}")

    # ------------------------------------------------------------------
    # 3. Amenities
    # ------------------------------------------------------------------
    amenities_data = [
        {"name": "WiFi",              "description": "High-speed wireless internet up to 500 Mbps"},
        {"name": "Swimming Pool",     "description": "Heated outdoor/indoor pool"},
        {"name": "Air Conditioning",  "description": "Climate-controlled rooms"},
        {"name": "Free Parking",      "description": "Dedicated free parking space"},
        {"name": "Kitchen",           "description": "Fully equipped modern kitchen"},
        {"name": "Washer",            "description": "In-unit washer and dryer"},
        {"name": "TV",                "description": "Smart TV with Netflix & satellite"},
        {"name": "Workspace",         "description": "Dedicated work desk with high-speed internet"},
        {"name": "Gym",               "description": "Fully-equipped fitness center"},
        {"name": "Balcony",           "description": "Private balcony with scenic views"},
        {"name": "Beach Access",      "description": "Direct private beach access"},
        {"name": "BBQ Grill",         "description": "Outdoor BBQ and patio area"},
    ]

    amenity_objects = {}
    for ad in amenities_data:
        existing = Amenity.query.filter_by(name=ad["name"]).first()
        if not existing:
            amenity = Amenity(**ad)
            db.session.add(amenity)
            db.session.commit()
            amenity_objects[ad["name"]] = amenity
            print(f"✅ Amenity created: {ad['name']}")
        else:
            amenity_objects[ad["name"]] = existing
            print(f"ℹ️  Amenity exists: {ad['name']}")

    # ------------------------------------------------------------------
    # 4. Places - realistic sample data
    # ------------------------------------------------------------------
    places_data = [
        {
            "title": "Luxury Beachfront Villa - Miami",
            "description": "Stunning 4-bedroom villa directly on Miami Beach. Enjoy breathtaking ocean views from every room. Features a private heated pool, chef's kitchen, and outdoor entertainment area. Perfect for families and groups looking for the ultimate Florida experience.",
            "price": 450.0,
            "latitude": 25.7617,
            "longitude": -80.1918,
            "owner": created_users[0],
            "amenities": ["WiFi", "Swimming Pool", "Air Conditioning", "Free Parking", "Kitchen", "Washer", "TV", "Beach Access", "BBQ Grill"],
            "reviews": [
                {"user": created_users[1], "text": "Absolutely stunning villa! The ocean view is breathtaking and the pool was perfect. Would definitely book again.", "rating": 5},
                {"user": created_users[2], "text": "Amazing location right on the beach. The kitchen was well-stocked and the space was immaculately clean.", "rating": 5},
                {"user": created_users[3], "text": "Great place but a bit pricey. The beach access was incredible and the pool was lovely.", "rating": 4},
            ]
        },
        {
            "title": "Cozy Mountain Cabin - Swiss Alps",
            "description": "Charming wooden cabin nestled in the Swiss Alps at 1,800m altitude. Wake up to panoramic mountain views, enjoy the crackling fireplace in the evenings. Perfect ski-in/ski-out access in winter, hiking trails in summer.",
            "price": 185.0,
            "latitude": 46.5197,
            "longitude": 7.9009,
            "owner": created_users[1],
            "amenities": ["WiFi", "Air Conditioning", "Free Parking", "Kitchen", "Washer", "TV", "Workspace"],
            "reviews": [
                {"user": created_users[0], "text": "A magical mountain retreat! The fireplace, the views, the peace and quiet — everything was perfect.", "rating": 5},
                {"user": created_users[4], "text": "We stayed for a week and didn't want to leave. The cabin is warm, cozy and the host was very helpful.", "rating": 5},
            ]
        },
        {
            "title": "Modern City Apartment - Paris",
            "description": "Sleek and stylish 2-bedroom apartment in the heart of Paris, just 5 minutes walk from the Eiffel Tower. Floor-to-ceiling windows, designer furniture, and a fully equipped kitchen. Experience the City of Light like a local.",
            "price": 220.0,
            "latitude": 48.8566,
            "longitude": 2.3522,
            "owner": created_users[2],
            "amenities": ["WiFi", "Air Conditioning", "Kitchen", "Washer", "TV", "Workspace"],
            "reviews": [
                {"user": created_users[0], "text": "Perfect Paris apartment! Location was unbeatable, the apartment itself was gorgeous. Highly recommended!", "rating": 5},
                {"user": created_users[1], "text": "Beautiful apartment in a great central location. Very clean and exactly as described.", "rating": 4},
                {"user": created_users[3], "text": "Great location, nice apartment. The Eiffel Tower view from the window was just magical.", "rating": 5},
            ]
        },
        {
            "title": "Historic Castle Suite - Edinburgh",
            "description": "Unique opportunity to stay in a converted 16th-century castle on the outskirts of Edinburgh. Stone walls, vaulted ceilings, and original period features throughout. Private grounds with gardens, and stunning views of the Scottish Highlands.",
            "price": 290.0,
            "latitude": 55.9533,
            "longitude": -3.1883,
            "owner": created_users[2],
            "amenities": ["WiFi", "Free Parking", "Kitchen", "TV"],
            "reviews": [
                {"user": created_users[0], "text": "A once-in-a-lifetime experience! Staying in a real castle was magical. The rooms are stunning and the grounds are beautiful.", "rating": 5},
                {"user": created_users[3], "text": "Absolutely incredible property. The castle is authentic and full of history. Will definitely return.", "rating": 5},
            ]
        },
    ]

    print("\n📍 Adding places and reviews...")
    for pd in places_data:
        # Check if place already exists
        existing_place = Place.query.filter_by(title=pd["title"]).first()
        if existing_place:
            print(f"ℹ️  Place exists: {pd['title']}")
            continue

        # Create place
        place = Place(
            title=pd["title"],
            description=pd["description"],
            price=pd["price"],
            latitude=pd["latitude"],
            longitude=pd["longitude"],
            owner_id=pd["owner"].id,
        )
        db.session.add(place)
        db.session.flush()  # get place.id before commit

        # Link amenities
        for amenity_name in pd["amenities"]:
            amenity = amenity_objects.get(amenity_name)
            if amenity:
                place.amenities.append(amenity)

        db.session.commit()
        print(f"✅ Place created: {pd['title']}")

        # Add reviews
        for rd in pd.get("reviews", []):
            # Don't let user review their own place
            if rd["user"].id == pd["owner"].id:
                continue
            review = Review(
                text=rd["text"],
                rating=rd["rating"],
                user_id=rd["user"].id,
                place_id=place.id
            )
            db.session.add(review)

        db.session.commit()
        print(f"   ➕ {len(pd.get('reviews', []))} reviews added")

    print("\n" + "=" * 50)
    print("✅ All data has been added successfully!")
    print("=" * 50)
    print(f"\n📊 Database summary:")
    print(f"   👤 Users:     {User.query.count()}")
    print(f"   🏠 Places:    {Place.query.count()}")
    print(f"   ⭐ Amenities: {Amenity.query.count()}")
    from app.models.review import Review
    print(f"   💬 Reviews:   {Review.query.count()}")
    print("\n🔑 Login credentials:")
    print("   Admin:  admin@hbnb.io  / Admin1234!")
    print("   User:   sarah.johnson@email.com / Pass1234!")
