'''
Checking Prime number or not
'''
def primeCheck(n):
    c,i=0,2
    while i<n:
        if n%i==0:
            c=c+1;
        i+=1
    return c
        
n=int(input('Enter number of your choice:\n'))
c=int(primeCheck(n))
if c<2:
    print("Bingo!! Prime number")
else:
  print("Not a Prime number")