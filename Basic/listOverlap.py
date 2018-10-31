def intersect(c,d):
    comList=[]
    for i in c:
        if i in d:
            if i in comList:
                continue
            else:
                comList.append(i)
    print("common elements are ", comList)

import random

c=[1,2,3,4,5,6,6,6]
d=[1,2,3,4,5,8,9,0,0,54,6,6]
print(c )
print(d )
intersect(c,d)


        
            