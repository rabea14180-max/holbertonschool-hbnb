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
        DataBase-->>BusinessLogic: Confirm Save
        BusinessLogic-->>API: registration success 
        API-->>user: account created 
        else Registration failed 
        DataBase-->>BusinessLogic: Email exists
        BusinessLogic-->>API: registration failed
        API-->>user: failed creation(email already exists)
        end
