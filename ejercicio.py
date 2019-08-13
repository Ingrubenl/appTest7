import os
from random import randint, uniform, random

## this fubction generates integer numbers
def Z():
    ansz = randint(0,100)
    return ansz 
## this fucntion generates float numbers
def R():
    ansr = uniform(0,100)
    return ansr

# Main
print(" the integer random number is : " , Z())
print(" the integer random number is : " , R())

