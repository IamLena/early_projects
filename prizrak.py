# Ghost Game
from random import randint
print('Приведение')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint (1, 3)
    print('Вперели три двери...')
    print('За одной из них призрак.')
    print('Какую дверь ты откроешь?')
    door = input('1, 2, или 3?')
    door_num = int(door)
    if door_num == ghost_door:
        print('ПРИЗРАК!')
        feeling_brave = False
    else:
        print('ПУТЬ СВОБОДЕН!')
        print('Переходи в следующую комнату.')
        score = score+1
print('БЕГИ!')
print('конец инры! Твой счет:', score)
        

