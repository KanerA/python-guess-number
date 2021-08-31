import random
import math


def guess_number():
    num = math.floor(random.random() * 10 + 1)
    print('Guess the number between 1 - 10 !')
    for i in range(5, 0, -1):
        if i == 1:
            print('You have ' + str(i) + ' try left')
        else:
            print('You have ' + str(i) + ' tries left')
        user_num = int(input())
        if user_num == num:
            return print('Good job!')
        else:
            if(i != 1):
                print('Try Again')
    print('Better luck next time!')


guess_number()
