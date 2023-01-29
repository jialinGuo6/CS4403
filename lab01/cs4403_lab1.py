# -*- coding: utf-8 -*-
"""CS4403_lab1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P6Gde4OKMgwBzp_YO1GEWOTC-cpWujlZ
"""

import random
import matplotlib.pyplot as plt
import time 
import numpy as np
seedList = []
LTwoList = []
Klist = []
seedList = []
k =0       #  cCount try to know how many time to get get a last 2 digits: if get a same last 2 digits(set cCount(0) record again), if not same cCount++
cCountSum = 0   #  sum of cCount
for i in range(1,202):       #  repeat 200 times
    k = k + 1     
    random.seed(i)           #  one seed get one random int 
    num = random.randint(1000000, 9999999)
    lastTwo = num%100    # 1 234 5(67) get the 6th and 7th digit
    LTwoList.append(lastTwo)
    if len(LTwoList) != len(set(LTwoList)):
      cCountSum= cCountSum + k
      seedList.append(i)
      Klist.append(k)
      LTwoList = []
      k=0
print('which seed happen repeat',seedList)
print('Klist',Klist)
print('average number of iterations required before a collision: ', cCountSum/len(Klist))
plt.subplot(1, 2, 1)
plt.scatter(seedList,Klist)
plt.title("Scatter k Of happen")
plt.xlabel('which seed happen repeat')
plt.ylabel('k')

plt.subplot(1, 2, 2)
plt.plot(Klist)
plt.title("k Of happen")
plt.xlabel('How many k')
plt.show()

seedList = []
LTwoList = []
Klist = []
seedList = []
k =0       #  cCount try to know how many time to get get a last 2 digits: if get a same last 2 digits(set cCount(0) record again), if not same cCount++
cCountSum = 0   #  sum of cCount
for i in range(1,202):       #  repeat 200 times
    k = k + 1     
    random.seed(i)           #  one seed get one random int 
    num = random.randint(1000000, 9999999)
    lastTwo = num%1000    
    LTwoList.append(lastTwo)
    if len(LTwoList) != len(set(LTwoList)):
      cCountSum= cCountSum + k
      seedList.append(i)
      Klist.append(k)
      LTwoList = []
      k=0


print('which seed happen repeat',seedList)
print('Klist',Klist)
print('average number of iterations required before a collision: ', cCountSum/len(Klist))
plt.subplot(1, 2, 1)
plt.scatter(seedList,Klist)
plt.title("Scatter k Of happen")
plt.xlabel('which seed happen repeat')
plt.ylabel('k')

plt.subplot(1, 2, 2)
plt.plot(Klist)
plt.title("k Of happen")
plt.xlabel('How many k')
plt.show()

seedList = []
LTwoList = []
Klist = []
seedList = []
k =0       #  cCount try to know how many time to get get a last 2 digits: if get a same last 2 digits(set cCount(0) record again), if not same cCount++
cCountSum = 0   #  sum of cCount
for i in range(1,202):       #  repeat 200 times
    k = k + 1     
    random.seed(i)           #  one seed get one random int 
    num = random.randint(1000000, 9999999)
    lastTwo = num%10000   
    LTwoList.append(lastTwo)
    if len(LTwoList) != len(set(LTwoList)):
      cCountSum= cCountSum + k
      seedList.append(i)
      Klist.append(k)
      LTwoList = []
      k=0


print('which seed happen repeat',seedList)
print('Klist',Klist)
print('average number of iterations required before a collision: ', cCountSum/len(Klist))
plt.subplot(1, 2, 1)
plt.scatter(seedList,Klist)
plt.title("Scatter k Of happen")
plt.xlabel('which seed happen repeat')
plt.ylabel('k')
