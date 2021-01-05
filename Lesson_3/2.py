# Task 2
def user_data():
    user = {'Имя': '', 'Фамилия': '', 'Год рождения': '', 'Город проживания': '', 'e-mail': '', 'Телефон': ''}
    for key, value in user.items():
        value = input(f'Введите {key} - ')
        user[key] = value
    return user.values()


print(*user_data())
