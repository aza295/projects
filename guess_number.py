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

import random



flag = 1
name = input('Введите ваше имя:')
v = input ('you want play?')
if v == 'yes': 
      number = random.randint(1,100)
      print(number)
      while True:
            a = int(input("Ugadaite chislo: "))
            if a == number:
                  print("Congratulations you won!!")
                  c=input('you want repeat?')
                  if c == 'yes':
                        continue
                  else:
                        break





      # b = input('Хотиgте ли вы сыграть ?')
      # c= int(input('Введите число')
      # if number == c
      #       print('Вы выиграли')
      # elif number < c
      #       print('')
