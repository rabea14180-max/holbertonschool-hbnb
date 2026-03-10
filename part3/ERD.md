# HBnB — Entity Relationship Diagram

```mermaid
erDiagram
    USER {
        char(36)      id         PK
        varchar(255)  first_name
        varchar(255)  last_name
        varchar(255)  email       "UNIQUE"
        varchar(255)  password
        boolean       is_admin    "DEFAULT FALSE"
        datetime      created_at
        datetime      updated_at
    }

    PLACE {
        char(36)     id          PK
        varchar(255) title
        text         description
        float        price
        float        latitude
        float        longitude
        char(36)     owner_id    FK
        datetime     created_at
        datetime     updated_at
    }

    REVIEW {
        char(36) id         PK
        text     text
        int      rating     "1-5"
        char(36) user_id    FK
        char(36) place_id   FK
        datetime created_at
        datetime updated_at
    }

    AMENITY {
        char(36)     id          PK
        varchar(255) name        "UNIQUE"
        varchar(512) description
        datetime     created_at
        datetime     updated_at
    }

    PLACE_AMENITY {
        char(36) place_id   FK
        char(36) amenity_id FK
    }

    USER         ||--o{ PLACE         : "owns"
    USER         ||--o{ REVIEW        : "writes"
    PLACE        ||--o{ REVIEW        : "receives"
    PLACE        ||--o{ PLACE_AMENITY : "has"
    AMENITY      ||--o{ PLACE_AMENITY : "offered at"
```

## Relationship Summary

| Relationship | Type | Description |
|---|---|---|
| User → Place | One-to-Many | A user can own many places; each place has exactly one owner |
| User → Review | One-to-Many | A user can write many reviews; each review belongs to one user |
| Place → Review | One-to-Many | A place can have many reviews; each review belongs to one place |
| Place ↔ Amenity | Many-to-Many | Via `PLACE_AMENITY`; a place can have many amenities and vice-versa |

## Constraints

- `REVIEW(user_id, place_id)` — **UNIQUE**: one review per user per place
- `REVIEW.rating` — **CHECK**: must be between 1 and 5
- `USER.email` — **UNIQUE**: no duplicate accounts
- `AMENITY.name` — **UNIQUE**: no duplicate amenity names
- All FK relationships cascade on delete

## Integration into GitHub / GitLab

Copy the `mermaid` code block above directly into any `.md` file in your repository.
GitHub renders Mermaid diagrams natively in markdown previews.

To render and export as PNG/SVG, paste only the diagram body (starting with `erDiagram`) into
[Mermaid Live Editor](https://mermaid.live) and use the **Download PNG** / **Download SVG** button.
