from flask import Flask, render_template, request, redirect
import sqlite3
import os
from sql_db import db_start, create_profile, edit_profile, check_profile, get_profile, add_points_n
db_start()

app = Flask(__name__)
conn = sqlite3.connect('my_db.db')
cur = conn.cursor()
# Проверяем подключение к базе данных
def check_db_connection():
    if os.path.exists('my_db.db'):
        return True
    else:
        return False


# Главная страница с формой
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/authorise')
def authorise():
    return

@app.route('/main')
def main():
    if not check_db_connection():
        return "Ошибка: База данных не подключена."
    return render_template('index.html')

# Обработка данных из формы и сохранение в базе данных
@app.route('/register', methods=['GET', 'POST'])
def register():

    if not check_db_connection():
        return "Ошибка: База данных не подключена."

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        position = request.form['game']
        comment = request.form['comment']

        f = open('user_id.txt')
        user_id = int(f.read()) + 1
        print(user_id)
        f.close()

        f = open('user_id.txt', 'w')
        f.write(str(user_id))
        f.close()



        date = {'FullName': username,
                'email': email,
                'password': password,
                'JobTitle': position,
                'points': comment}

        create_profile(user_id)
        edit_profile(date, user_id)
        return render_template('index.html')
    return render_template('form.html')
# Обработка данных из формы и проверка входа пользователя

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login_check', methods=['GET', 'POST'])
def login_check():
    if not check_db_connection():
        return "Ошибка: База данных не подключена."
    if request.method == 'POST':
        email = request.form['login']
        password = request.form['password']
        if (check_profile(email, password)):
            file = open('templates/Proekt/data.txt', 'w')
            file.write(email)
            file.close()
            profile = get_profile(email)
            full_name, email, job_title, points = profile
            return render_template('user.html', full_name=full_name, email=email, job_title=job_title, points=points)
        else:
            return render_template('login.html')
    return render_template('login.html')


@app.route('/user', methods=['GET', 'POST'])
def user():

    return render_template('user.html')

@app.route('/Profile_menu', methods=['GET', 'POST'])
def Profile_menu():
    return render_template('profile.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    return render_template('menu.html')

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    return render_template('tasks.html')
@app.route('/reward_points100', methods=['GET', 'POST'])
def reward_points100():
    add_points_n(100)
    return open_profile()

@app.route('/reward_points300', methods=['GET', 'POST'])
def reward_points300():
    add_points_n(300)
    return open_profile()

@app.route('/reward_points500', methods=['GET', 'POST'])
def reward_points500():
    add_points_n(500)
    return open_profile()

@app.route('/reward_points700', methods=['GET', 'POST'])
def reward_points700():
    add_points_n(700)
    return open_profile()
def open_profile():
    file = open('templates/Proekt/data.txt', 'r')
    email = file.read()
    profile = get_profile(email)
    full_name, email, job_title, points = profile
    return render_template('user.html', full_name=full_name, email=email, job_title=job_title, points=points)


if __name__ == '__main__':
    app.run(debug=True)