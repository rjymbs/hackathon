# Updated code without password hashing for demonstration purposes only.
# This is not recommended for production use due to security concerns.

from flask import Flask, render_template, request, redirect, session, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key


# Function to check the database connection
def check_db_connection():
    try:
        conn = sqlite3.connect('my_db.db')
        conn.close()
        return True
    except sqlite3.Error:
        return False


# Function to get a user from the database by username
def get_user(username):
    conn = sqlite3.connect('my_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM profile WHERE email = ?", (email,))
    user = cursor.fetchone()
    conn.close()
    return user


# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check if the database is connected
        if not check_db_connection():
            return "Database connection error."

        # Get username and password from the form
        email = request.form['email']
        password = request.form['password']

        # Get the user from the database
        user = get_user(email)

        # Check if the user exists and the password is correct
        if user and user[3] == password:  # Assuming the password is the fourth column
            session['email'] = user[1]  # Assuming the username is the second column
            return redirect('login.html')  # Redirect to the home page or dashboard
        else:
            flash('Invalid username or password')

    return render_template('login.html')


# This is just to simulate the app running, in this environment it won't actually work
if __name__ == "__main__":
    app.run(debug=True)