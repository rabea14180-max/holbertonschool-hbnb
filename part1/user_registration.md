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
        API-->>user: account created 
        else Registration failed 
        DataBase-->>BusinessLogic: Email found
        BusinessLogic-->>API: registration failed
        API-->>user: creation failed(email already exists)
        end
