# 📧 User Management System

A simple and clean **User Management System** built with Flask and SQLite. Add users with their name and email, search through them, and delete them — all in a lightweight full-stack Python application.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-green?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Lightweight-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- ➕ **Add Users** — Submit a name and email through a clean form
- 📋 **View All Users** — See all saved users in a structured table
- 🔍 **Search** — Filter users by name or email with a live search bar
- 🗑️ **Delete Users** — Remove users with a confirmation dialog
- 🛡️ **Input Validation** — Length limits, duplicate checks, and user cap to prevent crashes
- 💾 **Persistent Storage** — Data saved in a local SQLite database
- 🎨 **Clean UI** — Minimal, responsive design with custom CSS
- ⚡ **Lightweight** — No heavy frameworks, just Flask + SQLite

---

## 🛠️ Tech Stack

| Layer          | Technology       |
|---------------|------------------|
| **Backend**    | Python 3, Flask  |
| **Database**   | SQLite3          |
| **Frontend**   | HTML, CSS        |
| **Templating** | Jinja2 (Flask)   |

---

## 📁 Project Structure

```
python-fullstack-task1/
├── app.py              # Flask application (routes, DB logic, validation)
├── database.db         # SQLite database (users table)
├── static/
│   └── style.css       # Stylesheet for the UI
├── templates/
│   └── index.html      # Main page template (form, search, user table)
├── LICENSE             # MIT License
└── README.md           # This file
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
pip install flask
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

## 📸 Screenshots

### Home Page — Add, Search & Delete Users
```
┌──────────────────────────────────────────────┐
│          User Management System              │
│                                              │
│  [Name________] [Email________] [Add User]   │
│                                              │
│  [Search___________________] [Search] [Clear]│
│  3 user(s) shown                             │
│  ┌────┬──────────┬───────────────┬────────┐  │
│  │ ID │   Name   │     Email     │ Action │  │
│  ├────┼──────────┼───────────────┼────────┤  │
│  │  1 │ John     │ john@mail.com │[Delete]│  │
│  │  2 │ Jane     │ jane@mail.com │[Delete]│  │
│  │  3 │ Bob      │ bob@mail.com  │[Delete]│  │
│  └────┴──────────┴───────────────┴────────┘  │
└──────────────────────────────────────────────┘
```

---

## 🗄️ Database Schema

```sql
CREATE TABLE users (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT,
    email TEXT
);
```

---

## 🔌 API Routes

| Method | Route              | Description                          |
|--------|--------------------|--------------------------------------|
| `GET`  | `/`                | Render page with all users           |
| `POST` | `/`                | Add a new user (name + email)        |
| `GET`  | `/?q=<search>`     | Search users by name or email        |
| `POST` | `/delete/<user_id>`| Delete a user by ID                  |

---

## 🛡️ Input Validation & Safety

| Protection            | Details                                  |
|-----------------------|------------------------------------------|
| **Required fields**   | Name and email cannot be empty           |
| **Name length**       | Max 50 characters (`MAX_NAME_LEN`)       |
| **Email length**      | Max 100 characters (`MAX_EMAIL_LEN`)     |
| **Duplicate email**   | Prevents registering the same email twice|
| **User cap**          | Max 50 users total (`MAX_USERS`)         |
| **SQL Injection**     | All queries use parameterized statements |
| **Delete confirm**    | Browser confirmation dialog before delete|
| **POST for delete**   | Destructive action uses POST, not GET    |

---

## 🧩 How It Works

1. **Add User** → Name + Email submitted via POST → validated → inserted into SQLite → page reloads
2. **Search** → Query sent via GET with `?q=` → `LIKE` query filters results → table updates
3. **Delete User** → POST to `/delete/<id>` → confirmation dialog → row removed → page reloads
4. **Validation** → Every input is checked server-side (length, duplicates, capacity) with user-friendly error messages

---

## 🔮 Future Improvements

- [ ] ✏️ Edit user functionality
- [ ] ✅ Email format validation (regex)
- [ ] 📱 Improved mobile-responsive design
- [ ] 🔐 User authentication
- [ ] 🧪 Unit tests
- [ ] ⏱️ Rate limiting on form submissions

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Ramkumar** — [GitHub](https://github.com/ramkumar007-hub)

---

> Built with ❤️ using Flask & SQLite
