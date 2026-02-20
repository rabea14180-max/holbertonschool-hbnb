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

## HBnB Project — Part 2 (Places & Reviews)

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
---
Author: Solaf Alessa
## HBnB Project — Part 2 (Project Setup & User Endpoints)

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

### Author

Rabea Thabit
