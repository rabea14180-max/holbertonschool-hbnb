classDiagram
direction LR

class BaseEntity {
  <<abstract>>
  +UUID id
  +DateTime created_at
  +DateTime updated_at
  +update_timestamp() void
  +to_dict() dict
}

class User {
  +String first_name
  +String last_name
  +String email
  +String password_hash
  +set_password(password:String) void
  +check_password(password:String) bool
  +update_profile(first_name:String,last_name:String,email:String) void
}

class Place {
  +String title
  +String description
  +Float price
  +Float latitude
  +Float longitude
  +update_details(title:String,description:String,price:Float,latitude:Float,longitude:Float) void
  +add_amenity(amenity:Amenity) void
  +remove_amenity(amenity:Amenity) void
}

class Review {
  +String text
  +Int rating
  +update_review(text:String,rating:Int) void
}

class Amenity {
  +String name
  +rename(name:String) void
}

BaseEntity <|-- User
BaseEntity <|-- Place
BaseEntity <|-- Review
BaseEntity <|-- Amenity

User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes
Place "1" --> "0..*" Review : has
Place "0..*" -- "0..*" Amenity : includes
Review "1" --> "1" User : author
Review "1" --> "1" Place : about
