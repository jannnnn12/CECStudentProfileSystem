# CECStudentProfileSystem

Django-based student profile management system for Cebu Eastern College (CEC).

## Requirements

- Python 3.10+ (recommended)
- pip

## Project Structure

```text
cecproject/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── cecproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   └── css/style.css
└── students/
    ├── admin.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    └── templates/students/
```

## Local Setup (Windows PowerShell)

```powershell
cd "cecproject"
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py makemigrations students
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:

- `http://127.0.0.1:8000/login/`
- `http://127.0.0.1:8000/` (requires login)

If PowerShell blocks activation:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

## Main URLs

| URL | Description | Auth Required |
|---|---|---|
| `/login/` | Admin login page | No |
| `/logout/` | Logout endpoint | Yes |
| `/register/` | Public student registration page | No |
| `/register/success/<id>/` | Registration success page | No |
| `/` | Student dashboard/list | Yes |
| `/student/add/` | Add student profile (admin side) | Yes |
| `/student/<id>/` | Student details | Yes |
| `/student/<id>/edit/` | Edit student profile | Yes |
| `/student/<id>/inactive/` | Mark student inactive | Yes |
| `/student/<id>/active/` | Reactivate student | Yes |
| `/admin/` | Django admin | Superuser |

## Notes

- The app uses SQLite by default (`db.sqlite3`).
- Static files are loaded from `cecproject/static/`.
- Uploaded files are served from `/media/` in development mode.
- Pillow is required for profile image uploads.
