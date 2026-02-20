<<<<<<< Updated upstream
from   # Імпортуємо випадкові числа для позицій та швидкостей
from   # Імпортуємо CustomTkinter
from   # Імпортуємо PIL для роботи з зображеннями
=======
from random import randint, choice  # Імпортуємо випадкові числа для позицій та швидкостей
from customtkinter import CTk, CTkButton,CTkCanvas,CTkEntry,CTkLabel,CTkImage  # Імпортуємо CustomTkinter
from PIL import Image   # Імпортуємо PIL для роботи з зображеннями
>>>>>>> Stashed changes

# Клас, який описує одне коло (бульбашку) на Canvas
class Circle:
    def __init__(self, canvas):
<<<<<<< Updated upstream
        self.x0 =   # Випадкова початкова X координата верхнього лівого кута
        self.y0 =   # Випадкова початкова Y координата верхнього лівого кута
        self.radius =   # Випадковий радіус кола
        self.x1 =   # Правая межа кола (x0 + діаметр)
        self.y1 =   # Нижня межа кола (y0 + діаметр)
        self.dx =   # Випадкова швидкість по X вибрати серед [-5, -4, -3, 3, 4, 5]
        self.dy =   # Випадкова швидкість по Y
        self.color = "#{:06x}".format(randint(0, 0xFFFFFF))  # Випадковий колір кола у HEX
        self.id = canvas.create_oval()  # Створюємо коло на Canvas - передати координати верхньої та нижньої межі, колір
        self.canvas =  # Зберігаємо посилання на Canvas для подальшого руху
=======
        self.x0 = randint(0, 500)  # Випадкова початкова X координата верхнього лівого кута
        self.y0 = randint(0, 500)  # Випадкова початкова Y координата верхнього лівого кута
        self.radius = randint(10, 50)  # Випадковий радіус кола
        self.x1 = self.x0 + self.radius + self.radius  # Правая межа кола (x0 + діаметр)
        self.y1 = self.y0 + self.radius + self.radius  # Нижня межа кола (y0 + діаметр)
        self.dx = choice([-5,-4,-3,3,4,5])  # Випадкова швидкість по X вибрати серед [-5, -4, -3, 3, 4, 5]
        self.dy = choice([-5,-4,-3,3,4,5])  # Випадкова швидкість по Y
        self.color = "#{:06x}".format(randint(0, 0xFFFFFF))  # Випадковий колір кола у HEX
        self.id = canvas.create_oval(self.x0, self.y0, self.x1,self.y1, fill = self.color)  # Створюємо коло на Canvas - передати координати верхньої та нижньої межі, колір
        self.canvas = canvas # Зберігаємо посилання на Canvas для подальшого руху
>>>>>>> Stashed changes

    # Метод для руху кола
    def move(self): 
        # Перевірка відбиття від стін по горизонталі
<<<<<<< Updated upstream
        if 
              # Змінюємо напрямок по X
        # Перевірка відбиття від стін по вертикалі
        if 
=======
        if self.x0 < 0 or self.x1 > 700:
            self.dx *= -1 # Змінюємо напрямок по X
        # Перевірка відбиття від стін по вертикалі
        if self.y0 < 0 or self.y1 > 700:
            self.dy *= -1
>>>>>>> Stashed changes
              # Змінюємо напрямок по Y
        # Оновлюємо координати кола
        self.x0 
        self.y0 
        self.x1 
        self.y1 
        self.canvas.move()  # Переміщуємо коло на Canvas, пердайємо айді та напрямок по х та у

# Основний клас вікна Launcher успадковує стандартне вікно 
<<<<<<< Updated upstream
class Launcher():
    def __init__(self):
          # Ініціалізуємо батьківський клас CTk

        self. # Встановлюємо розмір вікна
        self.  # Встановлюємо заголовок вікна
        self.  # Встановлюємо іконку вікна

        # Створюємо Canvas для фону та анімації кол
        self.fon = CTkCanvas(self, width=500, height=500, bg = "#090e62", highlightthickness=0)
        self.fon  # Розтягуємо Canvas на весь простір вікна
=======
class Launcher(CTk):
    def __init__(self):
          # Ініціалізуємо батьківський клас CTk
        super().__init__()
        self.geometry("500x500") # Встановлюємо розмір вікна
        self.title("Agario")  # Встановлюємо заголовок вікна
        self.iconbitmap("icon.ico")  # Встановлюємо іконку вікна
        self.end = False
        self.restart = False
        # Створюємо Canvas для фону та анімації кол
        self.fon = CTkCanvas(self, width=700, height=700, bg = "#090e62", highlightthickness=0)
        self.fon.place(x=0, y=0)  # Розтягуємо Canvas на весь простір вікна
>>>>>>> Stashed changes

        # Створюємо список кол (бульбашок) для анімації
        self.circles = 
        self.update_circles()  # Запускаємо метод анімації кол

    # Метод для оновлення позицій всіх кол (анімовані бульбашки)
    def update_circles(self):
        for   # Проходимо по всіх колах
              # Рухаємо коло відповідно до dx/dy та відбиваємо від країв
        self.after(15, self.update_circles)  # Викликаємо цей метод повторно через 15 мс (~60 FPS)

    # Метод для відображення стартового вікна
    def window_start(self):
        # Додаємо картинки по обидва боки назви
