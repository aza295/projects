# 1) Дан список в котором хранится строка. Разрежьте его на две равные части (если длина строки нечетная, то длина первой части должна быть на один символ больше). Переставьте эти две части местами, при этом каждый символ должен являться отдельной строкой, результат запишите в новый список и выведите на экран.
# """
# # писать код здесь
# """
# 2) Дан список, состоящий ровно из двух строк. Переставьте эти слова местами. Результат запишите в список и выведите получившийся результат.
# """
# # писать код здесь
# """
# 3) Даны два множества. С помощью определенного метода (оператора) найдите пересечение множеств:
# """
# # писать код здесь
# """
# 4) Четверо коллег собрались на обед. Но они не могут решить, где им пообедать, так как у каждого свои вкусовые предпочтения. Помогите найти им выход в данной ситуации. Данные:

# -Тилек хочет покушать в Dodo или в ImperiaPizza, ну или в крайнем случае FreshBox.
# -Тимур хочет покушать шашлык в OchakKebab или рамен в FreshBox.
# -Александр очень хочет вафли с FreshBox либо KFC.
# -Элину устраивает любой из вариантов. 

# Напишите код, который сможет определить, в какое место им лучше пойти.
# """
# # писать код здесь
# """
# 5) Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.
# """
# # писать код здесь
# """
# 6) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.
# """
# # писать код здесь
# """
# 7) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.
# """
# # писать код здесь
# """
# 8) Дан словарь, значениями в котором являются другие словари. Замените внутренние словари их значениями. Например: my_dict = {'first': {'a': 1}, 'second': {'b': 2}} -> {'first': 1, 'second': 2}
# """
# # писать код здесь
# """
# 9) Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если такого ключа нет.
# """
# # писать код здесь
# """
# 10) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
# """
# # писать код здесь




# 7) Создайте словарь из чисел от 1 до 10, где ключами будут сами числа, а значениями их квадраты.

# a = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10'}
# b = [key:value for value in key value**2 in.items]




# a = {'first': {'a': 1}, 'second': {'b': 2}} 
# b = []

# 6) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.

# a = {'a':'1','b':'2','c':'3','d':'4','e':'5'}
# b = [ i for i in value + ]



# 2) Дан список, состоящий ровно из двух строк. Переставьте эти слова местами. 
# Результат запишите в список и выведите получившийся результат


# a = ['string','integer']

# b = ([2][1])


# print(b)



# 5) Создайте словарь где ключами будут фрукты, а значением их цены. Удалите те элементы, значение которых будет чётным.


# a = {'banana':'25','apple':'50','watermelon':'15'}
# for i in value:
#       if value %2 ==0:


# 10) Запросите у пользователя сумму, которая у него сейчас есть в бумажнике.
#  Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"
# # """
# # писать код здесь

# 6) Создайте словарь, где значениями будут являться числа. Найдите сумму этих значений.

# a = {'1':'a','2':'b','3':'c','4':'d','5':'e'}
# b = (for key in a if key+)

# a = {'a':'1','b':'2','c':'3','d':'4','e':'5'}
# try:
#    for i in key,value get(b)
# except KeyError:
#       print('неверный ключ')
# finally:
#     print ('thnx')

# a = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10'}
# b = [key:value for value in key value**2 in.items]
# print(b)


# 1) Дан список в котором хранится строка. Разрежьте его на две равные части
#  (если длина строки нечетная, то длина первой части должна быть на один символ больше).
#   Переставьте эти две части местами, при этом каждый символ должен являться отдельной строкой, 
#   результат запишите в новый список и выведите на экран.



# a = ['be' 'quick']
# b = [i for i in a if ]



import pygame
pygame.init()
dis=pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption('Snake game by Edureka')
game_over=False
while not game_over:
    for event in pygame.event.get():
        print(event)   #prints out all the actions that take place on the screen
 
pygame.quit()
quit()