import pygame                 # Імпортуємо бібліотеку pygame для створення гри
from my_class import *       # Імпортуємо всі класи з файлу my_class (наприклад Button)
import json                           # Імпортуємо модуль для роботи з json файлами

pygame.init()                # Запускаємо всі модулі pygame

WIDTH, HEIGHT = 500, 500    # Створюємо змінні ширини і висоти вікна
list_complexity = ["Easy", "Medium", "Hard"] # Список можливих рівнів складності

# Відкриваємо файл налаштувань
with open("setting.json","r") as f:
    data = json.loads(f)    
    current_complexty = data["complexty"]  # Зчитуємо поточну складність із файлу

index = 0                                          # Індекс для перемикання складності
window = pygame.display.set_mode((WIDTH, HEIGHT))  # Створюємо ігрове вікно
clock = pygame.time.Clock()                        # Створюємо таймер для контролю FPS


# ---------- ФУНКЦІЇ ДЛЯ КНОПОК ----------

def start_game():            # Функція запуску гри
           # Використовуємо глобальну змінну стану гри
           # Перемикаємо сцену на гру
    global game_part
    game_part = "game"

def exit_game():             # Функція виходу з гри
           # Отримуємо доступ до глобальної змінної
          # Перемикаємо сцену на вихід
    global game_part
    game_part = "exit"

def choice_complexity():     # Функція зміни складності
       # Використовуємо глобальні змінні
       # Переходимо до наступної складності
     # Якщо дійшли до кінця списку
       # Починаємо знову з першого елемента
     # Записуємо нову складність
    # Оновлюємо текст кнопки
    # Записуємо нову складність у файл
    global index, current_complexty
    index +=1
    if index >= len(list_complexity):
        index = 0
    current_complexty = list_complexity[index]
    complexity.add_text(f"complexty:{current_complexty}")
    data = {"complexty":current_complexty}
    with open("setting.json","w") as f:
        json.dump(data,f)



# ---------- СТВОРЕННЯ КНОПОК ----------

# Текст з поточною складністю
complexity = Button(x = 100, y = 100, w = 300, h = 50, color=(0,0,155),
                    color_text=(200,200,200), text=f"complexty:{current_complexty}", command=None)

# Кнопка старту гри
btn_play = Button(x = 100, y = 200, w = 300, h = 50, color=(200,0,0),
                    color_text=(200,200,200), text="Play", command=start_game)
# Кнопка зміни складності
btn_complaxity = Button(x = 100, y = 300, w = 300, h = 50, color=(0,155,0), 
                        color_text=(200,200,200), text="complexty", command=choice_complexity)
# Кнопка виходу
btn_exit = Button (x = 100, y = 400, w = 300, h = 50, color=(200,0,0),
                   color_text=(200,200,200), text="Exit", command=exit_game)


# ---------- ЕКРАНИ ГРИ ----------

# Напис GAME
game = Button(x = 100, y = 200, w = 200, h = 50, color=(200,0,0),
              color_text=(200,200,200), text="Game",command=None)

# Напис EXIT GAME
buy_game = Button(x = 100, y = 300, w = 200, h = 50, color=(200,0,0),
                  color_text=(200,200,200),text="Buy",command=None)


run = True          # Змінна роботи головного циклу
game_part = "menu"  # Поточна сцена гри
exit_timer = 0      # Таймер для затримки виходу


# ---------- ГОЛОВНИЙ ЦИКЛ ГРИ ----------
while run:

    window.fill((0,0,155))  # Очищаємо екран і заливаємо кольором

    # ---------- МЕНЮ ----------
    if game_part=="menu":
        
             # Малюємо текст складності
        complexity.draw(window)
               # Малюємо кнопку
               # Перевіряємо чи її натиснули
        btn_play.draw(window)
        btn_play.is_clicked()
         # Малюємо кнопку
          # Перевіряємо натискання
        btn_complaxity.draw(window)
        btn_complaxity.is_clicked()
                # Малюємо кнопку
               # Перевіряємо натискання
        btn_exit.draw(window)
        btn_exit.is_clicked()

    # ---------- ГРА ----------
    elif game_part == "game":
               # Малюємо напис GAME
        game.draw(window)

    # ---------- ВИХІД ----------
    elif game_part =="exit":

                # Малюємо напис EXIT
        buy_game.draw(window)
                    # Збільшуємо таймер

               # Через 50 кадрів
                     # Завершуємо програму


    # ---------- ПОДІЇ ----------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:  # Якщо натиснули хрестик
            run = False                # Закриваємо програму


    clock.tick(60)           # Обмежуємо FPS до 60
    pygame.display.flip()    # Оновлюємо екран