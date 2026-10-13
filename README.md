# 🚀 Job Portal REST API

<div align="center">

**A RESTful backend for a modern job portal** — candidates discover jobs and apply, recruiters manage postings, and administrators oversee the platform.

Built with **Django · Django REST Framework · MySQL**

[![Django](https://img.shields.io/badge/Django-6.1-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-3.18-red)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.14-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.4-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Swagger](https://img.shields.io/badge/Docs-Swagger%20UI-85EA2D?logo=swagger&logoColor=black)](#-api-documentation)
[![License](https://img.shields.io/badge/License-None--Yet-lightgrey)](https://choosealicense.com/)

</div>

> [!IMPORTANT]
> **Project status: 🟡 In development.** The custom user model, MySQL setup, API documentation, and candidate/recruiter registration endpoint are in place. Roadmap items are **planned, not implemented**.

---

## 📋 Table of Contents

- [✨ Overview](#-overview)
- [🧰 Tech Stack](#-tech-stack)
- [✅ Current Features](#-current-features)
- [🗺️ Roadmap](#️-roadmap)
- [📁 Project Structure](#-project-structure)
- [⚙️ Prerequisites](#️-prerequisites)
- [🔧 Local Setup](#-local-setup)
- [🔐 Environment Variables](#-environment-variables)
- [📚 API Documentation](#-api-documentation)
- [🔌 API Endpoints](#-api-endpoints)
- [🧪 Testing](#-testing)
- [🔒 Security Notes](#-security-notes)
- [🔄 Development Workflow](#-development-workflow)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Overview

An interview-ready backend showcasing **practical backend engineering** concepts:

| Concept | Where it shows up |
|---|---|
| 🌐 REST API design & HTTP status codes | All endpoints |
| 👤 Custom user models & JWT auth | `accounts/` app |
| 🛡️ Role-based access control (RBAC) | Candidate / Recruiter / Admin roles |
| 🗄️ Relational schema design | Django ORM + MySQL |
| ✅ Input validation & consistent errors | DRF serializers |
| 🔍 Search, filtering, ordering, pagination | Job listings |
| 🧪 Automated API tests | `python manage.py test` |
| 📖 OpenAPI docs (Swagger UI / ReDoc) | drf-spectacular |
| 🔐 Secure config via environment variables | `python-dotenv` |

---

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python 3.14.8 | Backend language |
| Django 6.1.2 | Web framework & project config |
| Django REST Framework 3.18.1 | API views, serializers, permissions |
| MySQL Server 8.4.11 | Relational database |
| Django ORM | Queries & model relationships |
| Simple JWT 5.5.1 | Token-based authentication |
| django-filter 26.2 | Query-parameter filtering |
| drf-spectacular 0.30.0 | OpenAPI schema & docs |
| python-dotenv 1.2.4 | Local environment variables |
| mysqlclient 2.3.0 | MySQL database driver |
| Git & GitHub | Version control & hosting |

> ⚠️ Versions reflect the initial development environment. Re-verify dependency compatibility and update `requirements.txt` as the project evolves.

---

## ✅ Current Features

**Done** ✅

- [x] Django project initialized
- [x] MySQL database configured via environment variables
- [x] Custom `User` model (`AbstractUser`)
- [x] Roles defined: `CANDIDATE` · `RECRUITER` · `ADMIN`
- [x] Registration serializer with role-choice validation
- [x] `POST /api/auth/register/` — *manually tested* ✅
- [x] JWT token & refresh URL configuration
- [x] OpenAPI schema, Swagger UI & ReDoc routes

**In Progress** 🟡

- [ ] Complete & test JWT login/refresh end-to-end
- [ ] Automated tests for registration & authentication

---

## 🗺️ Roadmap

### 🔐 Authentication & Authorization
- [ ] JWT login & refresh flow
- [ ] Password validation & auth tests
- [ ] Role-based and object-level permissions
- [ ] Admin-only platform management

### 👤 Profiles
- [ ] Candidate profile: skills, experience, resume
- [ ] Recruiter profile & company association
- [ ] Profile read/update with ownership checks

### 🏢 Companies & Jobs
- [ ] Company creation & management
- [ ] Job CRUD endpoints (detail, update, delete)
- [ ] Recruiter ownership rules
- [ ] Job status management (`open` / `closed`)
- [ ] Search, filtering, ordering & pagination

### 📨 Applications
- [ ] Apply to a job
- [ ] Block duplicate applications
- [ ] Block applications to closed jobs
- [ ] Application status tracking
- [ ] Candidate/recruiter permission enforcement

### 🧪 Quality & Delivery
- [ ] Unit & API test coverage
- [ ] Consistent validation & error responses
- [ ] ORM query optimization
- [ ] Documented example requests
- [ ] Production deployment guidance

---

## 📁 Project Structure

```text
job-portal-rest-api/
├── accounts/                 # Custom user model & authentication
├── applications/             # Planned job application functionality
├── companies/                # Planned company & recruiter functionality
├── jobs/                     # Planned job posting functionality
├── job_portal/               # Django settings & URL configuration
├── manage.py
├── .env.example              # Environment variable template
├── .gitignore
└── README.md
```

> Django migrations and additional modules will be added as the application develops.

---

## ⚙️ Prerequisites

- [Python](https://www.python.org/downloads/) 3.14.8 *(or a version verified against project dependencies)*
- [MySQL Server](https://dev.mysql.com/downloads/mysql/) 8.4.x
- [Git](https://git-scm.com/)
- A terminal & code editor *(MySQL Workbench optional but handy)*

---

## 🔧 Local Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Mayur-Satpute/job-portal-rest-api.git
cd job-portal-rest-api
```

### 2️⃣ Create & activate a virtual environment

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

### 3️⃣ Install dependencies

```bash
python -m pip install Django==6.1.2 mysqlclient==2.3.0 python-dotenv==1.2.4 \
  djangorestframework==3.18.1 django-filter==26.2 \
  drf-spectacular==0.30.0 djangorestframework-simplejwt==5.5.1
```

> 💡 If a package won't install on your platform/Python version, check compatibility and use a supported version — don't bypass the error.

### 4️⃣ Create the MySQL database

```sql
CREATE DATABASE job_portal_db;
```

> If the database already exists, don't drop it — just verify it's the intended dev database.

### 5️⃣ Configure environment variables

Copy `.env.example` → `.env` and fill in your local database credentials:

```dotenv
DB_NAME=job_portal_db
DB_USER=root
DB_PASSWORD=replace_with_your_local_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

> 🚫 Never commit `.env` or put real credentials in `.env.example`. `.gitignore` should exclude `.env`.

### 6️⃣ Apply migrations

```bash
python manage.py migrate
```

### 7️⃣ Run system checks

```bash
python manage.py check
```

### 8️⃣ Start the dev server 🎉

```bash
python manage.py runserver
```

The API is live at **`http://127.0.0.1:8000/`**

---

## 🔐 Environment Variables

| Variable | Description | Example |
|---|---|---|
| `DB_NAME` | MySQL database name | `job_portal_db` |
| `DB_USER` | MySQL username | `root` |
| `DB_PASSWORD` | Local MySQL password | *(set privately in `.env`)* |
| `DB_HOST` | MySQL host | `127.0.0.1` |
| `DB_PORT` | MySQL port | `3306` |

> Use a dedicated, least-privilege database user in non-local environments.

---

## 📚 API Documentation

With the dev server running:

| Interface | URL |
|---|---|
| 🟢 **Swagger UI** | http://127.0.0.1:8000/api/docs/ |
| 📄 **OpenAPI schema** | http://127.0.0.1:8000/api/schema/ |
| 🔴 **ReDoc** | http://127.0.0.1:8000/api/redoc/ |

The schema grows as new endpoints land.

---

## 🔌 API Endpoints

### Implemented / Configured

| Method | Endpoint | Purpose | Status |
|---|---|---|---|
| `POST` | `/api/auth/register/` | Register a candidate or recruiter | ✅ Implemented *(manual test passed)* |
| `POST` | `/api/token/` | Obtain JWT access + refresh tokens | 🟡 Configured *(e2e pending)* |
| `POST` | `/api/token/refresh/` | Refresh an access token | 🟡 Configured *(e2e pending)* |
| `GET` | `/api/schema/` | OpenAPI schema | ✅ Configured |
| `GET` | `/api/docs/` | Swagger UI | ✅ Configured |
| `GET` | `/api/redoc/` | ReDoc docs | ✅ Configured |

> JWT endpoints use Simple JWT's default token views. A user must exist before token issuance can be tested.

### Planned

- Candidate & recruiter profile endpoints
- Company CRUD endpoints
- Job CRUD + search / filter / ordering
- Application & status-management endpoints

---

## 🧪 Testing

```bash
# System checks
python manage.py check

# Full test suite
python manage.py test
```

**Planned coverage:** successful registration, invalid roles, duplicate username/email, password hashing, JWT auth, permissions, job workflows, application rules.

---

## 🔒 Security Notes

- 🔑 Keep `.env` out of Git
- 🧂 Use Django's `create_user()` so passwords are hashed
- 🚫 Never allow public registration to assign the `ADMIN` role
- 🛡️ Protect private endpoints with authentication & explicit permissions
- 👤 Validate ownership before any edit/delete
- 💪 Strong local passwords; least-privilege DB accounts outside dev
- ⚠️ **Not production-ready** until security settings, tests, and deployment config are reviewed

---

## 🔄 Development Workflow

1. 🧩 Implement a small feature
2. ✅ Run `python manage.py check` + relevant tests
3. 👀 Review changes with `git status` / `git diff`
4. 💬 Commit with a descriptive message
5. 🚀 Push to GitHub

**Commit message convention** (Conventional Commits):

```text
feat: implement user registration
feat: add JWT authentication tests
feat: add job filtering and pagination
test: cover application permissions
docs: update API setup instructions
```

---

## 🤝 Contributing

This is a **learning project under active development**. Suggestions, issues, and constructive feedback are welcome!

For substantial changes, please **open an issue first** to discuss the proposed implementation.

---

## 📄 License

No license has been selected yet. Until one is added, **do not assume permission** to reuse, distribute, or modify this project's code.

---

<div align="center">

⭐ *Star this repo if you find it useful — it helps the project grow!*

</div>