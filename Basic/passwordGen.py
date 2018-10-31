'Random password generator'
import random
import string
def gen(s,i):
    tpwd=''
    if i==1:
       tpwd="".join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation) 
                for i in range(10))
    elif i==2:
       tpwd="".join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation) 
                for i in range(8))
    elif i==3:
       tpwd="".join(random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits) 
                for i in range(6))
    return  tpwd  

    
s=input('Enter your name:\n')
strength=int(input('Enter your preference for password strength:\n 1 for Strong \n 2 for medium \n 3 for weak \n '))
if strength not in range(1,3):
    strength=int(input('Re-enter your preference for password strength:\n 1 for Strong \n 2 for medium \n 3 for weak \n '))
pwd=gen(s,strength)
print('Password generated is ',pwd)

        
            