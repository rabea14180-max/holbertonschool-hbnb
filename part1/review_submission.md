```mermaid
sequenceDiagram
        actor user
        participant API
        participant BusinessLogic
        participant DataBase

        user->>API: submit_Review(Rating, comment)
        API->>BusinessLogic: send review 
        BusinessLogic->>DataBase: save review 
        alt submission succesed 
        DataBase-->>BusinessLogic: review saved
        BusinessLogic-->>API: submission success
        API-->>user: review submitted 
        else invalid data 
        BusinessLogic-->>API: validation failed
        API-->>user: Review submission failed(invalid data)
        end
