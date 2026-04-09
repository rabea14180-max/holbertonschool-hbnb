import requests

API_BASE = 'http://127.0.0.1:5000/api/v1'

def delete_places():
    # 1. Login to get Admin token
    login_data = {"email": "admin@hbnb.io", "password": "Admin1234!"}
    res = requests.post(f"{API_BASE}/users/login", json=login_data)
    if res.status_code != 200:
        print(f"Login failed: {res.text}")
        return
    
    token = res.json().get('access_token')
    headers = {"Authorization": f"Bearer {token}"}
    
    # 2. Places to delete
    places_to_delete = {
        "98762929-ebb5-435d-9a9d-b68a918b219a": "Dubai Villa",
        "ebe0eb86-195f-45e0-a20e-59333da08c08": "Marrakech Riad"
    }
    
    for pid, name in places_to_delete.items():
        print(f"Deleting {name} ({pid})...")
        d_res = requests.delete(f"{API_BASE}/places/{pid}", headers=headers)
        if d_res.status_code in [200, 204]:
            print(f"Successfully deleted {name}.")
        else:
            print(f"Failed to delete {name}: {d_res.status_code} - {d_res.text}")

if __name__ == "__main__":
    delete_places()
