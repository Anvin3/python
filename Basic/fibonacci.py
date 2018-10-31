'''
Program for Fibonacci series.
The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21
'''

def fib(n):
    t1,t2,i=0,1,3
    print(t1, end=' ')
    print(t2, end=' ')
    while(i<=n):
        t1,t2=t2,t1+t2
        print(t2, end=' ')
        i=i+1
n= int(input('Enter length of sequence required (>2):'))
if n==2:
    print("Sequence is : 0 1")
elif n==1:
    print("Sequence is : 0 ")
elif n<1:
    print("Please enter a length which is greater than 2 ")
else:
    print('Series of length {} is'.format(n))
    fib(n)
    
