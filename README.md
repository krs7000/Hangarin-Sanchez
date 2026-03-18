# Hangarin Task & To-Do Manager

This repository contains a Django implementation of the Hangarin assignment from the provided PDF. It models tasks, priorities, categories, notes, and subtasks, and includes admin configuration plus a seed command for fake data generation.

## Implemented requirements

- `BaseModel` abstract model with `created_at` and `updated_at`
- `__str__` methods for every model
- status enums for `Task` and `SubTask`
- admin filters/search/list displays as specified
- corrected admin plurals for `Category` and `Priority`
- fake data generator for `Task`, `Note`, and `SubTask`
- default records for `Priority` and `Category`
- local virtual environment prepared in `.venv_ssp`
- Git repository initialized in the project root

## Project structure

- `config/` Django project settings and URLs
- `hangarin/` app with models, admin, tests, and management command

## Local setup

Activate the prepared virtual environment:

```powershell
.\.venv_ssp\Scripts\Activate.ps1
```

Apply migrations:

```powershell
python manage.py migrate
```

Create an admin user:

```powershell
python manage.py createsuperuser
```

Seed the database:

```powershell
python manage.py seed_hangarin --tasks 15 --notes-per-task 2 --subtasks-per-task 3
```

Run the development server:

```powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the Bootstrap dashboard. Use `http://127.0.0.1:8000/admin/` for Django admin.

## PythonAnywhere deployment notes

1. Create a Python 3.12 web app in PythonAnywhere.
2. Upload this project and create a virtual environment on PythonAnywhere.
3. Install the dependencies from `requirements.txt`.
4. Set the WSGI file to point to this project directory and `config.settings`.
5. Run:

```powershell
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
python manage.py seed_hangarin
```

`ALLOWED_HOSTS` already accepts `.pythonanywhere.com` by default.

## Social sign-in setup

Google and GitHub OAuth support are available, but they are disabled by default so the app can start cleanly on servers that do not have the social-login environment ready yet.

To enable it on a deployed server, set:

```text
DJANGO_ENABLE_SOCIAL_LOGIN=True
```

Then run migrations and reload the app.

Once enabled:

1. Open `/admin/`
2. Open `Sites` and update the default site domain to your live hostname
3. Open `Social applications`
4. Add a new social application for Google:
   - Provider: `Google`
   - Name: for example `Hangarin Google`
   - Client id: your Google OAuth client ID
   - Secret key: your Google OAuth client secret
   - Sites: attach your current site
5. Add a new social application for GitHub:
   - Provider: `GitHub`
   - Name: for example `Hangarin GitHub`
   - Client id: your GitHub OAuth client ID
   - Secret key: your GitHub OAuth client secret
   - Sites: attach your current site

Use these callback URIs:

- Google:
  - `https://your-domain/accounts/google/login/callback/`
  - `http://127.0.0.1:8000/accounts/google/login/callback/`
- GitHub:
  - `https://your-domain/accounts/github/login/callback/`
  - `http://127.0.0.1:8000/accounts/github/login/callback/`
