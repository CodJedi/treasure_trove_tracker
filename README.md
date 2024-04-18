# treasure_trove_tracker

1. Project Overview
Project Name: Treasure Trove Tracker
Description: This platform combines features of a traditional blogging site with a trading dashboard, allowing users to manage personal finance, investments, and share trading insights through blog posts. It supports user registration, profile management, blog creation, and financial tracking.

3. Installation Guide
Prerequisites:
Python 3.8+
Django 3.2+
Other dependencies are listed in requirements.txt.
Environment Setup:
Virtual environment setup and dependency installation:
bash

python -m venv env
env\Scripts\activate 
pip install -r requirements.txt
Database Configuration:
Using SQLite for development; instructions for migrations:(didnt use any other e.g. PostgreSQL, because i wasnt able use it. I tried to dump sqlite3, but wasnt able to interact with the settings...)
bash

python manage.py migrate

4. Running the Project
Local Server:
Starting the development server:
bash

python manage.py runserver
Accessing the web application at http://localhost:8000.

5. Testing
Test Execution:
Command to run tests to ensure the integrity of new and existing features:
bash

python manage.py test

6. Deployment
(Planned tried didnt went as wanted...) Heroku Deployment:
Detailed steps for deploying on Heroku, with PostgreSQL as the recommended production database.
Configuration details for Procfile and runtime.txt for Heroku setup.

7. Directory Structure
Overview of the main directories and files, reflecting the blogging and trading modules:
bash

/trading_blog_platform
    /accounts
        /migrations
        /templates
        /tests
        models.py
        views.py
        urls.py
    /blog
        /migrations
        /templates
        /tests
        models.py
        views.py
        urls.py
    /trading
        /migrations
        /templates
        /tests
        models.py
        views.py
        urls.py
    /trading_blog_platform
        settings.py
        urls.py
    db.sqlite3
    manage.py
    README.md
    requirements.txt
    
8. API (left no time for it)
