'''
This piece of code will remove duplicates in list
'''
def removeduplicate(a):
    b=set(a)
    
    print('Removed duplicates---',b)   
    
a=[int(x) for x in input('Enter the numbers seperated by space \n').split()]
print('Given list is ',a)
removeduplicate(a)