# Django OnlineCourse Project

Starter implementation for an online course application with Django models, admin customizations, course detail template, and mock exam submission/results.

## Setup
1. `python -m venv .venv`
2. Activate the virtual environment.
3. `python -m pip install django`
4. Configure the Django project settings and include `onlinecourse` in `INSTALLED_APPS`.
5. Add `path("onlinecourse/", include("onlinecourse.urls"))` to the project URL configuration.
6. Run `python manage.py makemigrations` and `python manage.py migrate`.
7. Create an admin user with `python manage.py createsuperuser`.
8. Start with `python manage.py runserver`.

This is a starter project. Adapt URL names, base templates, authentication behavior, and project settings to your course repository before submission.
