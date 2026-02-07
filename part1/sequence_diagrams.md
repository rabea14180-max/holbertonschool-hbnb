# TASK 2 — Sequence Diagrams for API Calls

This section presents sequence diagrams illustrating the interaction flow between the **Presentation Layer (API)**, **Business Logic Layer**, and **Persistence Layer (Database)** for the main API use cases of the HBnB Evolution application.

---

## 2.1 User Registration — POST /users

### Description
This API call handles the registration of a new user. The system receives user email and password, validates the input, and persists the user information in the database.

### Flow Summary
- The client sends a registration request to the API.  
- The API forwards the request to the Business Logic Layer for processing.  
- The Business Logic Layer interacts with the Database to save the user.  
- Appropriate HTTP responses are returned depending on success or failure.

### Sequence Diagram
```mermaid
sequenceDiagram
    actor user
    participant API
    participant BusinessLogic
    participant DataBase
    
    user->>API: register(email,password)
    API->>BusinessLogic: process registration request
    BusinessLogic->>DataBase: save data
    alt Registration success
        DataBase-->>BusinessLogic: user saved
        BusinessLogic-->>API: registration success 
        API-->>user: 201 Created (account created)
    else Registration failed 
        DataBase-->>BusinessLogic: Email found
        BusinessLogic-->>API: registration failed
        API-->>user: 409 Conflict (email already exists)
    end
