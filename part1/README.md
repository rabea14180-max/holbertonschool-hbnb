# HBnB Evolution - Part 1

**HBnB Evolution** is a simplified AirBnB-like application.  
It allows users to register, manage places, associate amenities, and submit reviews.

This README provides a **detailed overview** of the project architecture, entities, relationships, and API workflows.

---

## 1. Project Overview

HBnB Evolution mimics a basic vacation rental platform with features:

- User registration and management  
- Place creation and management  
- Amenities association (WiFi, Pool, Parking, etc.)  
- Review submission system  
- Clear layered architecture using Facade Pattern

**Goal:** Maintainable, modular, and extensible system.

---

## 2. Architecture

### 2.1 Layers

| Layer | Responsibility |
|-------|----------------|
| **Presentation Layer (API)** | Handles requests, input validation, and responses |
| **Business Logic Layer** | Core application logic, contains main entities (User, Place, Review, Amenity) |
| **Persistence Layer** | Stores and retrieves data; accessed only through Business Logic Layer |

**Communication Flow:**  
User → API → Facade → Business Logic → Persistence → Response

---

### 2.2 High-Level Package Diagram

![High-Level Package Diagram](./packeg.png)

**Explanation:**

- API → Facade → Business Logic → Persistence → Back  
- Ensures separation of concerns and avoids direct database access from API

---

## 3. Business Logic Layer

### 3.1 Core Entities

| Entity | Description |
|--------|-------------|
| **User** | Represents system users |
| **Place** | Represents properties listed by users |
| **Review** | Feedback and ratings for Places |
| **Amenity** | Features linked to Places (WiFi, Pool, Parking, etc.) |

All entities include `id`, `created_at`, and `updated_at`.

---

### 3.2 Detailed Class Diagram

![Detailed Class Diagram](./class_diagram.png)

---

### 3.3 Entities Description

#### 3.3.1 User

| Field | Type | Description |
|-------|------|------------|
| id | string | Unique identifier |
| first_name | string | User's first name |
| last_name | string | User's last name |
| email | string | User email for login |
| password | string | Hashed password |
| is_admin | boolean | Administrator flag |
| created_at | datetime | Creation timestamp |
| updated_at | datetime | Last updated timestamp |

**Responsibilities:**  
- Register and update profile  
- Own multiple Places  
- Write multiple Reviews  

---

#### 3.3.2 Place

| Field | Type | Description |
|-------|------|------------|
| id | string | Unique identifier |
| title | string | Property title |
| description | string | Property description |
| price | float | Rental price |
| latitude | float | GPS latitude |
| longitude | float | GPS longitude |
| owner_id | string | Reference to User |
| created_at | datetime | Creation timestamp |
| updated_at | datetime | Last updated timestamp |

**Responsibilities:**  
- Create and manage properties  
- Store location and pricing info  
- Associate Amenities  

---

#### 3.3.3 Review

| Field | Type | Description |
|-------|------|------------|
| id | string | Unique identifier |
| rating | int | Rating value (1-5) |
| comment | string | Feedback text |
| place_id | string | Reference to Place |
| user_id | string | Reference to User |
| created_at | datetime | Creation timestamp |
| updated_at | datetime | Last updated timestamp |

**Responsibilities:**  
- Submit feedback linked to User and Place  

---

#### 3.3.4 Amenity

| Field | Type | Description |
|-------|------|------------|
| id | string | Unique identifier |
| name | string | Feature name |
| description | string | Feature description |
| created_at | datetime | Creation timestamp |
| updated_at | datetime | Last updated timestamp |

**Responsibilities:**  
- Provide additional features  
- Link to multiple Places (Many-to-Many)  

---

### 3.4 Relationships

| Relationship | Type |
|-------------|------|
| User → Places | One-to-Many |
| User → Reviews | One-to-Many |
| Place → Reviews | One-to-Many |
| Place → Amenities | Many-to-Many |

---

## 4. API Workflows (Sequence Diagrams)

### 4.1 User Registration

![User Registration Sequence Diagram](./user_registration.png)

**Steps Table:**

| Step | Action |
|------|-------|
| 1 | User sends registration request to API |
| 2 | API forwards request to Facade |
| 3 | Business Logic validates user data |
| 4 | System checks email uniqueness |
| 5 | New User object created |
| 6 | Persistence Layer saves user |
| 7 | Success response returned |

---

### 4.2 Place Creation

![Place Creation Sequence Diagram](./place_creation.png)

| Step | Action |
|------|-------|
| 1 | Owner requests new Place creation |
| 2 | API → Facade → Business Logic |
| 3 | Owner validated |
| 4 | Place data validated |
| 5 | New Place object created |
| 6 | Persistence Layer saves Place |
| 7 | Success response returned |

---

### 4.3 Review Submission

![Review Submission Sequence Diagram](./review_submission.png)

| Step | Action |
|------|-------|
| 1 | User submits review |
| 2 | API → Facade → Business Logic |
| 3 | Validate User and Place |
| 4 | Validate rating value |
| 5 | Create Review object |
| 6 | Persistence Layer saves review |
| 7 | Success response returned |

---

### 4.4 Fetch Places

![Fetch Places Sequence Diagram](./fetch_places.png)

| Step | Action |
|------|-------|
| 1 | User requests Places list |
| 2 | API → Facade → Business Logic → Persistence |
| 3 | Retrieve all stored Places |
| 4 | Return list (or empty) |
| 5 | API returns response |

---

## 5. Conclusion

This README provides:

- Full layered architecture explanation  
- Core entities with detailed fields & responsibilities  
- Relationships & API workflows  
- Diagrams embedded directly as images

This file is **ready to be used on GitHub**, showing all images and tables clearly.

````
👩‍💻 Author : Hamsa Alammar , Rabea Younis Thabit , Solaf Alessa
