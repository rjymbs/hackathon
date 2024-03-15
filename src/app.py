from flask import Flask, render_template, request, redirect
import sqlite3
import os
from sql_db import db_start, create_profile, edit_profile
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



        return redirect('/')  # Перенаправляем на главную страницу
    return render_template('form.html')
# Обработка данных из формы и проверка входа пользователя
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)