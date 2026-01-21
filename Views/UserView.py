from tkinter import *
from tkinter import ttk
from Controllers.UserController import *
# from Views.SaleItemView import SaleItemView
from Views.SearchView import SaerchView



class UserView(Tk):
    def __init__(self):
        super().__init__()

        # Атрибуты окна
        self.title("Система управления пользователями")
        self.geometry("1280x920")

        # Фрейм Добавить пользователя
        self.add_frame = ttk.Frame(self,
                                   borderwidth=1,  # ширина границы фрейма
                                   relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                   padding=[18],  # внутренние отступы фрейма
                                   )
        self.add_frame.pack(
            anchor=CENTER,  # расположение по центру
            fill=X,  # заполнение
            padx=10,  # расположение по оси x от верней левой точки окна
            pady=10,  # расположение по оси y от верней левой точки окна

        )
        # Фрайм в которм расположен текст Добавить Пользователя (находится внутри фрейма add_frame)
        self.add_title_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                         borderwidth=1,  # ширина границы фрейма
                                         padding=[8, 10])
        self.add_title_frame.pack(anchor=CENTER,  # расположение по центру
                                  fill=X,  # заполнение
                                  padx=10,  # расположение по оси x от верней левой точки окна
                                  pady=10,  # расположение по оси y от верней левой точки окна
                                  )
        self.add_title = ttk.Label(self.add_title_frame, text="Добавить Пользователя")
        self.add_title.pack()
        # Фрайм в которм расположены окна ввода данных о Пользователе (находится внутри фрейма add_frame)
        self.add_input_frame = ttk.Frame(self.add_frame,
                                         relief=SOLID,  # тип линии фрейма - СПЛОШНАЯ
                                         borderwidth=1,  # ширина границы фрейма
                                         padding=[8, 10]
                                         )
        self.add_input_frame.pack(fill=X,  # заполнение
                                  padx=10,  # расположение по оси x от верней левой точки окна
                                  pady=10,  # расположение по оси y от верней левой точки окна
                                  )
        # Окна ввода данных Пользователя для добавления в таблицу БД
        self.add_title_name = ttk.Label(self.add_input_frame, text="Имя")
        self.add_title_name.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        self.add_title_rarity = ttk.Label(self.add_input_frame, text="Электронная почта")
        self.add_title_rarity.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.add_title_player = ttk.Label(self.add_input_frame, text="Возраст")
        self.add_title_player.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)

        self.add_title_quantity = ttk.Label(self.add_input_frame, text="Дата регистрации")
        self.add_title_quantity.grid(row=0, column=3, sticky="nsew", padx=5, pady=5)


        self.add_name = ttk.Entry(self.add_input_frame)
        self.add_name.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.add_email = ttk.Entry(self.add_input_frame)
        self.add_email.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.add_age = ttk.Entry(self.add_input_frame)
        self.add_age.grid(row=1, column=2, sticky="nsew", padx=5, pady=5)

        self.add_registration_date = ttk.Entry(self.add_input_frame)
        self.add_registration_date.grid(row=1, column=3, sticky="nsew", padx=5, pady=5)


        self.add_button = ttk.Button(self.add_input_frame, text="Добавить Пользователя", command=self.add_data)
        self.add_button.grid(row=1, column=5, sticky="nsew", padx=5, pady=5)

        # Фрейм Вывод Пользователей
        self.get_data = ttk.Frame(
            self,
            relief="raised",
            borderwidth=3,
            padding=[5]
        )
        self.get_data.pack(
            anchor=CENTER
        )
        # Таблица
        self.columns = ('id', "name", 'email', 'age', 'registration_date')  # Столбцы
        self.table_data = ttk.Treeview(self.get_data, columns=self.columns, show='headings')
        # Заголовки
        self.table_data.heading('id', text="№")
        self.table_data.heading('name', text='Имя')
        self.table_data.heading('email', text='Электронная почта')
        self.table_data.heading('age', text='Возраст')
        self.table_data.heading('registration_date', text='Дата регистрации')
        # Превращает объекты из БД в список кортежей для таблицы
        self.table()
        # Фрейм для окна поиска по email
        self.search_frame = ttk.Frame(
            self,
            relief=SOLID,
            borderwidth=1,
            padding=[8, 10]
        )
        self.search_frame.pack(
            fill=X,  # заполнение
            padx=10,  # расположение по оси x от верней левой точки окна
            pady=10,
        )
        self.label_search = ttk.Label(self.search_frame, text="Найти Пользователя по email")
        self.label_search.grid(row=0)
        self.text_search = Text(self.search_frame, height=5, width=50)
        self.text_search.grid(row=1, column=0)
        self.button_search = ttk.Button(self.search_frame, text="Найти Пользователя", command=self.search)
        self.button_search.grid(row=1, column=2, padx=5, sticky="s")

        # # Кнопка перехода в окно передачи предмета
        # self.update_item = ttk.Button(self, text="Передать предмет другому игроку", command=self.all)
        # self.update_item.pack()

    # def all(self):
    #     window = SaleItemView()

    # метод передачи значения из строки ввода text_search в окно SaerchView
    def search(self):
        self.string = self.text_search.get("0.0", "end")  # передачи значения из строки ввода text_search
        self.string = self.string.strip()
        window = SaerchView(search_string=self.string)
        self.destroy()

    # Для обновления данных в таблице создал метод добавления записей из БД
    def table(self):
        # Очистить старые записи
        for item in self.table_data.get_children():
            self.table_data.delete(item)

        self.elemnt = []
        for el in UserController.get():
            self.elemnt.append(
                (el.id, el.name, el.email, el.age, el.registration_date)
            )

        # Вывод данных из БД в таблицу
        for item in self.elemnt:
            self.table_data.insert("", END, values=item)
        self.table_data.pack()

    # Методы для кнопок
    def add_data(self):
        self.name = self.add_name.get()
        self.email = self.add_email.get()
        self.age = self.add_age.get()
        self.registration_date = self.add_registration_date.get()
        UserController.add(
            self.name,
            self.email,
            self.age,
            self.registration_date
        )
        # Обновить данные таблицы Treeview
        self.table()
        # Очистить поля ввода
        self.clear()

    def clear(self):
        '''
        Метод очистит окна Treeview

        :return:
        '''
        self.add_name.delete(0, END)  # c 0-го идекса до конца
        self.add_email.delete(0, END)  # c 0-го идекса до конца
        self.add_age.delete(0, END)  # c 0-го идекса до конца
        self.add_registration_date.delete(0, END)  # c 0-го идекса до конца


if __name__ == "__main__":
    window = UserView()
    window.mainloop()