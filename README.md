# HBnB Evolution 

**HBnB Evolution** is a simplified AirBnB-like application that allows users to register, manage places, associate amenities, and submit reviews.

## 📝 Project Overview

This project is designed to mimic a basic vacation rental platform with the following features:

- User registration and authentication
- Property management (places)
- Amenities association (WiFi, Pool, Parking, etc.)
- Review system for users to rate places
- Clear separation of concerns with a layered architecture:
  - Presentation Layer (API)
  - Business Logic Layer
  - Persistence Layer (Database)

The project uses a **Facade Pattern** to simplify communication between the API and the business logic layer.

---

## 🏗 Architecture Overview

- **Presentation Layer (API Layer):** Handles user requests and responses.
- **Business Logic Layer:** Core application logic and entities (User, Place, Review, Amenity).
- **Persistence Layer:** Responsible for storing and retrieving data from the database.

High-level interactions:

User → API → Facade → Business Logic → Persistence → Response


---

## ⚡ Features

- Register, login, and manage users
- Create, edit, and delete places
- Associate multiple amenities with each place
- Submit and view reviews for places
- Retrieve a list of available places

---

## 🖼 Screenshots / Diagrams

High-level architecture and sequence diagrams are included in the [Technical Documentation](https://github.com/rabea14180-max/holbertonschool-hbnb/blob/main/part1/TECHNICAL_DOCUMENT.md) file.

---

👩‍💻 Authors 
This project was created by Holberton School students:
- Hamsa Alammar
- Rabea Younis Thabit
- Solaf Alessa

🎓 Academic Context
 - School: Holberton School Saudi Arabia
 - Program: Advanced Backend Specialization
 - Project: HBnB Evolution — Part 1 (Technical Documentation)
 - Date: February 2026

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

