# Assignment 1
# ICS3U
# <Shaan>
# March 28, 2018

print('Enter 1 for Celcius to Fahrenheit, and 2 for Fahrenheit to Celcius: ')
 
def CtoF(C):
    """Converts a temperature inputed in Celsius into Fahrenheit"""
    F =(1.8)*C+32
    return F

def FtoC(F):
    """Converts a temperature inputed in Fahrenheit into Celsius"""
    C =(0.55556)*(F-32)
    return C

X = int(input())
    
if X == 1:
        temperature1 = float(input('Enter your temperature in Celsius: '))
        if temperature1 < -273.15:
            print('invail input')
        else:
            print(int(round(CtoF(temperature1)))
            elif X == 2:
       temperature2 = float(input('Enter your temperature in Fahrenhit: '))
       print(round(FtoC(temperature2)))
else:
       print('invalid option')





