---
classDiagram
direction LR

%% =========================
%% Base / Shared
%% =========================
class BaseEntity {
  <<abstract>>
  +UUID id
  +DateTime created_at
  +DateTime updated_at
  +update_timestamp() void
  +to_dict() dict
}

%% =========================
%% Core Entities
%% =========================
class User {
  +String first_name
  +String last_name
  +String email
  +String password_hash
  +is_valid_email(email:String) bool
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
  +is_valid_coordinates(lat:Float, lon:Float) bool
  +add_amenity(a:Amenity) void
  +remove_amenity(a:Amenity) void
  +update_details(title:String,description:String,price:Float,lat:Float,lon:Float) void
}

class Review {
  +String text
  +Int rating
  +is_valid_rating(rating:Int) bool
  +update_review(text:String, rating:Int) void
}

class Amenity {
  +String name
  +rename(name:String) void
}

%% =========================
%% Inheritance
%% =========================
BaseEntity <|-- User
BaseEntity <|-- Place
BaseEntity <|-- Review
BaseEntity <|-- Amenity

%% =========================
%% Relationships (with multiplicities)
%% =========================
%% A User can own many Places; each Place has exactly one owner
User "1" --> "0.." Place : owns

%% A Place can have many Reviews; each Review belongs to exactly one Place
Place "1" --> "0.." Review : has

%% A User can write many Reviews; each Review is written by exactly one User
User "1" --> "0.." Review : writes

%% Many-to-many: Places <-> Amenities
Place "0.." -- "0..*" Amenity : includes
---

%% (Optional but common) Each Review targets one Place and one User explicitly
Review "1" --> "1" Place : about
Review "1" --> "1" User : author
