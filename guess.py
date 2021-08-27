
# Требования:
# 1. Ваша программа должна запрашивать
# имя пользователя. Программа должна
# запросить у пользователя хочет ли он
# играть или нет. Если ответ будет ‘нет’, то
# программа должна завершиться.
# 2. Далее пользователь должен угадать
# число. Также вы должны сделать счетчик
# попыток, и показать пользователю сколько
# попыток ему потребовалось, чтобы отгадать
# число.
# 3. Если пользователь угадал число,
# запросить у него хочет ли он пройти игру
# еще раз, если ответ будет “нет”, программа
# должна завершиться


# import random
# имя =input('Введите ваше имя:')
# старт=input('Хотите ли вы играть?:')
# счетчик = 0
# if старт == 'да':
#       число1 =random.randint(1,10)
#       # print (число1)
#       while True:
#             число2 = int(input('Введите число:'))
#             счетчик = счетчик +1
#             if число2 == число1:
#                   print(f'Поздравляю  вы выиграли!!!,ваше количество попыток{счетчик}')
#                   повтор=input('хотите ли пройти игру еще раз?:')
#                   if повтор == 'да':
#                               numbers = random.randint(1,10)
#                               # print(число1)
#                               i = 0                       
#                               continue
#                   else:
#                               break


# import random


# name = input ('Enter your name:')
# wish = input ('Do yoou want to play ?:')
# number = random.randint(1,10)
# i = 0 
# while True:
#       i +=1
#       if wish.lower().strip == 'yes':
#             guess_number = int(input('we asked the number from 1 to 10 try to find it. you have 5 tries. try  №' ))
#             {i}:'))
#             except ValueError:
#                   print ('enter number from 1 to 10:')
#                   continue
#             if guess_number == number:
#                    print('congratulations you won !!!')  
#                    wish = input('do you want repeat')

#       elif wish.lower().strip == 'no':
#             print('thank you, come again')

#       else: 
#             print('enter correct choice')








import random
имя =input('Введите ваше имя:')
старт=input('Хотите ли вы играть?:')

if старт == 'да':
      число1 =random.randint(1,10)
      # print (число1)
      while True:
            число2 = int(input('Введите число:'))
            счетчик = счетчик +1
            if число2 == число1:
                  print(f'Поздравляю  вы выиграли!!!, Сектор приз в терминале,ваше количество попыток{счетчикд}')
                  повтор=input('хотите ли пройти игру еще раз?:')
                  if повтор == 'да':
                              numbers = random.randint(1,10)
                              # print(число1)
                              i = 0                       
                              continue
                  else:
                              break


