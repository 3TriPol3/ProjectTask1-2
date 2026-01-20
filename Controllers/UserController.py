from Models.User import *

class UserController:
    '''
    методы:
       добавить,
       показать всех,
       найти по email,
       удалить.
    '''
    @classmethod
    def add(cls,name,email,age,registration_date):
        # добавить пользователя в Таблицу
        try:
            User.create(
            name = name,
            email = email,
            age = age,
            registration_date = registration_date
            )
        except:
            print("Ошибка добавления пользователя")
    @classmethod
    def get(cls):
        # Выводит список записей из таблицы БД
        return User.select()

    @classmethod
    def update(cls, id, name):
        # Обновить запись по id
        User.update({User.name:name}).where(User.id == id).execute()
    @classmethod
    def search_email(cls,email):
        # Метод выводит список записей, если встречается характеристика email
        # list = [] # создание пустого списка
        query = User.select().where(User.email == email) # переменной передаём список записей у которых в поле email есть email из аргумента метода
        # for item in query:
        #     list.append(item.name)
        return query


if __name__ == "__main__":
    UserController.add(
        name="Мария Петрова",
        email="maria@yandex.ru",
        age=30,
        registration_date= "2024-02-20"
    )
    UserController.update(2,'Warrior123')
    for item in UserController.get():
        print(item.name, item.player)

    print(UserController.search_email("урон: 150, прочность: 200"))
