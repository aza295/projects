# импорт из библиотеки pygame
import pygame
import time
import random
 
pygame.init()

#задаем параметры цвета

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
#  задаем параметры экрана и игрового поля
# ширина экрана
screen_width = 600
# высота экрана
screen_height = 400

# размер экрана
screen = pygame.display.set_mode((screen_width, screen_height))
#при помощи функции display.set_caption(),
#  мы вывели заголовок нашего экрана — ‘python 13’.
pygame.display.set_caption('python13')
 
#   частота обновления
clock = pygame.time.Clock()
 
#  параметры змеи
snake_block = 10
snake_speed = 15
 
# создаем шрифт
font_style = pygame.font.SysFont("iron pythonshift", 25)
score_font = pygame.font.SysFont("pythanos", 35)
 
# функция вывода счета
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    screen.blit(value, [0, 0])
 
 
#  функция создающяя змею
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])
 
# грубо говоря эта функция  выводит вы проиграли 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [screen_width / 6, screen_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
# Для сохранения изменений координат
#  x и y мы создали две новых переменные: 
# x1_change и y1_change.

    x1 = screen_width / 2
    y1 = screen_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            screen.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

#благодаря функции event.get() будут отображаться все действия игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                  print(event)

#Чтобы передвигать змейку, 
# мы будем использовать ключевые события из класса 
# KEYDOWN библиотеки Pygame. 
# События K_UP, K_DOWN, K_LEFT, и K_RIGHT 
# заставят змейку двигаться вверх, вниз, 
# влево и вправо соответственно. 
# Также, цвет дисплея меняется от черного 
# (по умолчанию) до белого при помощи метода fill()


                  if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                  elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                  elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                  elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
 
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 #Your_score. Это функция будет показывать размер змейки за вычетом 1 (так как это начальный размер змейки).
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
        
 #Pygame – это библиотека модулей для языка Python, созданная для разработки 2D игр. Также Pygame могут называть фреймворком.
    pygame.quit()
    quit()
 
 
gameLoop()

# gameLoop()
# Каждая игра использует игровой цикл для управления игровым процессом. 
# Игровой цикл выполняет четыре очень важных задачи:

# 1)Обрабатывает ввод данных пользователем
# 2)Обновляет состояние всех игровых объектов
# 3)Обновляет дисплей и аудиовыход
# 4)Поддерживает скорость игры







# 1) init()
# Инициализирует все модули Pygame (возвращает кортеж в случае успеха или неудачи).

# display.set_mode()
# Для создания поверхности принимает в качестве параметра либо список либо кортеж (кортеж предпочтительней).

# update()
# Обновляет экран.

# quit()
# Используется для деинициализации всех модулей.

# set_caption()
# Устанавливает текст заголовка в верхней части экрана

# event.get()
# Возвращает список всех событий.

# Surface.fill()
# Заполняет пространство сплошным цветом.

# time.Clock()
# Отслеживание времени

# font.SysFont()
# Задает шрифт Pygame, используя системные ресурсы.
      























