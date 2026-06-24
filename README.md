# 📧 User Management System : Authentication

A **User Management System** with full **authentication** (Register, Login, Logout) built with Flask and SQLite. This project extends previous project by adding secure user authentication while preserving all original features.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-green?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Lightweight-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- 🔐 **User Registration** — Create an account with name, email, username, and password
- 🔑 **User Login** — Secure login with username and password verification
- 🚪 **Logout** — End session securely
- 🛡️ **Password Hashing** — All passwords hashed using Werkzeug (never stored in plain text)
- 📊 **Protected Dashboard** — Only accessible to logged-in users
- 🔒 **Protected Actions** — Add/delete users requires authentication
- ✅ **Input Validation** — Length limits, duplicate checks, password matching

---

## 🛠️ Tech Stack

| Layer          | Technology                    |
|---------------|-------------------------------|
| **Backend**    | Python 3, Flask               |
| **Auth**       | Flask-Login, Werkzeug Hash    |
| **Database**   | SQLite3                       |
| **Frontend**   | HTML, CSS, Jinja2             |

---

## 📁 Project Structure

```
python-fullstack-task1/
├── app.py                 # Flask app (auth routes + user management)
├── database.db            # SQLite database (users table with auth columns)
├── static/
│   └── style.css          # Stylesheet (auth + dashboard styles)
├── templates/
│   ├── index.html         # Main page (user management, auth-aware)
│   ├── register.html      # Registration form
│   ├── login.html         # Login form
│   └── dashboard.html     # Protected dashboard
├── LICENSE                # MIT License
└── README.md              # This file
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- pip (Python package manager)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/ramkumar007-hub/User-email-saver.git
cd User-email-saver
```

**2. Create a virtual environment (recommended)**
```bash
python -m venv .venv
source .venv/bin/activate    # Linux / Mac / Arch (zsh)
# .venv\Scripts\activate     # Windows
```

**3. Install dependencies**
```bash
pip install flask flask-login
```

**4. Run the application**
```bash
python app.py
```

**5. Open your browser**
```
http://127.0.0.1:5000
```

---

## 🔐 Authentication Flow

### Registration Flow
1. User visits `/register`
2. Fills in: Name, Email, Username, Password, Confirm Password
3. Server validates all fields (length, duplicates, password match)
4. Password is hashed using `werkzeug.security.generate_password_hash`
5. User is stored in SQLite database
6. Redirected to `/login` with success message

### Login Flow
1. User visits `/login`
2. Enters: Username, Password
3. Server looks up user by username
4. Password verified using `werkzeug.security.check_password_hash`
5. `login_user()` creates a Flask-Login session (handles session management automatically)
6. Redirected to `/dashboard`

### Logout Flow
1. User clicks Logout
2. `logout_user()` destroys the Flask-Login session
3. Redirected to `/login`

### Protected Routes
- `/dashboard` — Only accessible when logged in (`@login_required` decorator)
- Add/Delete users — Only accessible when logged in (`@login_required` decorator)
- Unauthenticated users are automatically redirected to `/login`

## 🗄️ Database Schema (Updated)

```sql
CREATE TABLE users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT,
    email         TEXT,
    username      TEXT,
    password_hash TEXT
);
```

---

## 🔌 API Routes

| Method | Route              | Description                          | Auth Required |
|--------|--------------------|--------------------------------------|:---:|
| `GET`  | `/`                | Render page with all users           | No |
| `POST` | `/`                | Add a new user (name + email)        | Yes |
| `GET`  | `/?q=<search>`     | Search users by name or email        | No |
| `POST` | `/delete/<user_id>`| Delete a user by ID                  | Yes |
| `GET`  | `/register`        | Show registration form               | No* |
| `POST` | `/register`        | Process registration                 | No* |
| `GET`  | `/login`           | Show login form                      | No* |
| `POST` | `/login`           | Process login                        | No* |
| `GET`  | `/logout`          | End session                          | Yes |
| `GET`  | `/dashboard`       | Protected dashboard                  | Yes |

\* Redirects to dashboard if already logged in

---

## 🛡️ Security Features

| Protection              | Details                                          |
|-------------------------|--------------------------------------------------|
| **Password Hashing**    | Werkzeug `generate_password_hash` (pbkdf2:sha256)|
| **Session Management**  | Flask-Login with `LoginManager` and random secret key |
| **Input Validation**    | Length limits, required fields, duplicate checks  |
| **Password Matching**   | Confirm password field must match                |
| **Min Password Length** | 6 characters minimum                             |
| **SQL Injection**       | All queries use parameterized statements         |
| **Protected Routes**    | Add/delete require authentication               |
| **POST for Delete**     | Destructive action uses POST, not GET            |
| **Delete Confirm**      | Browser confirmation dialog before delete        |

---

##  How It Works

1. **Register** → Fill form → Validate → Hash password → Store in DB → Redirect to login
2. **Login** → Enter credentials → Verify hash → Create session → Redirect to dashboard
3. **Dashboard** → Protected page showing user info → Link to manage users
4. **Add User** (logged in) → POST to `/` → Validate → Insert into DB → Reload
5. **Search** → GET with `?q=` → `LIKE` query → Filter results (works without login)
6. **Delete User** (logged in) → POST to `/delete/<id>` → Confirmation → Remove → Reorder IDs
7. **Logout** → Clear session → Redirect to login

---

## 📖 References

- [Flask Sessions](https://flask.palletsprojects.com/en/latest/quickstart/#sessions)
- [Werkzeug Security](https://werkzeug.palletsprojects.com)
- [OWASP Password Guidelines](https://owasp.org/www-project-top-ten/)

---

##  Future Improvements

- [ ]  Edit user functionality
- [ ]  Email format validation (regex)
- [ ]  Improved mobile-responsive design
- [ ]  Password reset / forgot password
- [ ]  User roles (admin, regular user)
- [ ]  Unit tests
- [ ] ⏱ Rate limiting on login attempts
- [ ]  CSRF protection (Flask-WTF)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Ramkumar** — [GitHub](https://github.com/ramkumar007-hub)

---

> Built with ❤️ using Flask & SQLite - Authentication System
