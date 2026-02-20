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

# HBnB – Part 2
## Business Logic & REST API Implementation
## 📖 Overview

This phase translates the architectural design of HBnB into a working backend system.
The focus is on implementing a clean, modular, and scalable backend using Flask, structured around clear separation of concerns and layered architecture.

The system is built to be extensible, maintainable, and ready for database integration in the next phase.

## 🏗 Architectural Design

The application follows a layered architecture:

## 1️⃣ Presentation Layer

Responsible for exposing RESTful endpoints using Flask + flask-restx.
This layer:

- Defines API routes and namespaces
- Handles request parsing and validation
- Serializes responses
- Documents endpoints using Swagger

## 2️⃣ Business Logic Layer

Encapsulates the core domain models and application rules.

Implemented entities:

- User
- Place
- Review
- Amenity

This layer:

- Manages relationships between entities
- Handles domain-level validation
- Controls object lifecycle and interactions
- Remains independent from the web framework

## 3️⃣ Persistence Layer (Abstraction-Ready)

Although database integration is postponed to Part 3, the system is designed with persistence abstraction in mind.

- An in-memory repository is implemented.
- The architecture allows seamless replacement with a database-backed repository (e.g., SQLAlchemy).
- Business logic remains decoupled from storage implementation.

## 🎯 Design Principles Applied

- Separation of Concerns
- Single Responsibility Principle
- Facade Pattern to simplify communication between Presentation and Business Logic layers
- Clean modular project structure
- Scalable API design
- Extensibility for authentication (JWT) and RBAC in future phases

## 🚀 Implemented Features

- Structured Flask application with modular packaging
- RESTful CRUD endpoints for:
   - Users
   - Places
   - Reviews
   - Amenities
- Entity relationship handling
- Nested/extended serialization (e.g., Place returns owner details and amenities)
- Swagger API documentation via flask-restx
- Edge-case handling and endpoint validation

  ## 🛠 Tech Stack

  - Python 3
  - Flask
  - flask-restx
  - In-Memory Repository Pattern
  - Facade Design Pattern
 
    ## 🔮 Forward Compatibility

    The system is intentionally architected to support:

    - SQLAlchemy integration (Part 3)
    - JWT authentication
    - Role-based access control
    - Production-ready scalability
   
      
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

