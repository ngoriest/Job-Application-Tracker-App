import sys
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Category, Application

# Database setup
engine = create_engine('sqlite:///job_application.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def create_initial_admin():
    if not session.query(User).first():
        admin = User(
            username="admin",
            email="admin@example.com",
            password="admin123" 
        )
        session.add(admin)
        session.commit()

# ========== APPLICATION OPERATIONS ==========
def create_application():
    print("\n=== Add New Job Application ===")
    company = input("Company Name: ")
    title = input("Job Title: ")
    status = input("Status (Applied/Interview/Offer/Rejected): ")
    deadline = input("Deadline (YYYY-MM-DD): ")
    notes = input("Notes: ")
    
    # List available categories
    print("\nAvailable Categories:")
    fetch_categories()
    category_id = input("Select Category ID: ")
    
    # List available users
    print("\nAvailable Users:")
    fetch_users()
    user_id = input("Select User ID: ")
    
    try:
        new_app = Application(
            company_name=company,
            job_title=title,
            status=status,
            application_date=datetime.now(),
            deadline=datetime.strptime(deadline, "%Y-%m-%d"),
            notes=notes,
            user_id=user_id,
            category_id=category_id
        )
        session.add(new_app)
        session.commit()
        print("\nApplication added successfully!")
    except Exception as e:
        session.rollback()
        print(f"\nError: {e}")

def fetch_applications():
    apps = session.query(Application).all()
    if not apps:
        print("\nNo applications found.")
        return
    
    print("\n=== All Applications ===")
    for app in apps:
        print(f"\nID: {app.id}")
        print(f"Company: {app.company_name}")
        print(f"Title: {app.job_title}")
        print(f"Status: {app.status}")
        print(f"Date Applied: {app.application_date}")
        print(f"Deadline: {app.deadline}")
        print(f"Notes: {app.notes}")
        print(f"User: {app.user.username}")
        print(f"Category: {app.category.name}")

def update_application():
    fetch_applications()
    app_id = input("\nEnter ID of application to update: ")
    app = session.get(Application, app_id)
    
    if not app:
        print("\nApplication not found.")
        return
    
    print("\nLeave blank to keep current value")
    company = input(f"Company Name [{app.company_name}]: ") or app.company_name
    title = input(f"Job Title [{app.job_title}]: ") or app.job_title
    status = input(f"Status [{app.status}]: ") or app.status
    deadline = input(f"Deadline [{app.deadline.date()}]: ") or app.deadline
    notes = input(f"Notes [{app.notes}]: ") or app.notes
    
    try:
        app.company_name = company
        app.job_title = title
        app.status = status
        app.notes = notes
        
        if isinstance(deadline, str):
            app.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        
        session.commit()
        print("\nApplication updated successfully!")
    except Exception as e:
        session.rollback()
        print(f"\nError: {e}")

def delete_application():
    fetch_applications()
    app_id = input("\nEnter ID of application to delete: ")
    app = session.get(Application, app_id)
    
    if not app:
        print("\nApplication not found.")
        return
    
    confirm = input(f"\nAre you sure you want to delete application for {app.company_name}? (y/n): ")
    if confirm.lower() == 'y':
        try:
            session.delete(app)
            session.commit()
            print("\nApplication deleted successfully!")
        except Exception as e:
            session.rollback()
            print(f"\nError: {e}")

# ========== CATEGORY OPERATIONS ==========
def create_category():
    print("\n=== Add New Category ===")
    name = input("Category Name: ")
    desc = input("Description: ")
    
    try:
        new_cat = Category(name=name, description=desc)
        session.add(new_cat)
        session.commit()
        print("\nCategory added successfully!")
    except Exception as e:
        session.rollback()
        print(f"\nError: {e}")

def fetch_categories():
    cats = session.query(Category).all()
    if not cats:
        print("\nNo categories found.")
        return
    

    for cat in cats:
        print(f"ID: {cat.id}  NAME: {cat.name}")
       
def update_category():
    fetch_categories()
    cat_id = input("\nEnter ID of category to update: ")
    cat = session.get(Category, cat_id)
    
    if not cat:
        print("\nCategory not found.")
        return
    
    print("\nLeave blank to keep current value")
    name = input(f"Name [{cat.name}]: ") or cat.name
    desc = input(f"Description [{cat.description}]: ") or cat.description
    
    try:
        cat.name = name
        cat.description = desc
        session.commit()
        print("\nCategory updated successfully!")
    except Exception as e:
        session.rollback()
        print(f"\nError: {e}")

def delete_category():
    fetch_categories()
    cat_id = input("\nEnter ID of category to delete: ")
    cat = session.get(Category, cat_id)
    
    if not cat:
        print("\nCategory not found.")
        return
    
    confirm = input(f"\nAre you sure you want to delete {cat.name}? (y/n): ")
    if confirm.lower() == 'y':
        try:
            session.delete(cat)
            session.commit()
            print("\nCategory deleted successfully!")
        except Exception as e:
            session.rollback()
            print(f"\nError: {e}")

# ========== USER OPERATIONS ==========
def create_user():
    print("\n=== Add New User ===")
    username = input("Username: ")
    email = input("Email: ")
    password = input("Password: ")
    
    try:
        new_user = User(
            username=username,
            email=email,
            password=password
        )
        session.add(new_user)
        session.commit()
        print("\nUser created successfully!")
    except Exception as e:
        session.rollback()
        print(f"\nError: {e}")

def fetch_users():
    users = session.query(User).all()
    if not users:
        print("\nNo users found.")
        return
    
    for user in users:
        print(f"ID: {user.id}  USERNAME: {user.username}  EMAIL: {user.email}")
        if user.applications:
            print("   Applications:")
            for app in user.applications:
                print(f"    - {app.company_name}: {app.job_title}")

def update_user():
    fetch_users()
    user_id = input("\nEnter ID of user to update: ")
    user = session.get(User, user_id)
    
    if not user:
        print("\nUser not found.")
        return
    
    print("\nLeave blank to keep current value")
    username = input(f"Username [{user.username}]: ") or user.username
    email = input(f"Email [{user.email}]: ") or user.email
    password = input("New Password (leave blank to keep current): ")
    
    try:
        user.username = username
        user.email = email
        if password:
            user.password = password
        session.commit()
        print("\nUser updated successfully!")
    except Exception as e:
        session.rollback()
        print(f"\nError: {e}")

def delete_user():
    fetch_users()
    user_id = input("\nEnter ID of user to delete: ")
    user = session.get(User, user_id)
    
    if not user:
        print("\nUser not found.")
        return
    
    confirm = input(f"\nAre you sure you want to delete {user.username}? (y/n): ")
    if confirm.lower() == 'y':
        try:
            session.delete(user)
            session.commit()
            print("\nUser deleted successfully!")
        except Exception as e:
            session.rollback()
            print(f"\nError: {e}")

# ========== MENUS ==========
def application_menu():
    while True:
        print("\n=== APPLICATION MENU ===")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Update Application")
        print("4. Delete Application")
        print("0. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_application()
        elif choice == "2":
            fetch_applications()
        elif choice == "3":
            update_application()
        elif choice == "4":
            delete_application()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

def category_menu():
    while True:
        print("\n=== CATEGORY MENU ===")
        print("1. Add Category")
        print("2. View Categories")
        print("3. Update Category")
        print("4. Delete Category")
        print("0. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_category()
        elif choice == "2":
            fetch_categories()
        elif choice == "3":
            update_category()
        elif choice == "4":
            delete_category()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

def user_menu():
    while True:
        print("\n=== USER MENU ===")
        print("1. Add User")
        print("2. View Users")
        print("3. Update User")
        print("4. Delete User")
        print("0. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_user()
        elif choice == "2":
            fetch_users()
        elif choice == "3":
            update_user()
        elif choice == "4":
            delete_user()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

def main():
    create_initial_admin()
    
    while True:
        print("\n============ JOB APPLICATION TRACKER =============")
        print("1. Application Operations")
        print("2. Category Operations")
        print("3. User Operations")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            application_menu()
        elif choice == "2":
            category_menu()
        elif choice == "3":
            user_menu()
        elif choice == "0":
            print("\nGoodbye!")
            session.close()
            sys.exit()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()