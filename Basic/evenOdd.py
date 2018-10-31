'''
Check number is even or odd
'''
def evenOddcheck(num):
    if(num%2)==0:
        print("Hola {} is a even number".format(num))
        if(num%4)==0:
                print("And {} is also divisible by 4".format(num))
    else:
        print("Hola {} is a odd number".format(num))
num=int(input("Please enter a number of your choice:"))
evenOddcheck(num)