"""
populate_via_api.py -- يضيف بيانات حقيقية عبر الـ API مباشرةً
استخدام:
    python populate_via_api.py
"""
import requests
import json

BASE = "http://127.0.0.1:5000/api/v1"

def step(msg):
    print(f"\n{'='*50}\n{msg}\n{'='*50}")

# ------------------------------------------------------------------
# 1. تسجيل الدخول كـ Admin
# ------------------------------------------------------------------
step("1. تسجيل الدخول كـ Admin")
r = requests.post(f"{BASE}/users/login", json={"email": "admin@hbnb.io", "password": "Admin1234!"})
if r.status_code != 200:
    print(f"❌ فشل تسجيل الدخول: {r.status_code} {r.text}")
    print("محاولة إنشاء Admin أولاً...")
    r2 = requests.post(f"{BASE}/users/register", json={
        "first_name": "Admin", "last_name": "HBnB",
        "email": "admin@hbnb.io", "password": "Admin1234!", "is_admin": True
    })
    print(f"Register: {r2.status_code} {r2.text}")
    r = requests.post(f"{BASE}/users/login", json={"email": "admin@hbnb.io", "password": "Admin1234!"})
    if r.status_code != 200:
        print(f"❌ فشل تسجيل الدخول مجدداً: {r.text}")
        exit(1)

admin_token = r.json()["access_token"]
admin_headers = {"Authorization": f"Bearer {admin_token}", "Content-Type": "application/json"}
print(f"✅ Admin token received")

# ------------------------------------------------------------------
# 2. إضافة المستخدمين العاديين
# ------------------------------------------------------------------
step("2. إضافة المستخدمين")
users_data = [
    {"first_name": "Sarah",    "last_name": "Johnson",   "email": "sarah.j@email.com",   "password": "Pass1234!"},
    {"first_name": "Mohammed", "last_name": "Al-Rashid", "email": "m.rashid@email.com",  "password": "Pass1234!"},
    {"first_name": "Emily",    "last_name": "Chen",      "email": "emily.c@email.com",   "password": "Pass1234!"},
    {"first_name": "Carlos",   "last_name": "Garcia",    "email": "carlos.g@email.com",  "password": "Pass1234!"},
    {"first_name": "Aisha",    "last_name": "Ndiaye",    "email": "aisha.n@email.com",   "password": "Pass1234!"},
]

user_tokens = {}
user_ids = {}
for ud in users_data:
    r = requests.post(f"{BASE}/users/register", json=ud)
    if r.status_code == 201:
        uid = r.json().get("id")
        user_ids[ud["email"]] = uid
        print(f"✅ User created: {ud['first_name']} {ud['last_name']} (id={uid})")
    elif r.status_code == 400 and "already registered" in r.text:
        # User exists, login to get id
        lr = requests.post(f"{BASE}/users/login", json={"email": ud["email"], "password": ud["password"]})
        if lr.ok:
            import base64, json as jmod
            payload = lr.json()["access_token"].split(".")[1]
            payload += "=" * (4 - len(payload) % 4)
            claims = jmod.loads(base64.b64decode(payload))
            user_ids[ud["email"]] = claims.get("sub")
            print(f"ℹ️  User exists: {ud['first_name']} {ud['last_name']}")
    else:
        print(f"⚠️  {ud['email']}: {r.status_code} {r.text}")

    # Get token for each user (for reviews)
    lr = requests.post(f"{BASE}/users/login", json={"email": ud["email"], "password": ud["password"]})
    if lr.ok:
        user_tokens[ud["email"]] = lr.json()["access_token"]

# ------------------------------------------------------------------
# 3. إضافة وسائل الراحة (Amenities) - Admin only
# ------------------------------------------------------------------
step("3. إضافة وسائل الراحة")
amenities_data = [
    {"name": "WiFi",             "description": "High-speed wireless internet up to 500 Mbps"},
    {"name": "Swimming Pool",    "description": "Heated outdoor/indoor pool"},
    {"name": "Air Conditioning", "description": "Climate-controlled rooms"},
    {"name": "Free Parking",     "description": "Dedicated free parking space"},
    {"name": "Kitchen",          "description": "Fully equipped modern kitchen"},
    {"name": "Washer",           "description": "In-unit washer and dryer"},
    {"name": "TV",               "description": "Smart TV with Netflix and satellite"},
    {"name": "Workspace",        "description": "Dedicated work desk with high-speed internet"},
    {"name": "Gym",              "description": "Fully-equipped fitness center"},
    {"name": "Balcony",          "description": "Private balcony with scenic views"},
    {"name": "Beach Access",     "description": "Direct private beach access"},
    {"name": "BBQ Grill",        "description": "Outdoor BBQ and patio area"},
]

amenity_ids = {}
existing_r = requests.get(f"{BASE}/amenities")
if existing_r.ok:
    for a in existing_r.json():
        amenity_ids[a["name"]] = a["id"]
        print(f"ℹ️  Amenity exists: {a['name']}")

for ad in amenities_data:
    if ad["name"] in amenity_ids:
        continue
    r = requests.post(f"{BASE}/amenities", json=ad, headers=admin_headers)
    if r.status_code == 201:
        amenity_ids[ad["name"]] = r.json()["id"]
        print(f"✅ Amenity: {ad['name']}")
    else:
        print(f"⚠️  {ad['name']}: {r.status_code} {r.text}")

# ------------------------------------------------------------------
# 4. إضافة الأماكن والتقييمات
# ------------------------------------------------------------------
step("4. إضافة الأماكن والتقييمات")

def get_amenity_ids(names):
    return [amenity_ids[n] for n in names if n in amenity_ids]

