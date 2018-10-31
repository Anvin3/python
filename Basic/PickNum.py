'''
Random number guessing game.
'''
import random
num=random.randint(1,9)
t=0
play=True
while play:
    
    #print(num)
    g=int(input("Guess the number I am thinking of in between 1 and 9\n"))
    t=t+1
    if num<g:
        print("Guess is high")
        continue
    elif num>g:
        print("Guess is low")
        continue
    elif num==g:
        print("Hurrah!! Perfect guess")
        if input("Do you want to continue, if not type exit\n").lower()=='exit' :
            print("Thank you, Good day!! Number of trials are {} ".format(t))
            t=0
            play=False
        
