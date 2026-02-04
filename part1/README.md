# HBnB Evolution - Part 1

**HBnB Evolution** is a simplified AirBnB-like application.  
It allows users to register, manage places, associate amenities, and submit reviews.

This README provides a detailed explanation of the project structure, entities, relationships, and API workflows.

---

## 1. Project Overview

HBnB Evolution mimics a basic vacation rental platform with the following features:

- User registration and management
- Place creation and management
- Amenities association (WiFi, Pool, Parking, etc.)
- Review submission system
- Clear layered architecture with Facade Pattern

The architecture ensures maintainability, modularity, and easy extension.

---

## 2. Architecture

### 2.1 Layers

The system follows a layered architecture:

1. **Presentation Layer (API Layer)**  
   - Handles user requests and responses  
   - Validates input data  

2. **Business Logic Layer**  
   - Core application logic  
   - Contains main entities: User, Place, Review, Amenity  

3. **Persistence Layer (Database Layer)**  
   - Stores and retrieves data  
   - Interacts only with Business Logic Layer  

**Communication Flow:**  
User → API → Facade → Business Logic → Persistence → Response

---

### 2.2 High-Level Package Diagram

![High-Level Package Diagram](./packeg.png)

**Explanation:**

- API sends requests to the Facade  
- Facade calls Business Logic  
- Business Logic interacts with Persistence Layer  
- Data flows back through the same path  

---

## 3. Business Logic Layer

### 3.1 Core Entities

The system has four main entities:

1. **User** – Registered users  
2. **Place** – Properties listed by users  
3. **Review** – Feedback and ratings for places  
4. **Amenity** – Features that can be attached to places  

All entities include:

- `id` (unique identifier)  
- `created_at` & `updated_at` (audit fields)

---

### 3.2 Detailed Class Diagram

![Detailed Class Diagram](./class_diagram.png)

**Explanation:**

- One **User** can own multiple **Places** (One-to-Many)  
- One **User** can write multiple **Reviews** (One-to-Many)  
- One **Place** can have multiple **Reviews** (One-to-Many)  
- **Places** and **Amenities** are linked in a Many-to-Many relationship

---

### 3.3 Entities Description

#### User

**Attributes:** `id`, `first_name`, `last_name`, `email`, `password`, `is_admin`, `created_at`, `updated_at`  
**Responsibilities:** Register, update profile, own Places, write Reviews  

#### Place

**Attributes:** `id`, `title`, `description`, `price`, `latitude`, `longitude`, `owner_id`, `created_at`, `updated_at`  
**Responsibilities:** Create/manage properties, associate amenities, have reviews  

#### Review

**Attributes:** `id`, `rating`, `comment`, `place_id`, `user_id`, `created_at`, `updated_at`  
**Responsibilities:** Submit feedback, link to user and place  

#### Amenity

**Attributes:** `id`, `name`, `description`, `created_at`, `updated_at`  
**Responsibilities:** Provide additional features, link to multiple places  

---

## 4. API Interaction Flow

### 4.1 User Registration

![User Registration Sequence Diagram](./user_registration.png)

**Flow:**

1. User sends registration request  
2. API forwards to Facade  
3. Business logic validates data  
4. Email uniqueness check  
5. New User object is created  
6. Persistence Layer saves the user  
7. Success response returned  

---

### 4.2 Place Creation

![Place Creation Sequence Diagram](./place_creation.png)

**Flow:**

1. Owner requests place creation  
2. API → Facade → Business Logic  
3. Owner existence validated  
4. Place data validated  
5. New Place object created  
6. Persistence Layer saves Place  
7. Success response returned  

---

### 4.3 Review Submission

![Review Submission Sequence Diagram](./review_submission.png)

**Flow:**

1. User submits review  
2. API → Facade → Business Logic  
3. User & Place existence validated  
4. Rating validated  
5. New Review object created  
6. Persistence Layer saves review  
7. Success response returned  

---

### 4.4 Fetch Places

![Fetch Places Sequence Diagram](./fetch_places.png)

**Flow:**

1. User requests places list  
2. API → Facade → Business Logic → Persistence Layer  
3. All stored places retrieved  
4. Response returned (list or empty)  

---

## 5. Conclusion

This part of HBnB Evolution defines:

- Layered architecture  
- Core entities and their relationships  
- Main API workflows with sequence diagrams  

All diagrams are included as images and appear directly in this README.

👩‍💻 Author : 
Hamsa Alammar ,  Rabea Younis Thabit ، Solaf Alessa
