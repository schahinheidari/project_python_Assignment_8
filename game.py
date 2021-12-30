import random

options = ['Rock', 'Paper', 'Scissor']
scores = {'user':0, 'computer':0}
for i in range(10):
    computer_choice = random.choice(options)
    print("Computer select: ",computer_choice)
    print("ROCK,PAPER,SCISSOR GAME")
    print("1 for Rock","2 for Paper","3 for Scissor",end="\n")
    user_choice = int(input('play the game and select your option: '))

    if((user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1)): 
        print('computer wins')
        scores['computer'] += 1
    elif((user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2)):
        print("Your select is Rock")
        print('you win')
        scores['user'] += 1

    if int(scores['user'])>int(scores['computer']):
                print("Congratulations You Win")
                print("Score is:","Your score: ",scores['user'],"Computer score: ",scores['computer'],end=" ")
    elif int(scores['computer'])>int(scores['user']):
                print("You Lose the game. Computer win the game:")
                print("Score is:","Your score: ",scores['user'],"Computer score: ",scores['computer'],end=" ")
    else:
                print("Match Draw")
                print("Score is:","Your score: ",scores['user'],",Computer score: ",scores['computer'],end=" ")
    user_choice=input("Want to Play again?(Yes/Exit)")
    if user_choice=='yes' or user_choice=='Yes' or user_choice=='YES':
            continue             
    else:
            break    

#### who wins ?