from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Flask-login Setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = "Please log in to access this page."
login_manager.login_message_category = "success"

# Validation limits
MAX_NAME_LEN = 50
MAX_EMAIL_LEN = 100
MAX_USERNAME_LEN = 30
MAX_USERS = 50


# User Model
class User(UserMixin):
    def __init__(self, id, name, email, username, password_hash):
        self.id = id
        self.name = name
        self.email = email
        self.username = username
        self.password_hash = password_hash


@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (int(user_id),)).fetchone()
    conn.close()
    if user:
        return User(user['id'], user['name'], user['email'], user['username'], user['password_hash'])
    return None


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id            INTEGER PRIMARY KEY AUTOINCREMENT,
            name          TEXT,
            email         TEXT,
            username      TEXT,
            password_hash TEXT
        )
    ''')
    conn.commit()
    return conn


# Auth Routes

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    error = None
    if request.method == 'POST':
        name = request.form.get('name', '').strip().capitalize()
        email = request.form.get('email', '').strip()
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        # --- Input validation ---
        if not name or not email or not username or not password:
            error = "All fields are required."
        elif len(name) > MAX_NAME_LEN:
            error = f"Name must be {MAX_NAME_LEN} characters or fewer."
        elif len(email) > MAX_EMAIL_LEN:
            error = f"Email must be {MAX_EMAIL_LEN} characters or fewer."
        elif len(username) > MAX_USERNAME_LEN:
            error = f"Username must be {MAX_USERNAME_LEN} characters or fewer."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        elif password != confirm_password:
            error = "Passwords do not match."

        if not error:
            conn = get_db_connection()
            # Check duplicate username
            existing = conn.execute('SELECT id FROM users WHERE username = ?',
                                    (username,)).fetchone()
            if existing:
                error = "This username is already taken."
            else:
                # Check duplicate email
                existing_email = conn.execute('SELECT id FROM users WHERE email = ?',
                                              (email,)).fetchone()
                if existing_email:
                    error = "This email is already registered."

            if not error:
                count = conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]
                if count >= MAX_USERS:
                    error = f"Maximum of {MAX_USERS} users reached."
                else:
                    password_hash = generate_password_hash(password)
                    conn.execute(
                        'INSERT INTO users (name, email, username, password_hash) VALUES (?, ?, ?, ?)',
                        (name, email, username, password_hash)
                    )
                    conn.commit()
                    conn.close()
                    flash("Registration successful! Please log in.", "success")
                    return redirect(url_for('login'))

            conn.close()

    return render_template('register.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    error = None
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not username or not password:
            error = "Both username and password are required."
        else:
            conn = get_db_connection()
            user = conn.execute('SELECT * FROM users WHERE username = ?',
                                (username,)).fetchone()
            conn.close()

            if user and check_password_hash(user['password_hash'], password):
                user_obj = User(user['id'], user['name'], user['email'], user['username'], user['password_hash'])
                login_user(user_obj)
                flash(f"Welcome back, {user['name']}!", "success")
                return redirect(url_for('dashboard'))
            else:
                error = "Invalid username or password."

    return render_template('login.html', error=error)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for('login'))


# Dashboard (Protected)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html',
                           name=current_user.name,
                           username=current_user.username)


# ---- Home / User Management (Task 1 features preserved) ----

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    error = None

    if request.method == 'POST':
        # Only allow adding users if logged in
        if not current_user.is_authenticated:
            conn.close()
            return redirect(url_for('login'))

        name = request.form.get('name', '').strip().capitalize()
        email = request.form.get('email', '').strip()

        # --- Input validation ---
        if not name or not email:
            error = "Both name and email are required."
        elif len(name) > MAX_NAME_LEN:
            error = f"Name must be {MAX_NAME_LEN} characters or fewer."
        elif len(email) > MAX_EMAIL_LEN:
            error = f"Email must be {MAX_EMAIL_LEN} characters or fewer."

        if not error:
            existing = conn.execute('SELECT id FROM users WHERE email = (?)',
                                    (email,)).fetchone()
            if existing:
                error = "This email is already registered."

        if not error:
            count = conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]
            if count >= MAX_USERS:
                error = f"Maximum of {MAX_USERS} users reached."
            else:
                conn.execute('INSERT INTO users (name, email) VALUES (?, ?)',
                             (name, email))
                conn.commit()
                conn.close()
                return redirect('/')

    # Searching
    search_query = request.args.get('q', '').strip()
    if search_query:
        users = conn.execute(
            'SELECT * FROM users WHERE name LIKE ? OR email LIKE ?',
            (f'%{search_query}%', f'%{search_query}%')
        ).fetchall()
    else:
        users = conn.execute('SELECT * FROM users').fetchall()

    conn.close()
    return render_template('index.html',
                           users=users,
                           error=error,
                           search=search_query)


@app.route('/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    rows = conn.execute('SELECT name, email FROM users ORDER BY id').fetchall()
    conn.execute('DELETE FROM users')
    for row in rows:
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)',
                     (row['name'], row['email']))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
