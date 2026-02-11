from tkinter import *
from tkinter import ttk

from Controllers.UserController import UserController

class SaerchView(Tk):
    def __init__(self, search_string):
        super().__init__()

        self.search_string = search_string # Из строки поиска в окне UserView, занчение предаётся атрибуту self.search_string

        # Атрибуты окна
        self.title("Все пользователи")
        self.geometry("1280x920")

        # Фрейм для таблицы
        self.table_frame = ttk.Frame(
            self,
            padding=20
        )
        self.table_frame.pack(
            anchor=CENTER,
            fill=X,
            padx=10,
            pady=10
        )

        # Создание таблицы
        self.columns = ('id', "name", 'email', 'age', 'registration_date')  # Столбцы
        self.table_data = ttk.Treeview(self, columns=self.columns, show='headings')
        # Заголовки
        self.table_data.heading('id', text="№")
        self.table_data.heading('name', text='Имя')
        self.table_data.heading('email', text='Электронная почта')
        self.table_data.heading('age', text='Возраст')
        self.table_data.heading('registration_date', text='Дата Регестрации')

        self.elemnt = []
        for row in UserController.search_email(self.search_string):
            self.elemnt.append(
                (row.id,row.name,row.email,row.age,row.registration_date)
            )
        # Вывод данных из списка   self.elemnt в таблицу   self.table_data
        for item in self.elemnt:
            self.table_data.insert("", END,values=item)
        self.table_data.pack()


        # Кнопка закрытия окна / перехода в главное
        # переход на главное окно
        self.button_move = ttk.Button(self, text="Вернуться на главную страницу", command=self.move)
        self.button_move.pack(anchor=CENTER)

    def move(self):
        from Views.UserView import UserView
        window_home = UserView()
        self.destroy()

if __name__ == "__main__":
    window = SaerchView(search_string="")
    window.mainloop()
