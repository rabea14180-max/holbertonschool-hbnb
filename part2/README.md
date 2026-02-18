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
