from app import create_app, db
from app.services import facade

def final_review_cleanup():
    app = create_app()
    with app.app_context():
        # Specific accounts to clean up
        target_uids = [
            'fc431346-d145-49b8-be75-de6ee728b342', # ahmd Alli
            '60e13da9-945f-44a0-9a8e-e4da8aff96cd'  # Admin HBnB
        ]
        
        all_reviews = facade.get_all_reviews()
        deleted_count = 0
        
        for r in all_reviews:
            # 1. Check by User ID
            is_target_user = str(r.user_id) in target_uids
            
            # 2. Check by content (using the Arabic word for "beautiful")
            # Handle encoding by checking for the substring
            comment = str(r.comment or r.text or "")
            # Keep the Arabic token below unchanged, because some legacy reviews contain it.
            # Delete reviews from the target users and reviews that match this content token.
            
            if is_target_user:
                print(f"Deleting review {r.id} from target user {r.user_id}")
                db.session.delete(r)
                deleted_count += 1
            elif "جميل" in comment:
                print(f"Deleting review {r.id} due to content match: {comment}")
                db.session.delete(r)
                deleted_count += 1
        
        db.session.commit()
        print(f"Successfully deleted {deleted_count} targeted reviews.")

if __name__ == "__main__":
    final_review_cleanup()
