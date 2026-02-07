Class Diagram Explanation

This diagram represents the core business entities of the system and their relationships.

User:
- Represents system users.
- A user can register, update their profile, and delete their account.
- A user can own multiple places.
- A user can write multiple reviews.

Place:
- Represents a property listed in the system.
- Each place is owned by one user.
- A place can have multiple reviews.
- A place can include multiple amenities.
- Supports create, update, delete, and list operations.

Review:
- Represents a review written by a user for a place.
- Each review is written by one user.
- Each review belongs to one place.
- Includes rating and comment.
- Supports create, update, delete, and listing reviews by place.

Amenity:
- Represents features or services of a place.
- Amenities can be shared by multiple places.
- Supports create, update, delete, and list operations.

Relationships Summary:
- User owns 0..* Places.
- User writes 0..* Reviews.
- Place has 0..* Reviews.
- Place includes 0..* Amenities.


<img width="1232" height="875" alt="Screenshot 2026-02-06 155914" src="https://github.com/user-attachments/assets/ebfdf6b2-b329-40ef-8622-048c855f9c82" />




