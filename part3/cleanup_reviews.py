from app import create_app, db
from app.services import facade

def cleanup_admin_reviews():
    app = create_app()
    with app.app_context():
        # List of Admin User IDs whose reviews should be deleted
        # 1. Primary Admin: 60e13da9-945f-44a0-9a8e-e4da8aff96cd
        # 2. Sarah Johnson (Now Admin): bfc2b04d-0c95-410b-aa39-543453cc1054
        admin_ids = ['60e13da9-945f-44a0-9a8e-e4da8aff96cd', 'bfc2b04d-0c95-410b-aa39-543453cc1054']
        
        all_reviews = facade.get_all_reviews()
        deleted_count = 0
        
        for r in all_reviews:
            if str(r.user_id) in admin_ids:
                db.session.delete(r)
                deleted_count += 1
        
        db.session.commit()
        print(f"Successfully deleted {deleted_count} reviews from Admin accounts.")

if __name__ == "__main__":
    cleanup_admin_reviews()
