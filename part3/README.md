# HBnB Project — Part 2 (Project Setup & User Endpoints) 

This repository contains the HBnB project work focusing on:

- **Task 0** — Project Setup and Package Initialization  
- **Task 2** — User API Endpoints  

---

## Project Overview

- **Project Setup (Task 0)**
  - The project is organized using a modular layered architecture.
  - The application structure includes:
    - `api/` — Presentation Layer (handles HTTP requests and API endpoints)
    - `models/` & `services/` — Business Logic Layer
    - `persistence/` — In-memory repository implementation
  - Implements the **Facade Pattern** in `services/facade.py`.
  - Communication flow:
    - `API → Facade → Repository`
  - No database is used in this phase.
  - Designed to be replaced with SQLAlchemy in Part 3.

---

- **User Management — API Endpoints (Task 2)**
  - `models/user.py` defines the `User` class.
  - Handles attributes:
    - `first_name`
    - `last_name`
    - `email`
    - `password`
    - `is_admin`
  - Includes validation and profile update logic.
  - Password is excluded from API responses.

  - `api/v1/users.py` exposes REST API endpoints:
    - `POST /api/v1/users` — Create a new user
    - `GET /api/v1/users` — Retrieve all users
    - `GET /api/v1/users/<id>` — Retrieve single user
    - `PUT /api/v1/users/<id>` — Update user

> DELETE operation is not implemented for Task 2 as per project requirements.

---
## Architecture

- `models/` → Business logic classes  
- `persistence/` → In-memory repository implementation  
- `services/facade.py` → Application service layer (handles validation and coordination)  

Data storage is handled using:

```bash
# In-memory repository (no database in this phase)
```

---

Author: Rabea Thabit


# HBnB Project — Part 2 (Tasks 1 & 3) 

This repository contains the HBnB project work focusing on:

- **Task 1** — Core Business Logic for Users  
- **Task 3** — Amenity API Endpoints

---

## Project Overview

- **User Management (Task 1)**
  - `models/user.py` defines the User class.
  - Handles attributes: `first_name`, `last_name`, `email`, `password`, `is_admin`.
  - Includes validation, profile update, and registration logic.

- **Amenity Management (Task 3)**
  - `models/amenity.py` defines the Amenity class.
  - `services/facade.py` handles CRUD operations for amenities.
  - `api/v1/amenities.py` exposes REST API endpoints:
    - `GET /amenities` — List all amenities
    - `GET /amenities/<id>` — Get single amenity
    - `POST /amenities` — Create a new amenity
    - `PUT /amenities/<id>` — Update an amenity

> DELETE operation is not implemented for Task 3 as per project requirements.

---

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt

```

Author : Hamsa Alammar

# HBnB Project — Part 2 (Places & Reviews)

This repository contains the HBnB project work focusing on:
- Task 4: Place Endpoints
- Task 5: Review Endpoints
---
Project Overview

- **Place Management (Task 4)**
  - `models/place.py` defines the `Place` class.
  - Handles attributes:
    - `title`
    - `description`
    - `price`
    - `latitude`
    - `longitude`
    - `owner_id`
    - `amenities`
    - `reviews`

  - Includes validation logic for:
  - Price (non-negative)
  -  Latitude (-90 to 90)
  -  Longitude (-180 to 180)
- Managed through` services/facade.py`.
---
- **Review Management (Task 5)**
  - `models/review.py` defines the `Review `class.
  - Handles attributes:
    - `text`
    - `rating`
    -` user_id`
    -` place_id`
  - Includes validation:
    - Rating must be between 1 and 5
    - Text must be non-empty
 - Reviews are linked to their corresponding places.

## Architecture

- models/ → Business logic classes
- persistence/ → In-memory repository implementation
- services/facade.py → Application service layer (handles validation and coordination)

Data storage is handled using:
```bash
InMemoryRepository
```
No database is used in this phase.

## Supported Operations
Places
- `create_place(data)`
- `get_place(place_id)`
- `get_all_places()`
- `update_place(place_id, data)`

Reviews
- `create_review(data)`
- `get_review(review_id)`
- `get_all_reviews()`
- `get_reviews_by_place(place_id)`
- `update_review(review_id, data)`
- `delete_review(review_id)`

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```
2. Run the application:
```bash
python3 run.py
```

Author: Solaf Alessa

---

# HBnB API Testeng and validation
providing a detailed overview of the API endpoints tested in the HBnB project, including Users, Amenities, Places, and Reviews

1. Users
Create a User (POST)

<img width="911" height="665" alt="Screenshot 2026-02-21 200404" src="https://github.com/user-attachments/assets/8005ef4a-70d8-4773-8096-45ee96fd2d34" />

---

<img width="910" height="624" alt="Screenshot 2026-02-21 202707" src="https://github.com/user-attachments/assets/f6bc24c8-449d-4d7c-9cf7-bad322bb2c8a" />

---

Update User (PUT)

