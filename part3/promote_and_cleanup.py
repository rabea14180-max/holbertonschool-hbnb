from app import create_app, db
from app.services import facade

def promote_and_cleanup():
    app = create_app()
    with app.app_context():
        # 1. Find the user Sarah Johnson
        email = 'sarah.johnson@email.com'
        user = facade.get_user_by_email(email)
        if not user:
            print(f"User {email} not found.")
            return

        # 2. Update her to admin
        user.is_admin = True
        db.session.add(user)
        db.session.commit()
        print(f"Updated user ID {user.id} ({email}) to Admin status.")

        # 3. Delete all her reviews
        all_reviews = facade.get_all_reviews()
        sarah_reviews = [r for r in all_reviews if str(r.user_id) == str(user.id)]
        
        count = 0
        for r in sarah_reviews:
            db.session.delete(r)
            count += 1
        
        db.session.commit()
        print(f"Successfully deleted {count} reviews associated with Sarah.")

if __name__ == "__main__":
    promote_and_cleanup()
