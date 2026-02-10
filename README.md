**HomeHunt 🏡**

HomeHunt is a web-based property search application built with Django. It allows users to register, log in, search for properties, and save their favorite listings for easy access.

**Features**

User Registration & Login

Search Properties

Add Properties to Favorites

Admin Panel for Managing Users & Properties

**Tech Stack**

Backend: Python, Django

Frontend: HTML, CSS, Bootstrap

Database: SQLite (default Django DB)

Admin Panel: Django Admin

**Installation & Setup**

Clone the repository

git clone https://github.com/karuppuvk/Homehunt.git


Navigate to the project directory

cd Homehunt


Create a virtual environment and activate it

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


Install dependencies

pip install django


Apply migrations

python manage.py migrate


Create a superuser (for admin panel access)

python manage.py createsuperuser


Run the development server

python manage.py runserver

Admin Panel Access

URL: http://127.0.0.1:8000/admin/

Login using the superuser credentials created earlier

Admins can manage users and property listings

**Project Purpose**

HomeHunt is built to demonstrate a basic real estate platform using Django with authentication, CRUD functionality, and user-friendly UI.
