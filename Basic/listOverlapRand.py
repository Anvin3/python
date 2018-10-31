def intersect(c,d):
    comList=set(i for i in c if i in d )
    print("Common elements are ", comList)
import random
c=random.sample(range(50),15)
d=random.sample(range(20),15)
print(c )
print(d )
intersect(c,d)


        
            