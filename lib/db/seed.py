from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Category, Application

def seed_database():
    # Database setup##
    engine = create_engine('sqlite:///job_application.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Clear existing data
        session.query(Application).delete()
        session.query(Category).delete()
        session.query(User).delete()
        session.commit()

        # Create sample users
        users = [
            User(
                username="johndoe",
                email="john@example.com",
                password="password123"  # Note: In production, use hashed passwords
            ),
            User(
                username="janedoe",
                email="jane@example.com",
                password="password456"
            ),
            User(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
        ]
        session.add_all(users)
        session.commit()

        # Create sample categories
        categories = [
            Category(
                name="Software Development",
                description="Software engineering and development roles"
            ),
            Category(
                name="Data Science",
                description="Data analysis, machine learning, and AI roles"
            ),
            Category(
                name="DevOps",
                description="Cloud infrastructure and deployment roles"
            ),
            Category(
                name="Product Management",
                description="Product owner and manager roles"
            ),
            Category(
                name="UX/UI Design",
                description="User experience and interface design roles"
            )
        ]
        session.add_all(categories)
        session.commit()

        # Create sample applications
        today = datetime.now()
        applications = [
            Application(
                company_name="TechCorp",
                job_title="Senior Software Engineer",
                status="Applied",
                application_date=today - timedelta(days=5),
                deadline=today + timedelta(days=30),
                notes="Focus on Python and Django",
                user_id=1,
                category_id=1
            ),
            Application(
                company_name="DataWorld",
                job_title="Data Scientist",
                status="Interview",
                application_date=today - timedelta(days=10),
                deadline=today + timedelta(days=15),
                notes="Second interview scheduled",
                user_id=1,
                category_id=2
            ),
            Application(
                company_name="CloudSystems",
                job_title="DevOps Engineer",
                status="Offer",
                application_date=today - timedelta(days=20),
                deadline=today - timedelta(days=5),
                notes="Considering offer of $120k",
                user_id=2,
                category_id=3
            ),
            Application(
                company_name="DesignHub",
                job_title="UX Designer",
                status="Rejected",
                application_date=today - timedelta(days=30),
                deadline=today - timedelta(days=10),
                notes="Went with another candidate",
                user_id=2,
                category_id=5
            ),
            Application(
                company_name="ProductLabs",
                job_title="Product Manager",
                status="Applied",
                application_date=today - timedelta(days=2),
                deadline=today + timedelta(days=45),
                notes="Remote position",
                user_id=1,
                category_id=4
            )
        ]
        session.add_all(applications)
        session.commit()

        print("Database seeded successfully with sample data!")
        
    except Exception as e:
        session.rollback()
        print(f"Error seeding database: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    seed_database()