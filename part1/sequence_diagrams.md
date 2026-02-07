1- User Registration :
sequenceDiagram
    participant Client
    participant API as Presentation Layer
    participant Facade as HBnBFacade
    participant UserRepo as UserRepository
    participant DB as Database

    Client->>API: POST /users
    API->>Facade: registerUser(userData)
    Facade->>UserRepo: findByEmail(email)
    UserRepo->>DB: SELECT user
    DB-->>UserRepo: user or null

    alt Email already exists
        Facade-->>API: email conflict
        API-->>Client: 409 Conflict
    else Email available
        Facade->>Facade: hashPassword()
        Facade->>UserRepo: save(user)
        UserRepo->>DB: INSERT user
        DB-->>UserRepo: OK
        Facade-->>API: user created
        API-->>Client: 201 Created
    end


This sequence diagram illustrates how a new user account is created.

The client sends a registration request to the API (Presentation Layer).

The API forwards the request to the HBnBFacade (Business Logic Layer), which checks email uniqueness and hashes the password.

The facade uses UserRepository (Persistence Layer) to save the user in the database.

Success returns 201 Created; if the email exists, 409 Conflict is returned.
This shows clear separation of responsibilities across layers.

2- Place Creation :
sequenceDiagram
    participant Client
    participant API as Presentation Layer
    participant Facade as HBnBFacade
    participant PlaceRepo as PlaceRepository
    participant AmenityRepo as AmenityRepository
    participant DB as Database

    Client->>API: POST /places
    API->>Facade: createPlace(placeData)
    Facade->>Facade: validateOwner()
    Facade->>Facade: validatePlaceAttributes()

    alt Invalid data
        Facade-->>API: validation failed
        API-->>Client: 400 Bad Request
    else Valid data
        Facade->>PlaceRepo: save(place)
        PlaceRepo->>DB: INSERT place
        DB-->>PlaceRepo: OK
        Facade->>AmenityRepo: linkAmenities(place, amenities)
        AmenityRepo->>DB: INSERT relations
        DB-->>AmenityRepo: OK
        Facade-->>API: place created
        API-->>Client: 201 Created
    end

This diagram represents creating a new place listing:

Client submits data to the API, which passes it to HBnBFacade for validation.

The facade validates the owner and place attributes.

PlaceRepository persists the place; AmenityRepository links any amenities.

Success returns 201 Created; validation errors return 400 Bad Request.
It demonstrates business rule enforcement and persistence coordination.

3- Review Submission :
sequenceDiagram
    participant Client
    participant API as Presentation Layer
    participant Facade as HBnBFacade
    participant ReviewRepo as ReviewRepository
    participant DB as Database

    Client->>API: POST /places/{id}/reviews
    API->>Facade: createReview(reviewData)
    Facade->>Facade: validateUser()
    Facade->>Facade: validatePlace()
    Facade->>Facade: validateRating()

    alt Invalid review data
        Facade-->>API: validation failed
        API-->>Client: 400 Bad Request
    else Valid review
        Facade->>ReviewRepo: save(review)
        ReviewRepo->>DB: INSERT review
        DB-->>ReviewRepo: OK
        Facade-->>API: review created
        API-->>Client: 201 Created
    end

This diagram illustrates submitting a review:

Client sends the review request to the API.

HBnBFacade validates the user, place, and rating.

ReviewRepository persists the review in the database.

Success returns 201 Created; invalid data returns 400 Bad Request.
It ensures data integrity and proper handling of user-generated content.

4- Fetching a List of Places :
sequenceDiagram
    participant Client
    participant API as Presentation Layer
    participant Facade as HBnBFacade
    participant PlaceRepo as PlaceRepository
    participant DB as Database

    Client->>API: GET /places?filters
    API->>Facade: getPlaces(filters)
    Facade->>PlaceRepo: query(filters)
    PlaceRepo->>DB: SELECT places

    alt Query failure
        DB-->>PlaceRepo: error
        Facade-->>API: retrieval failed
        API-->>Client: 500 Internal Server Error
    else Success
        DB-->>PlaceRepo: results
        PlaceRepo-->>Facade: places list
        Facade-->>API: places
        API-->>Client: 200 OK
    end

This diagram shows retrieving a list of places:

Client sends a request with filters to the API.

HBnBFacade coordinates querying PlaceRepository.

Database returns results; API forwards to client.

Success returns 200 OK; database errors return 500 Internal Server Error.
It highlights clear separation of concerns across layers and proper handling of filtered data.
