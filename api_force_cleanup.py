import requests
import json
import os

API_BASE = 'http://127.0.0.1:5000/api/v1'
LOG_FILE = r'c:\Users\REBEA\holbertonschool-hbnb\part4\base_files\api_delete_log.txt'

def force_delete():
    logs = []
    logs.append("Starting Force Delete via API...")
    
    try:
        # 1. Login
        logs.append("Logging in...")
        login_res = requests.post(f"{API_BASE}/users/login", json={"email": "admin@hbnb.io", "password": "Admin1234!"}, timeout=10)
        if login_res.status_code != 200:
            logs.append(f"FAILED LOGIN: {login_res.status_code} - {login_res.text}")
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                f.write("\n".join(logs))
            return
            
        token = login_res.json().get('access_token')
        headers = {"Authorization": f"Bearer {token}"}
        
        # 2. Get all places to find the 4 we want to KEEP
        logs.append("Fetching current places...")
        places_res = requests.get(f"{API_BASE}/places/", timeout=10)
        if not places_res.ok:
            logs.append("FAILED to fetch places")
            with open(LOG_FILE, 'w', encoding='utf-8') as f:
                f.write("\n".join(logs))
            return
            
        all_places = places_res.json()
        logs.append(f"Found {len(all_places)} places.")
        
        # Titles to KEEP
        keep_titles = [
            "Luxury Beachfront Villa - Miami",
            "Cozy Mountain Cabin - Swiss Alps",
            "Modern City Apartment - Paris",
            "Historic Castle Suite - Edinburgh"
        ]
        
        # 3. Delete everything ELSE
        for p in all_places:
            if p['title'] not in keep_titles:
                logs.append(f"Deleting {p['title']} ({p['id']})...")
                dr = requests.delete(f"{API_BASE}/places/{p['id']}", headers=headers, timeout=10)
                logs.append(f"   Result: {dr.status_code}")
            else:
                logs.append(f"KEEPING {p['title']}")
                
        logs.append("DONE.")
        
    except Exception as e:
        logs.append(f"CRITICAL ERROR: {e}")
        
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write("\n".join(logs))

if __name__ == "__main__":
    force_delete()
