'''
Random number guessing game.
'''
import random
num=random.randint(1001,9999)
t=0
play=True
c,b=2,0
while play:

    #print(num)
    g=int(input("Guess the number I am thinking of in between 1001 and 9999 \n"))
    t=t+1
    
    if num==g:
        print('{} cows, {} bulls'.format(c, b))
        print('Perfect Guess!!')
        play=False
    else:
        print('{} cows, {} bulls'.format(c,b))
        c=c-1
        b=b+1
        
