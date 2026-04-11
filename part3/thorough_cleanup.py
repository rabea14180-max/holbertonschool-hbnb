from app import create_app, db
from app.services import facade

def thorough_admin_cleanup():
    app = create_app()
    with app.app_context():
        users = facade.get_all_users()
        # Find all admins or users with 'Admin' or 'HBnB' in their name
        admin_and_problem_users = []
        for u in users:
            name = (u.first_name or "") + " " + (u.last_name or "")
            if u.is_admin or "Admin" in name or "HBnB" in name:
                admin_and_problem_users.append(u.id)
                print(f"Target User: {u.id} | Email: {u.email} | Name: {name} | Admin: {u.is_admin}")

        all_reviews = facade.get_all_reviews()
        count = 0
        for r in all_reviews:
            if r.user_id in admin_and_problem_users:
                print(f"Deleting Review {r.id}: {r.comment}")
                db.session.delete(r)
                count += 1
        
        db.session.commit()
        print(f"Successfully deleted {count} reviews from all Admin/HBnB accounts.")

if __name__ == "__main__":
    thorough_admin_cleanup()
