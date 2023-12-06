# blogs_news_webapp_iit_bombay


A short description of your project.

## Table of Contents

1. Authentication
a) User login, logout
b) User registration
c) Standard password validation
d) Forgot password validation
2. API calls, JSON handling, Dashboard
a) Fetch and display News image, title in home page (after logging-in)
b) Redirect user to detailed user article on clicking news clip image
c) User creates blog-blog title, content, date created(automatic)
d) User delete his/her own blogs from dashboard
3. Serializers - Django REST Framework
a) Site-administrator can view existing blogs list in json format through api
endpoint only
b) Site-admin can delete, update, create blogs through api endpoints onl

## is an innovative and secure platform that brings together news, blogs, and community engagement. This project aims to provide users with a seamless and secure registration and login process, giving them access to a diverse range of news articles fetched in real-time from trusted sources using the News API.

Provide a brief description of what your project does.

## Getting Started
Clone the Repository: Start by cloning this repository to your local machine.

Install Dependencies: Run pip install -r requirements.txt to install the required dependencies.

Configure Database Settings: Update the database settings in settings.py to match your environment.

Apply Migrations: Apply the database migrations using python manage.py migrate.

Create Superuser: Create a superuser account for administrative access using python manage.py createsuperuser.

Run the Server: Start the development server with python manage.py runserver.

Access the Platform: Open your web browser and visit the provided URL to access ContentHub.
Provide instructions on how to get started with your project.

## Technology Stack
Python
Django
HTML/CSS
Bootstrap
SQLite (default database)
jQuery/JS
Folder Structure
project_name/: Django project directory.
app_name/: Django app directory.
migrations/: Database migration files.
static/: Static files (CSS, JS, images).
templates/: HTML templates.
forms.py: Django forms for user input validation.
models.py: Django models representing the database schema.
urls.py: URL configuration for the app.
views.py: View functions handling user requests and rendering templates.


Explain how users can use your project. Include examples or screenshots if possible.

## Contributing

Explain how others can contribute to your project. Include guidelines for submitting pull requests, reporting issues, etc.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
