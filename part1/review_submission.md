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
        BusinessLogic-->>API: successed submission
        API-->>user: review submitted 
        else invalid data 
        DataBase-->>BusinessLogic: failed saving
        BusinessLogic-->>API: validation failed
        API-->>user: Review submission failed(invalid data)
        end
