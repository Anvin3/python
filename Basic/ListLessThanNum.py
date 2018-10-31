'''
This piece of code will take
1. Input number to form new list contains elements less than the given number 
'''
   
list1=[5,10,60,72,1,3,5,78,90,5,6,7,8,9,10]
print("List offered is",list1)
num=int(input("Please enter a number of your choice to get new list:"))
subList=[i for i in list1 if i<num ]
print("New list is",subList)