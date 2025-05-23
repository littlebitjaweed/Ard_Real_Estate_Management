# Ard - Real Estate Management App
URL: https://ard-9cpt.onrender.com/ <br>
Ard is a simple real estate management website built using Django, and deployed on cloud platform Render.  
It allows users to:

- Sign up and log in
- Upload their own properties
- Edit or delete only their own listings
- View properties uploaded by others

This project demonstrates basic CRUD operations in Django with simple authentication and authorization.

## Features

- Django-based backend
- Image uploads for properties
- User-specific property management
- Authentication (login, logout, signup)

## Setup

1. Clone the repository
2. Set up a virtual environment
3. Install requirements
4. Run migrations
5. Start the development server

```bash
git clone <your_repo_url>
cd <your_repo_folder>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
