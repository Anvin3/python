def strReverse(s):
   splits=s.split()
   rvrs=splits[::-1]
   #print(rvrs)
   print("Reverse of string: ",rvrs)
   print("Reverse of string: ","".join(rvrs))

    
s=input('Enter a string\n')
strReverse(s)
        
            