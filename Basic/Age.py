'''
This program will calculate the year by when user will complete 100 years old.
'''
import datetime
def calAge(age):
    diff=100-age
    curYear = int(datetime.date.today().strftime("%Y"))
    year=str(curYear+diff)
    print(name+' will be 100 years old by '+year)
name=input('Enter your name:')
age= int(input('Enter your age:'))
calAge(age)
    
