import random

import pygame as pg

# Инициализация pg
pg.init()

# Размеры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 550

DOG_WIDTH = 310
DOG_HEIGHT = 500

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 60

FOOD_SIZE = 200

DOG_Y = 100

MENU_NAV_XPAD = 90
MENU_NAV_YPAD = 130

ICON_SIZE = 80
PADDING = 5

font = pg.font.Font(None, 40)
mini_font = pg.font.Font(None, 15)


def load_image(file, width, height):
    image = pg.image.load(file).convert_alpha()
    image = pg.transform.scale(image, (width, height))
    return image


def text_render(text):
    return font.render(str(text) , True , "black")



class Item:
    def __init__(self , name , price , file):
        self.name = name
        self.price = price
        self.is_bought = False
        self.is_using = False

        self.image = load_image(file , DOG_WIDTH // 1.7 , DOG_HEIGHT // 1.7)
        self.full_image = load_image(file , DOG_WIDTH , DOG_HEIGHT)

class Clothes_menu:
    def __init__(self , game):
        self.game = game
        self.menu_page = load_image("images/menu/menu_page.png" , SCREEN_WIDTH , SCREEN_HEIGHT)

        self.bottom_label_off = load_image("images/menu/bottom_label_off.png", SCREEN_WIDTH , SCREEN_HEIGHT)
        self.bottom_label_on = load_image("images/menu/bottom_label_on.png", SCREEN_WIDTH , SCREEN_HEIGHT)
        self.top_label_off = load_image("images/menu/top_label_off.png", SCREEN_WIDTH , SCREEN_HEIGHT)
        self.top_label_on = load_image("images/menu/top_label_on.png", SCREEN_WIDTH , SCREEN_HEIGHT)

        self.items = [Item("Синяя вутболка" , 10 , "images/Items/blue t-shirt.png"),
                      Item("Ботинки" , 50 , "images/items/boots.png"),
                      Item("Шляпа" , 50 , "images/items/hat.png")]

        self.current_item = 0

        self.item_rect = self.items[0].image.get_rect()
        self.item_rect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2)

        self.next_button = Button("Вперёд" , SCREEN_WIDTH - MENU_NAV_XPAD - BUTTON_WIDTH , SCREEN_HEIGHT - MENU_NAV_YPAD,
                                 width = BUTTON_WIDTH // 1.2 , height= BUTTON_HEIGHT // 1.2 , func= self.to_next )
    def to_next(self):
        if  self.current_item != len(self.items) - 1 :
            self.current_item += 1

    def is_clicked(self , event):
        self.next_button.is_clicked(event)

    def draw(self , screen):
        screen.blit(self.menu_page , (0 , 0))

        screen.blit(self.items[self.current_item] , self.item_rect)

        if self.items[self.current_item].is_bought :
            screen.blit(self.bottom_label_on , (0 , 0))
        else:
            screen.blit(self.bottom_label_off , (0 , 0))

        if self.items[self.current_item.is_using]  :
            screen.blit(self.bottom_label_on , (0 , 0))
        else:
            screen.blit(self.top_label_off , (0 , 0))

        self.next_button.draw(screen)

    def update(self):
        self.next_button.update()


class Food:
    def __init__(self , name , image , price , satiety , medicine_power = 0):
        self.name = name
        self.image = load_image(image, FOOD_SIZE, FOOD_SIZE)
        self.price = price
        self.satiety = satiety
        self.medicine_power = medicine_power


class Food_menu:
    def __init__(self , game):
        self.game = game
        self.menu_page = load_image("images/menu/menu_page.png" , SCREEN_WIDTH , SCREEN_HEIGHT)

        self.bottom_label_off = load_image("images/menu/bottom_label_off.png", SCREEN_WIDTH , SCREEN_HEIGHT)
        self.bottom_label_on = load_image("images/menu/bottom_label_on.png", SCREEN_WIDTH , SCREEN_HEIGHT)
        self.top_label_off = load_image("images/menu/top_label_off.png", SCREEN_WIDTH , SCREEN_HEIGHT)
        self.top_label_on = load_image("images/menu/top_label_on.png", SCREEN_WIDTH , SCREEN_HEIGHT)

        self.items = [Food("Мясо", 30, "images/food/meat.png", 10),

                      Food("Корм", 40, "images/food/dog food.png", 15),

                      Food("Элитный корм", 100, "images/food/dog food elite.png", 25, medicine_power=2),

                      Food("Лекарство", 200, "images/food/medicine.png", 0, medicine_power=10)]

        self.current_item = 0

        self.item_rect = self.items[0].image.get_rect()
        self.item_rect.center = (SCREEN_WIDTH // 2 , SCREEN_HEIGHT // 2)

        self.next_button = Button("Вперёд" , SCREEN_WIDTH - MENU_NAV_XPAD - BUTTON_WIDTH , SCREEN_HEIGHT - MENU_NAV_YPAD,
                                 width = BUTTON_WIDTH // 1.2 , height= BUTTON_HEIGHT // 1.2 , func= self.to_next )
    def to_next(self):
        if  self.current_item != len(self.items) - 1 :
            self.current_item += 1

    def is_clicked(self , event):
        self.next_button.is_clicked(event)

    def draw(self , screen):
        screen.blit(self.menu_page , (0 , 0))

        screen.blit(self.items[self.current_item] , self.item_rect)

        if self.items[self.current_item].is_bought :
            screen.blit(self.bottom_label_on , (0 , 0))
        else:
            screen.blit(self.bottom_label_off , (0 , 0))

        if self.items[self.current_item.is_using]  :
            screen.blit(self.bottom_label_on , (0 , 0))
        else:
            screen.blit(self.top_label_off , (0 , 0))

        self.next_button.draw(screen)

    def update(self):
        self.next_button.update()




























class Button:
    def __init__(self, text, x, y , width  =  BUTTON_WIDTH , height  =   BUTTON_HEIGHT , text_font = font , func = None  ):
        self.func = func
        self.idle_image = load_image("images/button.png", width , height)
        self.pressed_image = load_image("images/button_clicked.png", width, height)
        self.font = text_font
        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.is_pressed = False
        self.text = self.font.render(str(text) , True , "black")
        self.text_rect = self.text.get_rect(center = self.rect.center)

    def draw(self , screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if self.is_pressed:
                self.image = self.pressed_image
            else:
                self.image = self.idle_image

    def is_clicked(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.is_pressed =True
                self.func()
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.is_pressed = False
class Game:
    def __init__(self):

        # Создание окна
        self.food_menu = Food_menu(self)
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Виртуальный питомец")

        self.happiness = 100
        self.satiety = 100
        self.health = 100
        self.money = 100



        self.coins_per_second = 1
        self.costs_of_upgrade = {100:False , 1000:False , 5000:False , 10000:False   }


        self.mode = "main"
        self.background = load_image("images/background.png", SCREEN_WIDTH, SCREEN_HEIGHT)
        self.happiness_image = load_image("images/happiness.png", ICON_SIZE, ICON_SIZE)
        self.satiety_image = load_image("images/satiety.png", ICON_SIZE, ICON_SIZE)
        self.health_image = load_image("images/health.png", ICON_SIZE, ICON_SIZE)
        self.money_image = load_image("images/money.png", ICON_SIZE, ICON_SIZE)
        self.dog_image = load_image("images/dog.png", 250 , 400)

        button_x = SCREEN_WIDTH - BUTTON_WIDTH - PADDING

        self.eat_button = Button("ЕДА", button_x, PADDING + ICON_SIZE, func = self.food_menu_on)
        self.clothes_button = Button("ОДЕЖДА", button_x, PADDING * 2 + ICON_SIZE + BUTTON_HEIGHT , func= self.clothes_menu_on)
        self.play_button = Button("ИГРЫ", button_x, PADDING * 3 + ICON_SIZE + BUTTON_HEIGHT * 2)
        self.upgrade_button = Button("УЛУЧШЕНИЕ", SCREEN_WIDTH - ICON_SIZE,0 ,
                                     width=BUTTON_WIDTH // 3, height=BUTTON_HEIGHT // 3, text_font=mini_font,
                                     func=self.increase_money)

        self.buttons = [self.eat_button , self.clothes_button , self.play_button , self.upgrade_button]

        self.INCREASE_COINS = pg.USEREVENT + 1
        pg.time.set_timer(self.INCREASE_COINS, 1000)

        self.DECREASE = pg.USEREVENT + 2
        pg.time.set_timer(self.DECREASE, 1000)

        self.clothes_menu = Clothes_menu(self)



        self.run()



    def food_menu_on(self):
        self.mode = "Food_menu"
        
        
        
    
    
    
    def clothes_menu_on(self):
        self.mode = "Clothes_menu"


    def increase_money(self):
        for cost , check , in self.costs_of_upgrade.items()  :
            if not check and self.money >= cost:
                self.coins_per_second += 1
                self.money -= cost
                self.costs_of_upgrade[cost] = True
                break
    def run(self):
        while True:
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()


            if event.type== pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.mode = "Main"
            
            
            if event.type == self.INCREASE_COINS:
                self.money += self.coins_per_second

     
            
            
            if event.type == self.DECREASE:
                chance = random.randint(1 , 10)
                if chance <= 5:
                    self.satiety -= 1
                elif 5 < chance <= 9:
                    self.happiness -= 1
                else:
                    self.health -= 1

                

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1  :
                self.money += self.coins_per_second

            for button in self.buttons:
                button.is_clicked(event)
                
            if self.mode != "Main":
                self.clothes_menu.is_clicked(event)
                self.food_menu.is_clicked(event)
                
                
                
    def update(self):
        for button in self.buttons:
            button.update()
        self.clothes_menu.update()   
        self.food_menu.update()
        
    def draw(self):
        self.screen.blit(self.background, (0, 0))
        
        self.screen.blit(self.happiness_image, (PADDING, PADDING))
        self.screen.blit(self.satiety_image, (PADDING, PADDING * 2 + ICON_SIZE))
        self.screen.blit(self.health_image, (PADDING, PADDING * 3 + ICON_SIZE * 2))
        self.screen.blit(self.money_image, (ICON_SIZE * 10.19, PADDING))
        self.screen.blit(self.dog_image, (315 , 100))
        self.screen.blit(text_render (self.happiness), (PADDING + ICON_SIZE, PADDING * 8))
        self.screen.blit(text_render (self.satiety), (PADDING + ICON_SIZE, PADDING * 8 + ICON_SIZE ))
        self.screen.blit(text_render (self.health), (PADDING + ICON_SIZE, PADDING * 8 + ICON_SIZE * 2))
        self.screen.blit(text_render (self.money), ( ICON_SIZE * 10.12 , PADDING * 7))

        for button in self.buttons:
            button.draw(self.screen)
        
        self.screen.blit(self.body, (SCREEN_WIDTH // 2 - DOG_WIDTH // 2, DOG_Y))
        
        for item in  self.clothes_menu.items:
            if item.is_using:
                self.screen.blit(item.full_image, (SCREEN_WIDTH // 2 - DOG_WIDTH // 2 , DOG_Y))
            
        if self.mode == "Clothes menu"  :  
            self.clothes_menu.draw(self.screen)
        
        if self.mode == "Food menu"  :  
            self.food_menu.draw(self.screen)
        
        
        
        
        pg.display.flip()



if __name__ == "__main__":
    Game()