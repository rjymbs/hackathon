import sqlite3 as sq

# Функция для проверки логина и пароля пользователя
def authenticate_user(login, password):
    # Подключение к базе данных
    db = sq.connect("my_db.db")
    cur = db.cursor()

    # Поиск пользователя в базе данных
    cur.execute('SELECT * FROM profile WHERE user_id=? AND password=?', (login, password))
    user = cur.fetchone()

    # Закрытие соединения с базой данных
    cur.close()
    db.close()

    if user is not None:
        return True
    else:
        return False

# Пример использования функции authenticate_user
login = input("Введите логин: ")
password = input("Введите пароль: ")

if authenticate_user(login, password):
    print("Вход выполнен успешно")
    # Здесь можно добавить код для перехода на страницу профиля и доступа к магазину мерча
else:
    print("Неверный логин или пароль")