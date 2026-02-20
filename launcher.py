from random import randint,choice # Імпортуємо випадкові числа для позицій та швидкостей
from customtkinter import CTk, CTkLabel,CTkButton,CTkEntry,CTkCanvas,CTkImage   # Імпортуємо CustomTkinter
from PIL import Image  # Імпортуємо PIL для роботи з зображеннями

# Клас, який описує одне коло (бульбашку) на Canvas
class Cicrle:
    def __init__(self, canvas):
        self.x0 = randint(0,700) # Випадкова початкова X координата верхнього лівого кута
        self.y0 =  randint(0,700) # Випадкова початкова Y координата верхнього лівого кута
        self.radius = randint(10,40)  # Випадковий радіус кола
        self.x1 = self.x0 + 2 * self.radius  # Правая межа кола (x0 + діаметр)
        self.y1 = self.y0 + 2 * self.radius  # Нижня межа кола (y0 + діаметр)
        self.dx = choice([-5,-4,-3,3,4,5])  # Випадкова швидкість по X вибрати серед [-5, -4, -3, 3, 4, 5]
        self.dy = choice([-5,-4,-3,3,4,5])  # Випадкова швидкість по Y
        self.color = "#{:06x}".format(randint(0, 0xFFFFFF))  # Випадковий колір кола у HEX
        self.id = canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill=self.color)  # Створюємо коло на Canvas - передати координати верхньої та нижньої межі, колір
        self.canvas = canvas # Зберігаємо посилання на Canvas для подальшого руху

    # Метод для руху кола
    def move(self): 
        # Перевірка відбиття від стін по горизонталі
        if  self.x0 < 0 or self.x1 > 700:
            self.dx *= -1
              # Змінюємо напрямок по X
        # Перевірка відбиття від стін по вертикалі
        if self.y0 < 0 or self.y1 > 700:
            self.dy *= -1
              # Змінюємо напрямок по Y
        # Оновлюємо координати кола
        self.x0 += self.dx
        self.y0 += self.dy
        self.x1 += self.dx
        self.y1 += self.dy
        self.canvas.move(self.id, self.dx,self.dy)  # Переміщуємо коло на Canvas, пердайємо айді та напрямок по х та у

