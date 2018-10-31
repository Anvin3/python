def strReverse(inpStr):
   rvrs=inpStr[::-1]
   #print(rvrs)
   if rvrs==inpStr:
        print("Given string is a palindrome!!")
   else:
        print("Given string is not a palindrome")
    
    
inpStr=input('Enter a string to check whether its palindrome or not\n')
strReverse(inpStr)
        
            