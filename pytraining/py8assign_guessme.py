import random

rand_num = random.randint(1, 1000)
# print(rand_num)

i = 10
while i > 0:
    user_num = int(input('Can you guess the number ?\n'))
    if user_num < rand_num:
        print('You guessed less!')
    elif user_num > rand_num:
        print('You guessed more!')
    else:
        print('Cracked!')
        break
    i -= 1
    print(f'You have {i} chances left...')
