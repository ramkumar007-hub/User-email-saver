# 📧 User Email Saver

A simple and clean **User Management System** built with Flask and SQLite. Add users with their name and email, and view them in a neatly styled table — all in a lightweight full-stack Python application.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-green?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Lightweight-blue?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- ➕ **Add Users** — Submit a name and email through a clean form
- 📋 **View All Users** — See all saved users in a structured table
- 💾 **Persistent Storage** — Data saved in a local SQLite database
- 🎨 **Clean UI** — Minimal, responsive design with custom CSS
- ⚡ **Lightweight** — No heavy frameworks, just Flask + SQLite

---

## 🛠️ Tech Stack

| Layer        | Technology       |
|-------------|------------------|
| **Backend**  | Python 3, Flask  |
| **Database** | SQLite3          |
| **Frontend** | HTML, CSS        |
| **Templating** | Jinja2 (Flask) |

---

## 📁 Project Structure

```
python-fullstack-task1/
├── app.py              # Flask application (routes, DB logic)
├── database.db         # SQLite database (users table)
├── static/
│   └── style.css       # Stylesheet for the UI
├── templates/
│   └── index.html      # Main page template (form + user table)
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
source .venv/bin/activate    # Linux/Mac
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

### Home Page — Add & View Users
```
┌──────────────────────────────────────┐
│       User Management System         │
│                                      │
│  [Name________] [Email________] [+]  │
│                                      │
│  ┌────┬──────────┬────────────────┐  │
│  │ ID │   Name   │     Email      │  │
│  ├────┼──────────┼────────────────┤  │
│  │  1 │ John     │ john@mail.com  │  │
│  │  2 │ Jane     │ jane@mail.com  │  │
│  └────┴──────────┴────────────────┘  │
└──────────────────────────────────────┘
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

| Method | Route | Description                     |
|--------|-------|---------------------------------|
| `GET`  | `/`   | Render page with all users      |
| `POST` | `/`   | Add a new user (name + email)   |

---

## 🧩 How It Works

1. **User fills the form** → Name + Email submitted via POST
2. **Flask receives data** → Inserts into SQLite `users` table
3. **Page redirects** → GET request fetches all users from DB
4. **Jinja2 renders** → Users displayed in the HTML table

---

## 🔮 Future Improvements

- [ ] ✏️ Edit user functionality
- [ ] 🗑️ Delete user button
- [ ] 🔍 Search / filter users
- [ ] ✅ Form validation (duplicate email check)
- [ ] 📱 Mobile-responsive design
- [ ] 🔐 User authentication
- [ ] 🧪 Unit tests

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👨‍💻 Author

**Ramkumar** — [GitHub](https://github.com/ramkumar007-hub)

---

> Built with ❤️ using Flask & SQLite
