#random number
from random import random

listnum = []
def Rannum() :
    num = int(input())
    i = 0
    x = 0
    #listnum = []
    for i in range(20) :
        ran = int((random())*(10**num))
        #while i < 20:
        listnum.append(ran)
        #print(ran)
    listnum.sort()

Rannum()
print(listnum)
#def Sornum() :
    #Rannum()

#Rannum()