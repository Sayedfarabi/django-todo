# Django REST API with PostgreSQL & UV

A professional, scalable Task Management API built with **Django** and **Django REST Framework (DRF)**. This project uses the ultra-fast **uv** package manager for dependency management and follows a **Service Layer** architecture for clean code.

---

## 🛠️ Installation & Setup Guide

Follow these steps to get the project running on your local machine.

### 1. Prerequisite: Install `uv`

If you don't have `uv` installed, run this in your **Windows PowerShell**:

```powershell
powershell -ExecutionPolicy ByPass -c "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"

Verify installation: uv --version

2. Initialize the Project
Create your project folder and initialize the environment:
mkdir my_django_project
cd my_django_project
uv init

3. Install Dependencies
Add all necessary packages for Django, PostgreSQL, and API development:
# Frameworks
uv add django djangorestframework django-cors-headers

# Database & Environment
uv add psycopg2-binary django-environ

4. Project & App Structure
Create the Django project configuration and the core application module:
# Create project config
uv run django-admin startproject config .

# Create 'todo' app module
uv run python manage.py startapp todo

⚙️ Configuration
5. Database Migration
Ensure your PostgreSQL database is running, then apply the migrations:
uv run python manage.py migrate

6. Start Development Server
uv run manage.py runserver

The server will be available at: http://127.0.0.1:8000


🏗️ Architecture & Features
This project implements a Service Layer (NestJS Style) to separate business logic from the views.

Models: PostgreSQL database schema.

Serializers: Data validation and JSON transformation (similar to NestJS DTOs).

Services: Centralized business logic and database queries in services.py.

CORS Enabled: Pre-configured to communicate with frontend frameworks like Next.js.

📡 API Endpoints
Action,Method,URL Path
List all tasks,GET,/api/tasks/
Create task,POST,/api/tasks/
Get single task,GET,/api/tasks/<id>/
Partial Update,PATCH,/api/tasks/<id>/
Delete task,DELETE,/api/tasks/<id>/

🛡️ Security Note
Remember to create a .env file in the root directory and move your SECRET_KEY and DATABASE_URL there to keep your credentials safe.
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://user:password@localhost:5432/db_name

```