# Основний клас вікна Launcher успадковує стандартне вікно 
class Launcher(CTk):
    def __init__(self):
          # Ініціалізуємо батьківський клас CTk
        super().__init__()
        self.geometry("500x500") # Встановлюємо розмір вікна
        self.title("Agario")  # Встановлюємо заголовок вікна
        self.iconbitmap("icon.ico")  # Встановлюємо іконку вікна

        # Створюємо Canvas для фону та анімації кол
        self.fon = CTkCanvas(self, width=500, height=500, bg = "#090e62", highlightthickness=0)
        self.fon.place(x=0,y=0)# Розтягуємо Canvas на весь простір вікна

        # Створюємо список кол (бульбашок) для анімації
        self.circles = [Cicrle(self.fon) for i in range(30)] 
        self.update_circles()  # Запускаємо метод анімації кол

    # Метод для оновлення позицій всіх кол (анімовані бульбашки)
    def update_circles(self):
        for circle in self.circles:
            circle.move()
              # Проходимо по всіх колах
              # Рухаємо коло відповідно до dx/dy та відбиваємо від країв
        self.after(15, self.update_circles)  # Викликаємо цей метод повторно через 15 мс (~60 FPS)

    # Метод для відображення стартового вікна
    def window_start(self):
        # Додаємо картинки по обидва боки назви
        img1 = CTkLabel(self.fon,text="",image=CTkImage(Image.open("flash.png"),size = (30,30)))
        img2 = CTkLabel(self.fon,text="",image=CTkImage(Image.open("flash.png"),size = (30,30)))
        img1.place(x=50,y=100)
        img2.place(x=200,y=100)
        # Додаємо заголовок гри
        lbl = CTkLabel(self.fon,text="Agario",text_color="#24CDDA",font=("Arial",18))
        lbl.place(x=100,y=100)
        # Поле для введення ніка
        self.nick_entry = CTkEntry(self.fon,placeholder_text="Введіть ваш нікнейм",text_color="#2E61EE",
                                   corner_radius=20,width=100,height=40,fg_color="#2CE4CB")
        self.nick_entry.place(x=100,y=200)
        # Поле для введення IP сервера
        self.ip_entry = CTkEntry(self.fon,placeholder_text="Введіть ip сервера",text_color="#4D73EE",
                                   corner_radius=20,width=100,height=40,fg_color="#2CE4CB")
        self.ip_entry.place(x=100,y=250)
        # Поле для введення порту
        self.port_entry = CTkEntry(self.fon,placeholder_text="Введіть порт сервера",text_color="#2E61EE",
                                   corner_radius=20,width=100,height=40)
        self.port_entry.place(x=100,y=300)

        # Кнопка старту гри
        start_btn = CTkButton(self.fon,text="start game",fg_color="#3ADA3A"
                              ,text_color="#6BC4FF",command=self.start_game)
        start_btn.place(x=100,y=400)

        self.end = False
        self.restart = False

        self.mainloop()  # Запускаємо головний цикл Tkinter

    # Метод для відображення кінця гри
    def window_end(self):
        # Додаємо картинки по обидва боки назви
        img1 = CTkLabel(self.fon,text="",image=CTkImage(Image.open("flash.png"),size = (30,30)))
        img2 = CTkLabel(self.fon,text="",image=CTkImage(Image.open("flash.png"),size = (30,30)))
        img1.place(x=50,y=100)
        img2.place(x=200,y=100)
        # Додаємо заголовок гри
        lbl = CTkLabel(self.fon,text="Agario",text_color="#24CDDA",font=("Arial",18))
        lbl.place(x=100,y=100)

        # Повідомлення про завершення гри
        lbl2 = CTkLabel(self.fon,text="Ви програли",text_color="#24CDDA",font=("Arial",18))
        lbl2.place(x=100,y=150)
        lbl3 = CTkLabel(self.fon,text="Чи хочите зіграти ще раз",text_color="#24CDDA",font=("Arial",18))
        lbl3.place(x=100,y=200)
        # Кнопка "Yes" для перезапуску гри
        yes_btn = CTkButton(self.fon,text="Так",fg_color="#3ADA3A"
                              ,text_color="#6BC4FF",command=self.restart_game)
        yes_btn.place(x=100,y=300)
        # Кнопка "No" для виходу з гри
        no_btn = CTkButton(self.fon,text="Ні",fg_color="#3ADA3A"
                              ,text_color="#6BC4FF",command=self.game_over)
        no_btn.place(x=170,y=300)

        self.mainloop()  # Запускаємо головний цикл Tkinter

    # Метод для перезапуску гри
    def restart_game(self):
        self.destroy() # Закриваємо поточне вікно
        self.restart = True  # Позначка для перезапуску гри
    
    # Метод для завершення гри
    def game_over(self):
        self.destroy()  # Закриваємо вікно
        self.end = True # Позначка, що гра завершена

    # Метод для обробки старту гри
    def start_game(self):
        self.nick = self.nick_entry.get() # Зчитуємо нік гравця
        self.ip = self.ip_entry.get()     # Зчитуємо IP
        self.port = self.port_entry.get()  # Зчитуємо порт
        if self.nick and self.ip and self.port:  # Перевірка, чи всі поля заповнені
            self.destroy  # Закриваємо стартове вікно
        else:  # Якщо є незаповнені поля
            error_lbl = CTkLabel(self.fon,text="Заповніть усі поля",text_color="#24CDDA",font=("Arial",18))
            error_lbl.place(x=100,y=250) # Виводимо повідомлення про помилку

    
