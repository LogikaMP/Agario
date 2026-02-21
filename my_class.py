import pygame
from random import randint
class Sprite:
    def __init__(self,x=10,y=10,w=50,h=50,speed=0,image=None,color=(200,0,0)):
            self.image = image
            self.color = color
            self.rect = pygame.Rect(x,y,w,h)
            self.speed = speed
            self.load_img()
    def draw(self,window):
         if self.image:
              window.blit(self.image,self.rect)
         else:
              pygame.draw.rect(window,self.color,self.rect)
    def move(self,window):
         key = pygame.key.get_pressed()
         if key[pygame.K_w] and self.rect.y >= self.speed:
              self.rect.y -= self.speed
         if key[pygame.K_s] and self.rect.bottom <= window.get_height() - self.speed:
              self.rect.y += self.speed
         if key[pygame.K_a] and self.rect.x >= self.speed:
              self.rect.x -= self.speed
         if key[pygame.K_d] and self.rect.right <= window.get_wigth() - self.speed:
              self.rect.x += self.speed
    def load_img(self):
         if self.image:
              self.image = pygame.image.load(self.image)
              self.image = pygame.transform.scale(self.image,(self.rect.w, self.rect.h))

class Circle(Sprite):
    def __init__(self, x = 100, y = 100, radius= 50, 
                 speed = 0, color = (0,0,130)):
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.speed = speed
        self.color = color

    def draw(self, surface):
        #pygame.draw.rect(surface, (0,0,0), self.rect, width=5)
        pygame.draw.circle(surface, self.color, self.rect.center, self.radius)

class Player(Circle):
      def __init__(self, x=100, y=100, radius=50, speed=0, color=(0, 0, 130), nickname= "player"):
           super().__init__(x, y, radius, speed, color)
           self.move_x = 0
           self.move_y = 0
           self.font = pygame.font.Font(None, 16)
           self.nick = self.font.render(nickname,True,(0,0,0))
      def move(self):
           self.move_x = 0
           self.move_y = 0
           key = pygame.key.get_pressed()
           if key[pygame.K_w]:
                self.move_y = -self.speed
           if key[pygame.K_s]:
                self.move_y = self.speed
           if key[pygame.K_a]:
                self.move_x = -self.speed
           if key[pygame.K_d]:
                self.move_x = self.speed     

      def draw(self, window):
           super().draw(window)
           window.blit(self.nick,(self.rect.x, self.rect.y-8))

      def grow(self, radius):
          self.radius += radius
          self.rect.w = self.radius*2
          self.rect.h = self.radius*2
          self.rect.center = (self.rect.x + self.rect.w//2, self.rect.y + self.rect.h//2)

class Food(Circle):
     def __init__(self):
          x = randint(-5000,500)
          y = randint(-5000,500)
          radius = randint(2,5)
          speed = 0
          color = (randint(0,255),randint(0,255),randint(0,255))
          super().__init__(x, y, radius, speed, color)

     def update(self,player):
          self.rect.x -= player.move_x
          self.rect.y -= player.move_y

     def eat_me(self,player):
         if self.rect.colliderect(player.rect):
              player.grow(self.radius)
              return True
         else:
              return False
              
class Button():  # Створюємо клас кнопки, який наслідує властивості класу Sprite
     
     def __init__  
          # Конструктор класу. Виконується при створенні об'єкта кнопки

          # Викликаємо конструктор батьківського класу Sprite і передаємо координати, розміри та колір
          self.color_text 
          # Зберігаємо колір тексту кнопки
          self.command 
          # Зберігаємо функцію, яка виконається при натисканні кнопки
          self.  
          # Викликаємо метод створення тексту на кнопці
          self.was_pressed  
          # Прапорець, що показує чи була кнопка натиснута раніше


     def add_text(self, text):  
          # Метод створення та розміщення тексту на кнопці

          # h = 0.45, w = 0.55 (коефіцієнти підбору розміру шрифту)
          size_h = 
          # Розраховуємо розмір шрифту від висоти кнопки
          size_w = 
          # Розраховуємо розмір шрифту від ширини кнопки та довжини тексту
          font_size = 
          # Обираємо менше значення, щоб текст точно помістився
          font = 
          # Створюємо шрифт потрібного розміру
          self.text =  
          # Створюємо зображення тексту
          self.text_x =  
          # Обчислюємо координату X для центрування тексту по горизонталі
          self.text_y = 
          # Обчислюємо координату Y для центрування тексту по вертикалі


     def draw(self, surface):  
          # Метод відмалювання кнопки на екрані

          # Малюємо саму кнопку через метод батьківського класу

          # Малюємо текст поверх кнопки


     def is_clicked(self):  
          # Метод перевіряє чи натиснута кнопка

          if   
               # Перевіряємо чи є функція для виконання
               click =
               # Перевіряємо чи натиснута ліва кнопка миші
               pos = 
               # Отримуємо поточну позицію курсора
               if  
                    # Якщо кнопка миші натиснута, курсор знаходиться на кнопці
                    # і попередній стан не був натисканням
                    self.
                    # Виконуємо функцію кнопки
               self. 
               # Запам’ятовуємо стан кнопки миші, щоб не викликати функцію багато разів