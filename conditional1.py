'''
this script let you apply basic math aperations as:
1, the user must press two numbers
2. the user must press and option from menu
3. the funtion must apply the operation
'''

#libraries#########################
import os

#functions####################
def calc (x,y,z):
    if z == 1 :
        ans = x + y
    elif z == 2:
        ans = x - y
    elif z == 3:
        ans = x * y
    else:
        ans = x / y
    return ans

##main#########################
n1=int(input("first number: "))
n2=int(input("two number: "))
print("MENU")
print("[1]. add")
print("[2]. subs")
print("[3]. mult")
print("[4]. div")

opt = int (input("press an option: "))

print ("the answer is: ", calc(n1,n2,opt))

