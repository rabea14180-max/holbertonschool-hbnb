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

High-level architecture and sequence diagrams are included in the [Technical Documentation](./TECHNICAL_DOCUMENT.md) file.

---

## 💻 Getting Started

1. Clone the repository:
```bash
git clone <your-repo-url>

2 - Navigate to the project folder:
cd HBnB-Evolution
3 - Explore the TECHNICAL_DOCUMENT.md for architecture and sequence diagrams.

📚 Technologies
. Python 3.x
. Object-Oriented Programming (OOP)
. Markdown documentation for diagrams and architecture
. Git & GitHub for version control
```
👩‍💻 Author :
Hamsa Alammar
Rabea Younis Thabit
Solaf Alessa