<<<<<<< Updated upstream
        img1 = 
        img2 =
        img1.
        img2.
        # Додаємо заголовок гри
        lbl = 
        lbl.
        # Поле для введення ніка
        self.nick_entry =
        self.nick_entry.
        # Поле для введення IP сервера
        self.ip_entry =
        self.ip_entry.
        # Поле для введення порту
        self.port_entry = 
        self.port_entry.

        # Кнопка старту гри
        start_btn = 
        start_btn.
=======
        img1 = CTkLabel(self.fon, text="", image=CTkImage(Image.open("flash.png"), size=(30, 30)))
        img2 = CTkLabel(self.fon, text="", image=CTkImage(Image.open("flash.png"), size=(30, 30)))
        img1.place(x=50, y=100)
        img2.place(x=200, y=100)
        # Додаємо заголовок гри
        lbl = CTkLabel(self.fon, text="Agario", font=(None, 16), text_color="#ffffff")
        lbl.place(x=100, y=100)
        # Поле для введення ніка
        self.nick_entry = CTkEntry(self.fon, width=100, height=40, placeholder_text="Enter Your Nickname...", fg_color="#ffffff", text_color="#666666")
        self.nick_entry.place(x=100, y=200)
        # Поле для введення IP сервера
        self.ip_entry =  CTkEntry(self.fon, width=100, height=40, placeholder_text="Enter Server IP...", fg_color="#ffffff", text_color="#666666")
        self.ip_entry.place(x=100, y=250)
        # Поле для введення порту
        self.port_entry =  CTkEntry(self.fon, width=100, height=40, placeholder_text="Enter Server Port...", fg_color="#ffffff", text_color="#666666")
        self.port_entry.place(x=100, y=300)

        # Кнопка старту гри
        start_btn = CTkButton(self.fon, text="Launch", fg_color="#ffffff", text_color="#000000", command=self.start_game)
        start_btn.place(x=100, y=400)
>>>>>>> Stashed changes

        self.  # Запускаємо головний цикл Tkinter

    # Метод для відображення кінця гри
    def window_end(self):
        # Додаємо картинки по обидва боки назви
<<<<<<< Updated upstream
        img1 = 
        img2 = 
        img1.
        img2.
        # Заголовок гри
        lbl = 
        lbl.

        # Повідомлення про завершення гри
        lbl2 =
        lbl2.
        lbl3 = 
        lbl3.
        # Кнопка "Yes" для перезапуску гри
        yes_btn = 
        yes_btn.
        # Кнопка "No" для виходу з гри
        no_btn = 
        no_btn.
=======
        img1 = CTkLabel(self.fon, text="", image=CTkImage(Image.open("flash.png"), size=(30, 30)))
        img2 = CTkLabel(self.fon, text="", image=CTkImage(Image.open("flash.png"), size=(30, 30)))
        img1.place(x=50, y=100)
        img2.place(x=200, y=100)
        # Заголовок гри
        lbl = CTkLabel(self.fon, text="Agario", font=(None, 16), text_color="#ffffff")
        lbl.place(x=100, y=100)

        # Повідомлення про завершення гри
        lbl2 = CTkLabel(self.fon, text="Game Over", font=(None, 16), text_color="#ffffff")
        lbl2.place(x=100, y=150)
        lbl3 = CTkLabel(self.fon, text="Are you want play again?", font=(None, 16), text_color="#ffffff")
        lbl3.place(x=100, y=200)
        # Кнопка "Yes" для перезапуску гри
        yes_btn = CTkButton(self.fon, text="Yes", fg_color="#ffffff", text_color="#000000", command=self.restart_game)
        yes_btn.place(x=100, y=300)
        # Кнопка "No" для виходу з гри
        no_btn = CTkButton(self.fon, text="Yes", fg_color="#ffffff", text_color="#000000", command=self.game_over)
        no_btn.place(x=170, y=300)
>>>>>>> Stashed changes

        self.  # Запускаємо головний цикл Tkinter

    # Метод для перезапуску гри
    def restart_game(self):
        self. # Закриваємо поточне вікно
        self.  # Позначка для перезапуску гри
    
    # Метод для завершення гри
    def game_over(self):
        self.  # Закриваємо вікно
        self. # Позначка, що гра завершена

    # Метод для обробки старту гри
    def start_game(self):
        self.nick =  # Зчитуємо нік гравця
        self.ip =      # Зчитуємо IP
        self.port =   # Зчитуємо порт
        if   # Перевірка, чи всі поля заповнені
            self.  # Закриваємо стартове вікно
        else:  # Якщо є незаповнені поля
<<<<<<< Updated upstream
            error_lbl = 
            error_lbl. # Виводимо повідомлення про помилку
=======
            error_lbl = CTkLabel(self.fon, text="Please, enter the all entries", font=(None, 16), text_color="#ffffff")
            error_lbl.place(x=100, y=250) # Виводимо повідомлення про помилку
>>>>>>> Stashed changes

    
