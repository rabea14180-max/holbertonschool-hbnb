```mermaid
sequenceDiagram
        actor user
        participant API
        participant BusinessLogic
        participant DataBase

        user->>API: submit_Review()
        API->>BusinessLogic: send review 
        BusinessLogic->>DataBase: save review 

        DataBase-->>BusinessLogic: review saved
        BusinessLogic-->>API: successed submission
        API-->>user: review submitted 
