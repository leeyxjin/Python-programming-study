types=['Rock', 'Sissor', 'Paper']
import random
computer=random.choice(types)


while True:
    user=input('Rock-Sissor-Paper!: ')
    
    if user in types:
        print('computer:',computer)
        if user==computer:
            print('It\'s a tie!')
        if (user, computer) in [('Rock', 'Sissor'), ('Sissor','Paper'), ('Paper','Rock')]:
            print('You win!')
        else:
            print('You lose!')
        break
    else:
        print('Check for typos.')