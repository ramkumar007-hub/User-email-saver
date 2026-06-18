from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# --- Validation limits ---
MAX_NAME_LEN = 50
MAX_EMAIL_LEN = 100
MAX_USERS = 50


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    error = None

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()

        # --- Input validation ---
        if not name or not email:
            error = "Both name and email are required."
        elif len(name) > MAX_NAME_LEN:
            error = f"Name must be {MAX_NAME_LEN} characters or fewer."
        elif len(email) > MAX_EMAIL_LEN:
            error = f"Email must be {MAX_EMAIL_LEN} characters or fewer."

        if not error:
            # Check duplicate email
            existing = conn.execute('SELECT id FROM users WHERE email = (?)',
                                    (email,)).fetchone()
            if existing:
                error = "This email is already registered."

        if not error:
            # Check user count limit
            count = conn.execute('SELECT COUNT(*) FROM users').fetchone()[0]
            if count >= MAX_USERS:
                error = f"Maximum of {MAX_USERS} users reached."
            else:
                conn.execute('INSERT INTO users (name, email) VALUES (?, ?)',
                             (name, email))
                conn.commit()
                conn.close()
                return redirect('/')

    # --- Search ---
    search_query = request.args.get('q', '').strip()
    if search_query:
        users = conn.execute(
            'SELECT * FROM users WHERE name LIKE ? OR email LIKE ?',
            (f'%{search_query}%', f'%{search_query}%')
        ).fetchall()
    else:
        users = conn.execute('SELECT * FROM users').fetchall()

    conn.close()
    return render_template('index.html', users=users, error=error, search=search_query)


@app.route('/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
