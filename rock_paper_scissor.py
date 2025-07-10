import random

full = {'r':'Rock','p':'Paper','s':'Scissor'}
choices = ('r','p','s')
while True:
    choice = input('Rock,paper or scissor?(r/p/s):').lower()
    if choice  not in choices:
        print('enter valid alphabet')
        continue
    computer = random.choice(choices)
    print(f'you choose {full[choice]}')
    print(f'computer choose {full[computer]}')
    if choice == computer:
        print('Tie')
    elif choice == 'r' and computer == 's':
        print('You win')
    elif choice == 'r' and computer == 'p':
        print('You lose')
    elif choice == 's' and computer == 'p':
        print('You win')
    elif choice == 's' and computer == 'r':
        print('You lose')
    elif choice == 'p' and computer == 'r':
        print('You win')
    elif choice == 'p' and computer == 's':
        print('You lose')

    should_continue = input('Do you want to continue(Y/N):').lower()
    if should_continue == 'n':
        break
    

