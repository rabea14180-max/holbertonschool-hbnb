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
        API-->>user: 201 Created (review submitted)
        else invalid data 
        BusinessLogic-->>API: validation failed
        API-->>user: 400 Bad Request (invalid data)
        end
