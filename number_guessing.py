import random


a=random.randint(1,100)
while True:
    try:
        b=int(input('Guess the number between 1 and 100:'))
        if a == b:
            print('Congratulation , You found the number')
            break
        elif a > b:
            print('Too Low')
        elif a < b:
            print('Too High')
    except ValueError:
            print('Please enter a valid number')