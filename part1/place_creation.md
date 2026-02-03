```mermaid
sequenceDiagram
        actor user
        participant API
        participant BusinessLogic
        participant DataBase

        user-->>API: create_Place(title, description, price, lat, long)
        API->>BusinessLogic: send creation request
        BusinessLogic->>DataBase: save place
        alt Creation success
        DataBase-->>BusinessLogic: place saved
        BusinessLogic-->>API: successed creation 
        API-->>user: place created
        else Creation failed
        DataBase-->>BusinessLogic: error saving
        BusinessLogic-->>API: failed creation
        API-->>user: could not create place
        end
