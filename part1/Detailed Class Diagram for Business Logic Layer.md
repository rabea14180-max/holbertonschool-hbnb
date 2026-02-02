 ```mermaid 
classDiagram
direction LR

class User {
  -id: UUID
  +first_name: String
  +last_name: String
  +email: String
  -password: String
  +is_admin: Boolean
  +register(): void
  +updateProfile(): void
  +delete(): void
}

class Admin {
  +createUser(): void
  +deleteUser(): void
  +managePlaces(): void
  +manageReviews(): void
  +manageAmenities(): void
}

class Place {
  +title: String
  +description: String
  +price: Float
  +latitude: Float
  +longitude: Float
  +create(): void
  +update(): void
  +delete(): void
  +list(): List~Place~
}

class Review {
  +rating: Integer
  +comment: String
  +create(): void
  +update(): void
  +delete(): void
  +list(): List~Review~
}

class Amenity {
  +name: String
  +description: String
  +create(): void
  +update(): void
  +delete(): void
  +list(): List~Amenity~
}

%% Inheritance (Admin is a User)
User <|-- Admin

%% العلاقات الأساسية
User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes
Place "1" --> "0..*" Review : has
Place "0..*" o-- "0..*" Amenity : includes

%% علاقات الأدمن (إدارية)
Admin --> Place : manages
Admin --> Review : moderates
Admin --> Amenity : manages
Admin --> User : manages
```
