 ```mermaid 
classDiagram
direction LR

class User {
  -id: UUID
  +first_name: String
  +last_name: String
  -email: String
  -password: String
  +is_admin: Bool
  +created_at: Date
  +updated_at: Date
  +register() void
  +updateProfile() void
  +delete() void
}

class Place {
  -id: UUID
  -owner_id: UUID
  +title: String
  +description: String
  +price: Float
  +latitude: Float
  +longitude: Float
  +created_at: Date
  +updated_at: Date
  +create () void
  +update () void
  +delete () void
  +list() List~Place~
}

class Review {
  -id: UUID
  +place_id: UUID
  +user_id: UUID
  +rating: Int
  +comment: String
  +created_at: DateTime
  +updated_at: DateTime
  +create() void
  +update() void
  +delete() void
  +listByPlace (place_id) List~Review~
}

class Amenity {
  -id: UUID
  +name: String
  +description: String
  +created_at: Date
  +updated_at: Date
  +create () void
  +update() void
  +delete() void
  +list() List~Amenity~
}

%% العلاقات الأساسية
User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes
Place "1" --> "0..*" Review : has
Place "0..*" o-- "0..*" Amenity : includes


```
