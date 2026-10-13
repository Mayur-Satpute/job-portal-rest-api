from pathlib import Path
import pypandoc

markdown = r"""# Job Portal REST API

A RESTful backend for a job portal where candidates can discover jobs and apply, recruiters can manage job postings, and administrators can oversee the platform. Built with Django and Django REST Framework, with MySQL as the database.

> **Project status:** In development. The custom user model, initial database setup, API documentation configuration, and candidate/recruiter registration endpoint are in place. Features listed under the roadmap are planned and should not be considered implemented yet.

## Table of Contents

- [Overview](#overview)
- [Technology Stack](#technology-stack)
- [Current Features](#current-features)
- [Planned Features](#planned-features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Local Setup](#local-setup)
- [Environment Variables](#environment-variables)
- [API Documentation](#api-documentation)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Security Notes](#security-notes)
- [Development Workflow](#development-workflow)
- [Contributing](#contributing)
- [License](#license)

## Overview

The goal of this project is to build an interview-ready backend that demonstrates practical backend engineering concepts:

- REST API design and HTTP status codes
- Custom user models and authentication
- Role-based access control (RBAC)
- Relational database design with Django ORM and MySQL
- Input validation and consistent error handling
- Search, filtering, ordering, and pagination
- Automated API tests
- API documentation with OpenAPI and Swagger UI
- Secure configuration using environment variables

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| Django | Web framework and project configuration |
| Django REST Framework | REST API views, serializers, and permissions |
| MySQL | Relational database |
| Django ORM | Database queries and model relationships |
| Simple JWT | JWT-based authentication |
| django-filter | Query parameter filtering |
| drf-spectacular | OpenAPI schema and API documentation |
| python-dotenv | Loading local environment variables |
| Git and GitHub | Version control and source hosting |

Versions used during initial development include Python 3.14.8, Django 6.1.2, MySQL Server 8.4.11, Django REST Framework 3.18.1, django-filter 26.2, drf-spectacular 0.30.0, Simple JWT 5.5.1, mysqlclient 2.3.0, and python-dotenv 1.2.4. Confirm dependency compatibility and update the dependency lock/requirements file as the project evolves.

## Current Features

- [x] Django project initialized
- [x] MySQL database configured through environment variables
- [x] Custom `User` model based on Django's `AbstractUser`
- [x] User roles defined: `CANDIDATE`, `RECRUITER`, and `ADMIN`
- [x] Candidate/recruiter registration serializer with role-choice validation
- [x] Registration endpoint at `POST /api/auth/register/`
- [x] JWT token and refresh URL configuration
- [x] OpenAPI schema, Swagger UI, and ReDoc URL configuration
- [ ] Complete and test JWT login/refresh behavior
- [ ] Automated tests for registration and authentication

## Planned Features

### Authentication and Authorization
- Candidate and recruiter registration
- JWT login and refresh
- Password validation and authentication tests
- Role-based and object-level permissions
- Admin-only platform management

### Candidate and Recruiter Profiles
- Candidate profile, skills, experience, and resume details
- Recruiter profile and company association
- Profile read/update endpoints with ownership checks

### Companies and Jobs
- Company creation and management
- Job creation, detail, update, and deletion endpoints
- Recruiter ownership rules
- Job status management (for example, open and closed)
- Search, filtering, ordering, and pagination

### Applications
- Apply to a job
- Prevent duplicate applications to the same job
- Prevent applications to closed jobs
- Track application status
- Enforce candidate/recruiter permissions and application ownership

### Quality and Delivery
- Automated unit and API tests
- Consistent validation and error responses
- ORM query optimization
- API documentation and example requests
- Production configuration and deployment guidance

## Project Structure

```text
job-portal-rest-api/
├── accounts/                 # Custom user model and authentication
├── applications/             # Planned job application functionality
├── companies/                # Planned company and recruiter functionality
├── jobs/                     # Planned job posting functionality
├── job_portal/               # Django settings and URL configuration
├── manage.py
├── .env.example              # Environment variable template
├── .gitignore
└── README.md
```

Django migration files and additional modules will be added as the application develops.

## Prerequisites

Install the following before setting up the project:

- Python 3.14.8 (or another version verified against the project's dependencies)
- MySQL Server 8.4.x
- Git
- A terminal and code editor
- MySQL Workbench is optional but useful for database administration

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Mayur-Satpute/job-portal-rest-api.git
cd job-portal-rest-api
```

### 2. Create and activate a virtual environment

**Windows CMD:**

```cmd
python -m venv venv
venv\Scripts\activate
```

**PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

The project should have a maintained `requirements.txt` as dependencies are finalized. Until that file is added, install the currently used packages:

```bash
python -m pip install Django==6.1.2 mysqlclient==2.3.0 python-dotenv==1.2.4 djangorestframework==3.18.1 django-filter==26.2 drf-spectacular==0.30.0 djangorestframework-simplejwt==5.5.1
```

If a package cannot be installed for your platform or Python version, check its current compatibility and use a supported version rather than bypassing the error.

### 4. Create the MySQL database

In MySQL Workbench or a MySQL client, run:

```sql
CREATE DATABASE job_portal_db;
```

If the database already exists, do not drop it; just verify that it is the intended development database.

### 5. Configure environment variables

Copy `.env.example` to `.env` and set the values for your local database. On Windows CMD, you can create/edit `.env` using your editor.

Example `.env`:

```dotenv
DB_NAME=job_portal_db
DB_USER=root
DB_PASSWORD=replace_with_your_local_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

Never commit `.env` or place real credentials in `.env.example`. The repository's `.gitignore` should exclude `.env`.

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Run system checks

```bash
python manage.py check
```

### 8. Start the development server

```bash
python manage.py runserver
```

The API is then available at `http://127.0.0.1:8000/`.

## Environment Variables

| Variable | Description | Example |
|---|---|---|
| `DB_NAME` | MySQL database name | `job_portal_db` |
| `DB_USER` | MySQL username | `root` |
| `DB_PASSWORD` | Local MySQL password | Set privately in `.env` |
| `DB_HOST` | MySQL host | `127.0.0.1` |
| `DB_PORT` | MySQL port | `3306` |

Use a dedicated database user with only the privileges needed for the application in non-local environments. Do not use a personal or production password in screenshots, commits, or issue reports.

## API Documentation

With the development server running:

- **Swagger UI:** `http://127.0.0.1:8000/api/docs/`
- **OpenAPI schema:** `http://127.0.0.1:8000/api/schema/`
- **ReDoc:** `http://127.0.0.1:8000/api/redoc/`

These routes are configured in the project. The schema will grow as API endpoints are implemented.

## API Endpoints

### Implemented/configured

| Method | Endpoint | Purpose | Status |
|---|---|---|---|
| `POST` | `/api/auth/register/` | Register a candidate or recruiter | Implemented; manual registration test passed |
| `POST` | `/api/token/` | Obtain JWT access and refresh tokens | Configured; end-to-end test pending |
| `POST` | `/api/token/refresh/` | Refresh an access token | Configured; end-to-end test pending |
| `GET` | `/api/schema/` | Retrieve the OpenAPI schema | Configured |
| `GET` | `/api/docs/` | Swagger UI | Configured |
| `GET` | `/api/redoc/` | ReDoc documentation | Configured |

JWT token endpoints use Simple JWT's default token view behavior. A user must exist before token issuance can be tested.

### Planned

The following endpoints will be documented here as they are implemented:

- Candidate and recruiter profile endpoints
- Company CRUD endpoints
- Job CRUD, search, filter, and ordering endpoints
- Job application and status-management endpoints

## Testing

Run Django's system checks:

```bash
python manage.py check
```

Run the automated test suite:

```bash
python manage.py test
```

Automated tests are planned and should be expanded to cover successful registration, invalid roles, duplicate usernames/emails, password hashing, JWT authentication, permissions, job workflows, and application rules.

## Security Notes

- Keep `.env` out of Git.
- Use Django's `create_user()` to create users so passwords are hashed.
- Do not allow public registration to assign the `ADMIN` role.
- Protect private endpoints with authentication and explicit permissions.
- Validate ownership before allowing users to edit or delete resources.
- Use strong local passwords and a least-privilege database account outside local development.
- Do not treat this project as production-ready until security settings, automated tests, deployment configuration, and operational requirements have been reviewed.

## Development Workflow

Work feature by feature:

1. Implement a small feature.
2. Run `python manage.py check` and relevant tests.
3. Inspect changes using `git status` and `git diff`.
4. Commit the feature with a descriptive message.
5. Push the commit to GitHub.

Example commit messages:

```text
feat: implement user registration
feat: add JWT authentication tests
feat: add job filtering and pagination
test: cover application permissions
docs: update API setup instructions
```

## Contributing

This is a learning project under active development. Suggestions, issues, and constructive feedback are welcome. For substantial changes, open an issue first to discuss the proposed implementation.

## License

No license has been added yet. Until a license is selected and committed, do not assume that others have permission to reuse, distribute, or modify this project's code.
"""

output_path = Path("/mnt/data/README.md")
pypandoc.convert_text(markdown, "md", format="md", outputfile=str(output_path), extra_args=["--standalone"])
print(f"Created: {output_path}")
print(f"Size: {output_path.stat().st_size} bytes")
