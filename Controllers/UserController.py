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

    @classmethod
    def delete(cls, id):
        # Удалить пользователя по - id
        User.delete_by_id(id)


if __name__ == "__main__":
    UserController.add(
        name="Виктор Петров",
        email="maria@yandex.ru",
        age=30,
        registration_date= "2024-02-20"
    )
    UserController.update(2,'Александра Петрова')
    for item in UserController.get():
        print(item.name, item.name)

    print(UserController.search_email("maria@yandex.ru"))
    # UserController.delete(2)

