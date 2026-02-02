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

%% العلاقات (UML Relationships)

User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes
Place "1" --> "0..*" Review : has
Place "0..*" o-- "0..*" Amenity : includes

```
