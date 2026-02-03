```mermaid
sequenceDiagram
        actor user
        participant API
        participant BusinessLogic
        participant DataBase
        
        user->>API: register(email,password)
        API->>BusinessLogic: send registration request
        BusinessLogic->>DataBase: save data
        alt Successed registration 
        DataBase-->>BusinessLogic: Confirm Save
        BusinessLogic-->>API: registration success 
        API-->>user: account created 
        else failed registration 
        DataBase-->>BusinessLogic: Email exists
        BusinessLogic-->>API: registration failed
        API-->>user: failed creation 
        end
