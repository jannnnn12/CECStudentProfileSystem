# CECStudentProfileSystem — Django Student Profile Manager

A clean, modern Django web application for managing student profiles at the
College of Engineering & Computing (CEC).

---

## Project Structure

```
cecproject/
├── manage.py
├── requirements.txt
│
├── cecproject/               ← Project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── students/                 ← Main app
│   ├── models.py             ← Student model
│   ├── views.py              ← All function-based views
│   ├── forms.py              ← StudentForm
│   ├── urls.py               ← URL routes
│   ├── admin.py              ← Django admin config
│   │
│   ├── templates/students/
│   │   ├── base.html                  ← Shared layout + navbar
│   │   ├── login.html                 ← Login page (full-screen bg)
│   │   ├── student_list.html          ← Dashboard / card grid
│   │   ├── student_detail.html        ← Single student profile
│   │   ├── student_form.html          ← Add & Edit form
│   │   └── student_confirm_delete.html
│   │
│   └── static/css/
│       └── style.css                  ← Full design system
│
└── media/                    ← Created after first image upload
    └── profile_pics/
```

---

## Quick Start (Windows)

Open VS Code, navigate to the `cecproject` folder in the terminal, then run:

```cmd
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py makemigrations students
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Quick Start (macOS / Linux)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations students
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## Pages & URLs

| URL                          | Page                  | Auth Required |
|------------------------------|-----------------------|---------------|
| `/login/`                    | Login page            | No            |
| `/`                          | Dashboard (card list) | Yes           |
| `/student/add/`              | Add student           | Yes           |
| `/student/<id>/`             | Student detail        | Yes           |
| `/student/<id>/edit/`        | Edit student          | Yes           |
| `/student/<id>/delete/`      | Delete confirm        | Yes           |
| `/admin/`                    | Django admin panel    | Superuser     |

---

## Student Model Fields

| Field           | Type         | Notes                        |
|-----------------|--------------|------------------------------|
| first_name      | CharField    | Max 100 chars                |
| last_name       | CharField    | Max 100 chars                |
| age             | IntegerField | 15–60                        |
| course          | CharField    | Dropdown choices             |
| year_level      | CharField    | 1st–5th Year dropdown        |
| profile_picture | ImageField   | Uploaded to media/profile_pics/ |
| created_at      | DateTimeField| Auto-set on creation         |

---

## Notes

- **Pillow** is required for ImageField (profile picture uploads).
- Images are served from the `/media/` URL in development mode.
- The login page uses a full-screen geometric CSS background (no external image file needed).
- Show/Hide password toggle uses a small inline JavaScript snippet on the login page only.