<img width="909" height="632" alt="Screenshot 2026-02-21 202848" src="https://github.com/user-attachments/assets/451294f6-7adf-48ba-87d0-ae6e8cb940fd" />

---
2. Amenities
Create an Amenity (POST)

<img width="916" height="545" alt="Screenshot 2026-02-21 200438" src="https://github.com/user-attachments/assets/1d5bc125-0045-4027-82ee-49b1a056c51b" />

---
3. Places
Create a Place (POST)

<img width="920" height="683" alt="Screenshot 2026-02-21 200511" src="https://github.com/user-attachments/assets/ad5b49c9-58ce-4e35-b3a1-18fd7dad9acb" />

---

Update Place to Add Amenities (PUT)

<img width="914" height="445" alt="Screenshot 2026-02-21 200555" src="https://github.com/user-attachments/assets/67fad870-a498-4b81-b65c-21068f664910" />

---

Delete place (DELETE)

<img width="917" height="370" alt="Screenshot 2026-02-21 201406" src="https://github.com/user-attachments/assets/c5e3688c-5ef7-44c7-a3d7-735d3a062276" />

- it can't be deleted because it's not a requirement for the project 

---

4. Reviews
Create a Review (POST)

<img width="903" height="596" alt="Screenshot 2026-02-21 200653" src="https://github.com/user-attachments/assets/d19b96ed-a269-4a5a-a37a-acdd2cf4b2f0" />

---

Delete Review (DELETE)

<img width="869" height="351" alt="Screenshot 2026-02-21 201225" src="https://github.com/user-attachments/assets/ad26da4f-6c37-4c27-a647-cfa1f2745289" />

---

List places with Amenities & Reviews (GET)

<img width="905" height="907" alt="Screenshot 2026-02-21 200731" src="https://github.com/user-attachments/assets/2d6a3522-84bf-4982-b634-3fa5fa2746f1" />

---

**How it would be showen**
- Users "before update"

<img width="691" height="510" alt="Screenshot 2026-02-21 202818" src="https://github.com/user-attachments/assets/24099c76-4911-4c77-b4b9-209f9f5dde12" />

---

- Users "after update"

<img width="676" height="508" alt="Screenshot 2026-02-21 202909" src="https://github.com/user-attachments/assets/b3f16616-f377-4e17-8daa-6158d62868e3" />

---

- Places

<img width="690" height="680" alt="Screenshot 2026-02-21 200907" src="https://github.com/user-attachments/assets/dbda7e1d-9823-4aac-b683-a4771ec0e566" />

---

- Reviews

<img width="671" height="329" alt="Screenshot 2026-02-21 200948" src="https://github.com/user-attachments/assets/833444ea-1a54-4dcf-b3e3-b7ce0b8216f8" />

---

## Failed Operations

1. User Errors

Missing required fields

<img width="907" height="551" alt="Screenshot 2026-02-21 211338" src="https://github.com/user-attachments/assets/74b6161e-b599-4f02-96be-177b111b8d9b" />

---

Wrong ID

<img width="920" height="409" alt="Screenshot 2026-02-21 211411" src="https://github.com/user-attachments/assets/4587a2b2-2449-46e3-8c66-1ad7d04dbda8" />

---

2. Amenity Errors

Missing name

<img width="916" height="418" alt="Screenshot 2026-02-21 211432" src="https://github.com/user-attachments/assets/ab879a5b-67ec-429c-ae9f-77288e1e1976" />

---

Wrong ID 

<img width="917" height="360" alt="Screenshot 2026-02-21 211453" src="https://github.com/user-attachments/assets/2fcb6ca6-f2d1-431c-879d-e05652d2089c" />

---

3. Place Errors

Missing required field `owner_id`

<img width="916" height="396" alt="Screenshot 2026-02-21 211513" src="https://github.com/user-attachments/assets/5190f1da-d914-4bb5-b9e4-32ec1ae68e13" />

---

Wrong ID 

<img width="905" height="389" alt="Screenshot 2026-02-21 211527" src="https://github.com/user-attachments/assets/b8bdbd33-26e4-46e7-9596-e618ccd72bd8" />

---

4. Review Errors

Rating out of bounds

<img width="908" height="454" alt="Screenshot 2026-02-21 211550" src="https://github.com/user-attachments/assets/138ef8fe-f4b6-411b-b209-91559286cec5" />

---

Wrong ID

<img width="915" height="366" alt="Screenshot 2026-02-21 211605" src="https://github.com/user-attachments/assets/dba3862d-fc50-4a16-8258-729d0a198b4d" />

---

- `DELETE` concerned an Error in  (`Users` , `Amenities` , `Places`) but not in `Reviews`

---
## Notes:
- `DELETE` is not implemented in (`Users` , `Amenities` , `Places`) as it's not required in the project but only in `Reviews`
- All `POST` and `PUT` operations have been successfully tested with curl
- `GET` operations can be tested by fetching entities using their IDs
- No authentication or authorization implemented yet
