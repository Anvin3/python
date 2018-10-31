'''
Rock paper scissors game.
'''
values=['rock','scissors','paper']
dec={'rock':'scissors','scissors':'paper','paper':'rock'}
play=True
def inputTake(a):
    p1=input("Type player {} choice : Rock, Scissors, Paper:\n".format(a))
    if p1 not in values:
        print('invalid input!!')
        p1=input("Type your choice again: Rock, Scissors, Paper:\n ")
        
    return p1.lower()
def inputCheck(choice1, choice2):
    if choice1==choice2:
        return 'Both won!!'
        
        for i in dec:
            if choice1==i and choice2==dec[i]:
                return 'Player1 won'
               
    else:
        return 'Player2 won'

while play:
    p1=inputTake(1)
    p2=inputTake(2)
    print(inputCheck(p1, p2))
    check=input("Want to continue with game?, Type Yes or No\n")
   #print(check.lower())
    if check.lower()=='no':
        print('Thank you, Good day!!')
        play=False
        
   