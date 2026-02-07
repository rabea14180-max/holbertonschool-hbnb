This class diagram represents the core entities of the application and how they relate to each other.

User
Represents a system user. A user can own places and write reviews.

Place
Represents a property listed in the system. A place belongs to one user and can have multiple reviews and amenities.

Review
Represents feedback written by a user for a place. Each review is written by one user and belongs to one place.

Amenity
Represents features available in a place (e.g., Wi-Fi, parking). A place can include multiple amenities.

Relationships

A User can own multiple Places

A User can write multiple Reviews.

A Place can have multiple Reviews.

A Place can include multiple Amenities.

Summary

This diagram shows the main domain entities, their attributes, and their relationships, forming the foundation of the business logic for the application.

<img width="1232" height="875" alt="Screenshot 2026-02-06 155914" src="https://github.com/user-attachments/assets/ebfdf6b2-b329-40ef-8622-048c855f9c82" />




