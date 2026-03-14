# HBnB Project — Part 3  
  Enhanced Backend with Authentication and Database Integration
## 1. Project Overview

HBnB Evolution is a backend system inspired by the concept of Airbnb. The project is developed incrementally across multiple parts.
Part 3 focuses on implementing the API Layer, which exposes the application functionality through RESTful endpoints.

The API allows external clients (such as frontend applications, mobile apps, or testing tools) to interact with the backend system. It receives HTTP requests, processes them through the business logic layer, and returns structured JSON responses.

This part of the project demonstrates how to design and implement a clean RESTful API architecture using Python and Flask while maintaining modularity and separation of concerns.

## 2. Objectives of Part 3

The primary goals of this stage are:

- Implement a RESTful API using Flask
- Connect API routes with the business logic layer
- Enable CRUD operations for the system entities
- Validate incoming client data
- Return appropriate HTTP status codes
- Ensure responses follow a consistent JSON structure
- Maintain modular and maintainable project architecture

## 3. System Architecture

The HBnB backend follows a three-layer architecture:

Client │ ▼ API Layer │ ▼ Business Logic Layer │ ▼ Persistence Layer











This repository contains **Part 3** of the HBnB project, where the backend evolves from a basic in-memory application into a **secure, authenticated, and database-backed API** using **Flask**, **JWT**, **SQLAlchemy**, and **SQLite**.

In this phase, the application introduces:

- **JWT-based authentication**
- **Role-based access control**
- **Persistent storage with SQLAlchemy**
- **Secure password hashing with Bcrypt**
- **Relational database design**
- **Entity mapping and relationships**
- **Database initialization scripts**
- **ER diagram documentation**

The goal of this part is to prepare the backend for a more realistic production-style architecture by replacing temporary in-memory storage with a structured relational database layer while preserving clean code organization through the repository and facade patterns.

---

# Table of Contents

1. [Project Overview](#project-overview)
2. [Main Objectives](#main-objectives)
3. [Features Implemented](#features-implemented)
4. [Project Architecture](#project-architecture)
5. [Authentication and Authorization](#authentication-and-authorization)
6. [Database Integration](#database-integration)
7. [Entities and Relationships](#entities-and-relationships)
8. [API Endpoints](#api-endpoints)
9. [Configuration](#configuration)
10. [How to Run the Project](#how-to-run-the-project)
11. [How to Test the Project](#how-to-test-the-project)
12. [Database Files](#database-files)
13. [ER Diagram](#er-diagram)
14. [Technologies Used](#technologies-used)
15. [Author](#author)

---

# Project Overview

In previous parts of the HBnB project, application data was stored in memory. While this approach is useful during the early development phase, it is not suitable for real-world applications because data is lost whenever the server stops.

In **Part 3**, the application is upgraded to support:

- persistent data storage using **SQLite**
- data modeling using **SQLAlchemy ORM**
- secure login using **JWT**
- role-based permissions for users and administrators
- ownership checks for protected resources
- clear relationships between core entities such as users, places, reviews, and amenities

This part transforms the backend into a more scalable and realistic web application architecture.

---

# Main Objectives

The main objectives of Part 3 are:

- Implement **JWT authentication** to secure the API
- Add **authorization rules** for regular users and administrators
- Replace the **in-memory repository** with **SQLAlchemy-based persistence**
- Store user passwords securely using **Bcrypt hashing**
- Map the application entities to relational database tables
- Define relationships between entities
- Provide SQL scripts for schema creation and initial data
- Document the database structure using **Mermaid ER diagrams**

---

# Features Implemented

## 1. Application Factory with Configuration
The Flask application uses the **Application Factory pattern** so that configuration can be injected cleanly.

The application supports loading configuration through:

## Authors

Rabea Thabit
Hamsa  Alammar
Solaf  Alessa

```python
create_app(config_class="config.DevelopmentConfig")