# Helper: get user token
def tok(email):
    return {"Authorization": f"Bearer {user_tokens.get(email, '')}", "Content-Type": "application/json"}

places_config = [
    {
        "place": {"title": "Luxury Beachfront Villa - Miami", "description": "Stunning 4-bedroom villa directly on Miami Beach. Breathtaking ocean views, private heated pool, chef's kitchen, and outdoor entertainment area. Perfect for families seeking the ultimate Florida experience.", "price": 450.0, "latitude": 25.7617, "longitude": -80.1918, "amenities": get_amenity_ids(["WiFi","Swimming Pool","Air Conditioning","Free Parking","Kitchen","Washer","TV","Beach Access","BBQ Grill"])},
        "owner": "sarah.j@email.com",
        "reviews": [
            {"email": "m.rashid@email.com", "text": "Absolutely stunning villa! The ocean view is breathtaking and the pool was perfect. Would definitely book again.", "rating": 5},
            {"email": "emily.c@email.com",  "text": "Amazing location right on the beach. The kitchen was well-stocked and the space was immaculately clean.", "rating": 5},
            {"email": "carlos.g@email.com", "text": "Great place but a bit pricey. The beach access was incredible and the pool was lovely.", "rating": 4},
        ]
    },
    {
        "place": {"title": "Cozy Mountain Cabin - Swiss Alps", "description": "Charming wooden cabin in the Swiss Alps at 1,800m altitude. Wake up to panoramic mountain views, enjoy the crackling fireplace. Perfect ski-in/ski-out access in winter, hiking trails in summer.", "price": 185.0, "latitude": 46.5197, "longitude": 7.9009, "amenities": get_amenity_ids(["WiFi","Air Conditioning","Free Parking","Kitchen","Washer","TV","Workspace"])},
        "owner": "m.rashid@email.com",
        "reviews": [
            {"email": "sarah.j@email.com", "text": "A magical mountain retreat! The fireplace, the views, the peace and quiet — everything was perfect.", "rating": 5},
            {"email": "aisha.n@email.com",  "text": "We stayed for a week and didn't want to leave. Warm, cozy and the host was very helpful.", "rating": 5},
        ]
    },
    {
        "place": {"title": "Modern City Apartment - Paris", "description": "Sleek 2-bedroom apartment in the heart of Paris, 5 minutes from the Eiffel Tower. Floor-to-ceiling windows, designer furniture, fully equipped kitchen. Experience the City of Light like a local.", "price": 220.0, "latitude": 48.8566, "longitude": 2.3522, "amenities": get_amenity_ids(["WiFi","Air Conditioning","Kitchen","Washer","TV","Workspace"])},
        "owner": "emily.c@email.com",
        "reviews": [
            {"email": "sarah.j@email.com",  "text": "Perfect Paris apartment! Location was unbeatable, the apartment itself was gorgeous. Highly recommended!", "rating": 5},
            {"email": "m.rashid@email.com", "text": "Beautiful apartment in a great central location. Very clean and exactly as described.", "rating": 4},
            {"email": "carlos.g@email.com", "text": "Great location, nice apartment. The Eiffel Tower view was just magical.", "rating": 5},
        ]
    },
    {
        "place": {"title": "Historic Castle Suite - Edinburgh", "description": "Stay in a converted 16th-century castle on the outskirts of Edinburgh. Stone walls, vaulted ceilings, original period features. Private grounds with gardens and stunning Highland views.", "price": 290.0, "latitude": 55.9533, "longitude": -3.1883, "amenities": get_amenity_ids(["WiFi","Free Parking","Kitchen","TV"])},
        "owner": "emily.c@email.com",
        "reviews": [
            {"email": "sarah.j@email.com",  "text": "A once-in-a-lifetime experience! Staying in a real castle was magical. The rooms are stunning and grounds are beautiful.", "rating": 5},
            {"email": "carlos.g@email.com", "text": "Absolutely incredible property. The castle is authentic and full of history. Will definitely return.", "rating": 5},
        ]
    },
]

for pc in places_config:
    owner_email = pc["owner"]
    owner_headers = tok(owner_email)

    r = requests.post(f"{BASE}/places/", json=pc["place"], headers=admin_headers)
    if r.status_code == 201:
        place_id = r.json()["id"]
        print(f"✅ Place: {pc['place']['title'][:45]}...")
        # Add reviews
        for rv in pc["reviews"]:
            rv_headers = tok(rv["email"])
            rv_data = {"place_id": place_id, "text": rv["text"], "comment": rv["text"], "rating": rv["rating"]}
            rr = requests.post(f"{BASE}/reviews/", json=rv_data, headers=rv_headers)
            if rr.status_code == 201:
                print(f"   ⭐ Review by {rv['email'].split('@')[0]}: {rv['rating']}/5")
            else:
                print(f"   ⚠️  Review failed ({rv['email']}): {rr.status_code} {rr.text[:80]}")
    else:
        print(f"⚠️  Place failed: {pc['place']['title'][:45]}: {r.status_code} {r.text[:100]}")

# ------------------------------------------------------------------
# 5. ملخص نهائي
# ------------------------------------------------------------------
step("✅ ملخص نهائي")
places_r = requests.get(f"{BASE}/places/")
amenities_r = requests.get(f"{BASE}/amenities")
places_count = len(places_r.json()) if places_r.ok else "?"
amenities_count = len(amenities_r.json()) if amenities_r.ok else "?"

print(f"🏠 الأماكن:          {places_count}")
print(f"🛎️  وسائل الراحة:     {amenities_count}")
print(f"\n🔑 بيانات الدخول:")
print(f"   Admin:  admin@hbnb.io / Admin1234!")
print(f"   User:   sarah.j@email.com / Pass1234!")
