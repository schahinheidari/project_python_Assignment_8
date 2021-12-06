import random

options = ['Rock', 'Paper', 'Scissor']
scores = {'user':0, 'computer':0}
for i in range(10):
    computer_choice = random.choice(options)
    user_choice = input('play the game: ')

    if(user_choice == 'Rock' and computer_choice == 'Paper'):
        print('computer wins')
        scores['computer'] += 1
    elif(user_choice == 'Rock' and computer_choice == 'Scissor'):
        print('you win')
        scores['user'] += 1

        #elif..........

#### who wins ?