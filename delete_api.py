import requests
import sys

API_BASE = 'http://127.0.0.1:5000/api/v1'

def delete_places():
    try:
        # 1. Login
        login_data = {"email": "admin@hbnb.io", "password": "Admin1234!"}
        res = requests.post(f"{API_BASE}/users/login", json=login_data, timeout=10)
        if res.status_code != 200:
            print(f"Login failed: {res.status_code} - {res.text}")
            return
        
        token = res.json().get('access_token')
        headers = {"Authorization": f"Bearer {token}"}
        
        # 2. Delete
        pids = [
            "98762929-ebb5-435d-9a9d-b68a918b219a", # Dubai
            "ebe0eb86-195f-45e0-a20e-59333da08c08"  # Marrakech
        ]
        
        for pid in pids:
            print(f"Deleting {pid}...")
            # Try both /places/<id> and /places/<id>/
            d_res = requests.delete(f"{API_BASE}/places/{pid}", headers=headers, timeout=10)
            print(f"Result for {pid}: {d_res.status_code} - {d_res.text}")
            
    except Exception as e:
        print(f"ERROR: {str(e)}")

if __name__ == "__main__":
    delete_places()
