import pygame                 # Імпортуємо бібліотеку pygame для створення гри
from my_class import *       # Імпортуємо всі класи з файлу my_class (наприклад Button)
import json                           # Імпортуємо модуль для роботи з json файлами

game_part ="menu"
pygame.init()                # Запускаємо всі модулі pygame

WIDTH, HEIGHT = 500, 500    # Створюємо змінні ширини і висоти вікна
list_complexity = ["Easy", "Medium", "Hard"] # Список можливих рівнів складності

# Відкриваємо файл налаштувань
with open("settings.json", "r") as settings:
    data = json.loads(settings)
    current_complexity = data["complexity"]# Зчитуємо поточну складність із файлу

index = 0                                          # Індекс для перемикання складності
window = pygame.display.set_mode((WIDTH, HEIGHT))  # Створюємо ігрове вікно
clock = pygame.time.Clock()                        # Створюємо таймер для контролю FPS


# ---------- ФУНКЦІЇ ДЛЯ КНОПОК ----------

def start_game():
    global game_part
    game_part = "game"
           # Використовуємо глобальну змінну стану гри
           # Перемикаємо сцену на гру


def exit_game():
    global game_part
    game_part = "exit"             # Функція виходу з гри
           # Отримуємо доступ до глобальної змінної
          # Перемикаємо сцену на вихід


def choice_complexity():
    global index, current_complexity   # Функція зміни складності
    index += 1
    if index >= len(list_complexity):
        index = 0
    current_complexity = list_complexity[index]
    complexity.add_text(text=f"Difficulty: {current_complexity}")   # Використовуємо глобальні змінні
    data = {"complexity": current_complexity}
    with open("settings.json", "w") as settings:
        json.dumps(data,settings)   # Переходимо до наступної складності
     # Якщо дійшли до кінця списку
       # Починаємо знову з першого елемента
     # Записуємо нову складність
    # Оновлюємо текст кнопки
    # Записуємо нову складність у файл
    



# ---------- СТВОРЕННЯ КНОПОК ----------

# Текст з поточною складністю
complexity = Button(x=100, y=150, w=300, h=60, color=(100, 100, 0),
                     color_text=(0, 0, 0), text=f"Difficulty: {current_complexity}", command=None)

# Кнопка старту гри
btn_play = Button(x=100, y=200, w=300, h=60, color=(100, 100, 0),
                   color_text=(0, 0, 0), text="Play", command=start_game)
# Кнопка зміни складності
btn_complexity = Button(x=100, y=250, w=300, h=60, color=(100, 100, 0),
                         color_text=(0, 0, 0), text="Choose complexity", command=choice_complexity)
# Кнопка виходу
btn_exit = Button(x=100, y=300, w=300, h=60, color=(100, 100, 0),
                   color_text=(0, 0, 0), text="Leave", command=exit_game)


# ---------- ЕКРАНИ ГРИ ----------

# Напис GAME
game = Button(x=250, y=200, w=300, h=60, color=(100, 100, 0),
               color_text=(0, 0, 0), text="GAME", command=None)

# Напис EXIT GAME
buy_game = Button(x=250, y=20, w=300, h=60, color=(100, 100, 0),
                   color_text=(0, 0, 0), text="Donate, pls", command=None)


run = True          # Змінна роботи головного циклу
game_part = "menu"  # Поточна сцена гри
exit_timer = 0      # Таймер для затримки виходу


# ---------- ГОЛОВНИЙ ЦИКЛ ГРИ ----------
while run:

    window.fill((0,0,155))  # Очищаємо екран і заливаємо кольором

    # ---------- МЕНЮ ----------
    if game_part=="menu":

        complexity.draw(window)
        btn_play.draw(window)
        btn_exit.draw(window)
                 # Малюємо текст складності

               # Малюємо кнопку
               # Перевіряємо чи її натиснули

         # Малюємо кнопку
          # Перевіряємо натискання

                # Малюємо кнопку
               # Перевіряємо натискання


    # ---------- ГРА ----------
    elif game_part == "game":
               # Малюємо напис GAME
        game.draw(window)

    # ---------- ВИХІД ----------
    elif game_part =="exit":
        buy_game.draw(window)
                # Малюємо напис EXIT

                    # Збільшуємо таймер

               # Через 50 кадрів
                     # Завершуємо програму


    # ---------- ПОДІЇ ----------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Якщо натиснули хрестик
            run = False                # Закриваємо програму


    clock.tick(60)           # Обмежуємо FPS до 60
    pygame.display.flip()    # Оновлюємо екран