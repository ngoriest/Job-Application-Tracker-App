# Job Application Tracker CLI

A command-line application for tracking job applications with SQLite storage.

##  Installation & Setup
```bash
git clone https://github.com/yourusername/job-application-tracker.git
cd job-application-tracker
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

🚀 Quick Start
Run the application:

bash
python cli.py
Default admin credentials:
Username: admin | Password: admin123

🛠️ Features
Applications
Add new applications with company, position, status, and deadlines

View all applications in a clean list

Update application details at any stage

Delete applications when needed

Categories
Create categories (e.g., "Software", "Marketing")

Assign applications to categories

Manage existing categories

Users
Basic multi-user support

Simple user management

🔍 Usage Examples
Adding an application:

> python cli.py
> [Main Menu] Select 1 (Applications)
> [Application Menu] Select 1 (Add)
> Enter company: Google
> Enter position: Software Engineer
> ...
Checking upcoming deadlines:

View Applications → Sort by Deadline
🗃️ Database Info
Automatically creates job_applications.db

Schema:

Applications (company, position, status, deadline)

Categories (name, description)

Users (username, email)

⚠️ Important Notes
This is a development tool

Passwords are stored in plaintext (not for production)

Back up your database regularly

📜 License
MIT - See LICENSE for details.


