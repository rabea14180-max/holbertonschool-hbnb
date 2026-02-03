```mermaid
sequenceDiagram
        actor user
        participant API
        participant BusinessLogic
        participant DataBase

        user->>API: get_place(criteria)
        API->>BusinessLogic: process request
        BusinessLogic->>DataBase: fetch list of places
        alt list exists 
        DataBase-->>BusinessLogic: list exists
        BusinessLogic-->>API: return list
        API-->>user: list of places
        else Empty list
        DataBase-->>BusinessLogic: Empty list
        BusinessLogic-->>API: return empty list
        API-->>user: no places found
        else list does not exist 
        DataBase-->>BusinessLogic: no list found
        BusinessLogic-->>API: fetch failed 
        API-->>user: list does not exist 
        end
