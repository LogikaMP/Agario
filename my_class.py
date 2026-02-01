import pygame

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
    def __init__(self, x=100, y=100, radius=50, speed=0, color=(0, 0, 130)):
          super().__init__(x, y, radius, speed, color)
          self.dx =0
          self.dy = 0
    def move(self):
          self.dx = 0
          self.dy = 0
          key = pygame.key.get_pressed()
          if key[pygame.K_w]:
               self.dy = self.speed
          if key[pygame.K_s]:
               self.dy = -self.speed
          if key[pygame.K_a]:
               self.dx = self.speed
          if key[pygame.K_d]:
               self.dx = -self.speed
         
         
class Eat(Circle):
     def check_collide(self, player):
          if self.rect.colliderect(player.rect):
               player.radius += self.radius // 5
               player.rect.w, player.rect.h = player.radius * 2, player.radius * 2
               return True
          return False


class AnimeSprite(Sprite):
    def __init__(self, x=10, y=10, w=50, h=50, images=None):
        super().__init__(x, y, w, h)
        self.current_frame = 0
        self.frames = []
        for image in images:
             self.image = image
             self.load_img()
             self.frames.append(self.image)

   

    def anime(self):
        self.current_frame += 0.1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.image = self.frames[int(self.current_frame)]

class Button:
    def __init__(self, x = 50, y = 50, w = 150, h = 80, 
                  text="Button", color=(255, 255, 255), 
                  color_text=(0,0,0), function=None):
        self.color = color
        self.color_text = color_text
        self.rect = pygame.Rect(x, y ,w, h)
        self.function = function
        self.font = pygame.font.Font(None, h)
        self.text = self.font.render(text,True, self.color_text)

    
    def draw(self, window):
        pygame.draw.rect(window, self.color,self.rect)
        pygame.draw.rect(window, self.color_text,self.rect, width=10)
        x,y  = self.text.get_width(), self.text.get_height()
        x,y = (self.rect.w - x)//2, (self.rect.h - y)//2
        x,y = self.rect.x +x, self.rect.y + y
        window.blit(self.text,(x,y))

    def click(self):
        be_click = pygame.mouse.get_pressed()[0]
        pos = pygame.mouse.get_pos()
        if be_click:
             if self.rect.collidepoint(pos):
                  self.function()