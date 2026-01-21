from Models.Base import *

class User(BaseModel):
    '''
    Данный класс описывает таблицу в БД с пользователями
    '''
    id  = PrimaryKeyField()
    name = CharField(unique=True) # Имя
    email = CharField() # Эдектронная почта
    age = IntegerField() # Возраст
    registration_date = DateField() # Дата регистрации

if __name__ == "__main__":
    mysql_db.create_tables([User])

