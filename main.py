# Assignment 1
# ICS3U
# <your name>
# March 28, 2018

###### uncomment this when you are ready to work on it
#def CtoF ():
#

###### uncomment this when you are ready to work on it
#def FtoC ():
#

print('User chooses weather they would like to convert Celcius to Fahrenheit')


def CtoF(C):
    """Converts a temperature inputed in Celsius into Fahrenheit"""
    F =(1.8)*C+32
    return F

def FtoC(F):
    C =(0.55556)*(F-32)
    return C
        
temperature = int(input('Enter your temperature in Celsius: '))
print(round(CtoF(temperature)))

