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
while True:
    if X == 1:
        temperature1 = float(input('Enter your temperature in Celsius: '))
        if temperature1 < -273.15:
            print('invaild input')
            continue
        else:
            print(round(CtoF(temperature1)))
            break
            
    elif X == 2:
       temperature2 = float(input('Enter your temperature in Fahrenhit: '))
       if temperature2 < -459.67:
           print('invalid input')
        else:
            print(round(FtoC(temperature2)))
    else:
       print('invalid option')
       
        




