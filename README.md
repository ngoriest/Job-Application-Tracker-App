# Job Application Tracker CLI

A command-line application for tracking job applications with SQLite storage.

  Installation & Setup
  bash
git clone https://github.com/yourusername/job-application-tracker.git
cd job-application-tracker
  pipenv install
   pipenv shell


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
MIT 

Copyright 2025 MANASE KIMUTAI

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.




