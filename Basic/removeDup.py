'''
This piece of code will remove duplicates in list
'''
def removeduplicate(a):
    b=[]
    for i in a:
        c=0
        for j in a:
            if i==j:
                c=c+1
        if c>1 or c==1:
            if i not in b:
               b.append(i)
    print(b)   
    
a=[int(x) for x in input('Enter the numbers seperated by space \n').split()]
print('Given list is ',a)
removeduplicate(a)