# 🏥 MedVault — Employee Medical Record Management System

A comprehensive, production-ready **Django** web application for managing employee medical records, appointments, pharmacy inventory, and notifications within an organization. Built with a modern dark-mode UI featuring glassmorphism design, role-based access control, and a fully responsive layout.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [User Roles & Permissions](#-user-roles--permissions)
- [Installation & Setup](#-installation--setup)
- [Running the Application](#-running-the-application)
- [Application Modules](#-application-modules)
- [URL Endpoints](#-url-endpoints)
- [Screenshots](#-screenshots)
- [Environment Variables](#-environment-variables)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Core Functionality
- **User Authentication** — Email-based login (no username), registration, password change, and password reset via email.
- **Role-Based Access Control (RBAC)** — Four distinct roles: Admin, HR, Doctor, and Employee, each with tailored permissions.
- **Medical Records Management** — Create, view, update, and track employee medical records with diagnosis, symptoms, prescriptions, vitals, and file attachments.
- **Appointment Scheduling** — Employees can request appointments; Doctors/Admins/HR can approve, reschedule, or cancel them.
- **Pharmacy & Inventory** — Track medicine stock batches, expiry dates, and dispense medicines against medical records with automatic inventory deduction.
- **Notifications** — Automatic alert generation (e.g., when an appointment is approved) with read/unread tracking.
- **User Profiles** — Comprehensive profiles with personal, employment, and emergency contact information.

### UI/UX
- **Dark-Mode Glassmorphism Design** — Premium, modern interface with translucent cards, gradient accents, and smooth animations.
- **Fully Responsive** — Works seamlessly on desktop, tablet, and mobile with a collapsible sidebar.
- **Real-Time Search** — Client-side table filtering for instant search across records.
- **Auto-Dismiss Messages** — Django flash messages fade out automatically after 5 seconds.
- **Active Navigation Highlighting** — Sidebar intelligently highlights the current page.

---

## 🛠 Tech Stack

| Layer        | Technology                                                             |
|--------------|------------------------------------------------------------------------|
| **Backend**  | Python 3.x, Django 5.2                                                 |
| **Database** | SQLite (default, easily swappable to PostgreSQL/MySQL)                  |
| **Frontend** | HTML5, Vanilla CSS3 (custom design system), Vanilla JavaScript         |
| **Icons**    | Font Awesome 6.5                                                       |
| **Fonts**    | Google Fonts — Inter (body), Outfit (headings)                         |

---

## 📁 Project Structure

```
employee_medical_record_django/
├── accounts/                   # User authentication & profile management
│   ├── admin.py                # User & UserProfile admin registration
│   ├── apps.py                 # App config with signal loading
│   ├── forms.py                # Registration, user update, profile update forms
│   ├── managers.py             # Custom user manager (email-based auth)
│   ├── models.py               # User (AbstractUser) & UserProfile models
│   ├── signals.py              # Auto-create UserProfile on User creation
│   ├── urls.py                 # Auth URLs (login, register, password reset, etc.)
│   └── views.py                # Dashboard, profile, registration views
│
├── medical_records/            # Medical record CRUD
│   ├── admin.py                # MedicalRecord admin registration
│   ├── forms.py                # Medical record form with file upload widgets
│   ├── mixins.py               # DoctorOrAdminRequiredMixin (permission mixin)
│   ├── models.py               # MedicalRecord model (diagnosis, vitals, files)
│   ├── urls.py                 # Record list, detail, create, update URLs
│   └── views.py                # List, detail, create, update views (CBVs)
│
├── appointments/               # Appointment scheduling
│   ├── forms.py                # Employee request form & admin management form
│   ├── models.py               # Appointment model with status workflow
│   ├── urls.py                 # Appointment list, create, update URLs
│   └── views.py                # List, create, update views (CBVs)
│
├── notifications/              # User alert system
│   ├── apps.py                 # App config with signal loading
│   ├── models.py               # UserAlert model
│   ├── signals.py              # Auto-notify on appointment approval
│   ├── urls.py                 # Alert list & mark-as-read URLs
│   └── views.py                # Alert list view & mark-as-read action
│
├── pharmacy/                   # Pharmacy inventory & dispensation
│   ├── forms.py                # Dispense form with stock validation
│   ├── models.py               # Medicine, StockBatch, Dispensation models
│   ├── urls.py                 # Inventory list & dispense URLs
│   └── views.py                # Inventory list & dispense views (CBVs)
│
├── core/                       # Django project configuration
│   ├── settings.py             # Project settings (apps, DB, auth, email)
│   ├── urls.py                 # Root URL configuration
│   ├── wsgi.py                 # WSGI entry point
│   └── asgi.py                 # ASGI entry point
│
├── templates/                  # All HTML templates
│   ├── base.html               # Master layout (sidebar, topbar, content)
│   ├── accounts/               # Auth & profile templates (12 files)
│   ├── medical_records/        # Record list, detail, form (3 files)
│   ├── appointments/           # Appointment list, form (2 files)
│   ├── notifications/          # Alert list (1 file)
│   └── pharmacy/               # Inventory list, dispense form (2 files)
│
├── static/                     # Static assets
│   ├── css/style.css           # Complete design system (dark mode, glassmorphism)
│   └── js/main.js              # Sidebar toggle, search, animations, auto-dismiss
│
├── manage.py                   # Django management script
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

---

## 👥 User Roles & Permissions

| Feature                     | Employee | Doctor | HR  | Admin |
|-----------------------------|----------|--------|-----|-------|
| View own medical records    | ✅       | ✅     | ✅  | ✅    |
| View all medical records    | ❌       | ✅     | ✅  | ✅    |
| Create/edit medical records | ❌       | ✅     | ✅  | ✅    |
| Request appointments        | ✅       | ✅     | ✅  | ✅    |
| Manage appointments         | ❌       | ✅     | ✅  | ✅    |
| View pharmacy inventory     | ❌       | ✅     | ✅  | ✅    |
| Dispense medicines          | ❌       | ✅     | ✅  | ✅    |
| View own notifications      | ✅       | ✅     | ✅  | ✅    |
| Access Django Admin Panel   | ❌       | ❌     | ❌  | ✅    |

---

## 🚀 Installation & Setup

### Prerequisites

- **Python 3.10+** installed
- **pip** package manager
- **Git** (optional, for cloning)

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/employee_medical_record_django.git
cd employee_medical_record_django
```

### Step 2: Create and Activate Virtual Environment

```bash
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install django
```

### Step 4: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

> **Note:** Since this project uses email-based authentication, you will be prompted for an **email** and **password** (no username required).

### Step 6: Run the Development Server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser.

---

## ▶️ Running the Application

| Action                  | Command                                          |
|-------------------------|--------------------------------------------------|
| Start dev server        | `python manage.py runserver`                     |
| Create migrations       | `python manage.py makemigrations`                |
| Apply migrations        | `python manage.py migrate`                       |
| Create superuser        | `python manage.py createsuperuser`               |
| Run system checks       | `python manage.py check`                         |
| Collect static files    | `python manage.py collectstatic`                 |
| Open Django shell       | `python manage.py shell`                         |
| Access admin panel      | Navigate to `http://127.0.0.1:8000/admin/`       |

---

## 📦 Application Modules

### 1. Accounts (`accounts/`)
Handles all user-related functionality using a **custom User model** with email-based authentication (no username field).

- **Custom User Model** — Extends `AbstractUser`, replaces username with email, includes role field.
- **User Profile** — Auto-created via signals; stores personal, employment, and emergency information.
- **Dashboard** — Central landing page with stat cards (record count, appointment count, pending approvals, unread alerts) and recent activity tables.
- **Authentication** — Login, logout, register, password change, and full password reset flow via email.

### 2. Medical Records (`medical_records/`)
Core module for health record management.

- **Record Fields** — Diagnosis, symptoms, prescription (text + file), lab notes (text + file), blood pressure, temperature, status, follow-up date.
- **File Attachments** — Supports PDF, JPG, JPEG, PNG uploads for prescriptions and lab reports.
- **Status Tracking** — Active Treatment, Resolved, Under Observation.
- **Access Control** — Employees see only their own records; Doctors/HR/Admins see all.

### 3. Appointments (`appointments/`)
Manages the appointment lifecycle from request to completion.

- **Employee View** — Request appointments with date, time, and reason.
- **Staff View** — Assign doctors, set status (Pending → Approved → Completed/Cancelled).
- **Auto-Notifications** — Approval triggers an automatic alert to the patient.

### 4. Notifications (`notifications/`)
In-app notification system with read/unread tracking.

- **Signal-Driven** — Alerts are auto-generated when appointments are approved.
- **Mark as Read** — One-click read acknowledgment.
- **Visual Indicators** — Unread alerts are highlighted with a teal left border.

### 5. Pharmacy (`pharmacy/`)
Medicine inventory and dispensation tracking.

- **Medicine Catalog** — Name, generic name, and description.
- **Stock Batches** — Batch number, quantity, expiry date, supplier.
- **Dispensation** — Link to medical records, automatic stock deduction, quantity validation.
- **Low Stock Warnings** — Visual indicator when batch quantity drops below 10.

---

## 🔗 URL Endpoints

### Authentication & Accounts
| URL                                        | Name                      | Description                |
|--------------------------------------------|---------------------------|----------------------------|
| `/`                                        | `dashboard`               | Main dashboard             |
| `/login/`                                  | `login`                   | User login                 |
| `/logout/`                                 | `logout`                  | User logout                |
| `/register/`                               | `register`                | New user registration      |
| `/profile/`                                | `profile`                 | View user profile          |
| `/profile/update/`                         | `profile_update`          | Edit user profile          |
| `/password-change/`                        | `password_change`         | Change password            |
| `/password-change/done/`                   | `password_change_done`    | Password change success    |
| `/password-reset/`                         | `password_reset`          | Request password reset     |
| `/password-reset/done/`                    | `password_reset_done`     | Reset email sent           |
| `/password-reset-confirm/<uidb64>/<token>/`| `password_reset_confirm`  | Set new password           |
| `/password-reset-complete/`               | `password_reset_complete` | Password reset success     |

### Medical Records
| URL                            | Name            | Description              |
|--------------------------------|-----------------|--------------------------|
| `/medical_records/`            | `record_list`   | List all records         |
| `/medical_records/new/`        | `record_create` | Create new record        |
| `/medical_records/<id>/`       | `record_detail` | View record details      |
| `/medical_records/<id>/edit/`  | `record_update` | Edit existing record     |

### Appointments
| URL                               | Name                 | Description              |
|-----------------------------------|----------------------|--------------------------|
| `/appointments/`                  | `appointment_list`   | List all appointments    |
| `/appointments/request/`         | `appointment_create` | Request new appointment  |
| `/appointments/<id>/edit/`       | `appointment_update` | Manage appointment       |

### Notifications
| URL                              | Name              | Description             |
|----------------------------------|-------------------|-------------------------|
| `/notifications/`               | `alert_list`      | List all notifications  |
| `/notifications/<id>/read/`     | `mark_alert_read` | Mark alert as read      |

### Pharmacy
| URL                                           | Name               | Description            |
|-----------------------------------------------|---------------------|------------------------|
| `/pharmacy/inventory/`                        | `inventory_list`    | View medicine stock    |
| `/pharmacy/record/<id>/dispense/`             | `dispense_medicine` | Dispense medicine      |

---

## 🖼 Screenshots

### Login Page
Beautiful glassmorphism login card with gradient background and email-based authentication.

### Dashboard
Central hub with animated stat cards showing Medical Records, Appointments, Pending Approvals, and Unread Alerts counts. Features recent activity tables for quick overview.

### Profile Page
Comprehensive profile view organized into Personal Information, Employment Details, and Medical & Emergency sections with card-based layout.

### Appointments
Searchable appointments table with color-coded status badges (Pending, Approved, Completed, Cancelled) and one-click management actions.

---

## ⚙️ Environment Variables

For production deployment, update the following in `core/settings.py`:

| Setting              | Description                          | Default Value                          |
|----------------------|--------------------------------------|----------------------------------------|
| `SECRET_KEY`         | Django secret key                    | Auto-generated (change for production) |
| `DEBUG`              | Debug mode toggle                    | `True`                                 |
| `ALLOWED_HOSTS`      | Permitted hostnames                  | `[]`                                   |
| `EMAIL_HOST_USER`    | SMTP email address                   | `your_email@gmail.com`                 |
| `EMAIL_HOST_PASSWORD`| SMTP app password                    | `your_app_password`                    |
| `DATABASES`          | Database configuration               | SQLite                                 |

> **Tip:** For Gmail SMTP, generate an [App Password](https://support.google.com/accounts/answer/185833) and use it for `EMAIL_HOST_PASSWORD`.

---

## 🤝 Contributing

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-feature`
3. **Commit** your changes: `git commit -m "Add your feature"`
4. **Push** to the branch: `git push origin feature/your-feature`
5. **Submit** a Pull Request

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

<p align="center">
  Built with ❤️ using <strong>Django 5.2</strong> &amp; <strong>Python</strong>
</p>
