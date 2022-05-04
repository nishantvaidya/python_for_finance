from cProfile import label
from time import time
from turtle import color
import numpy as np
import random as rd
import matplotlib as mlt
import matplotlib.pyplot as plt
a = np.array([0, 0.5, 1.0, 1.5, 2.0])
# print(type(a))
# print(a.std())
# print(a.sum())
# print(a.cumsum())
# print(np.sqrt(a)) 
#print(np.array([a, a ** 2]))
# Initialize 5000 * 5000 array
I = 5000
def fun(x):
    return 3 * x + 5

r = np.random.standard_normal((4,3))
# print(r)
# print(fun(r))
np.random.seed(2000)
y = np.random.standard_normal(20)
x = range(len(y))
print(x)
# plt.plot(y.cumsum(), 'b',lw=1.5)
# plt.plot(y.cumsum(),'ro')
# plt.grid(True)
# plt.xlim(1,20)
# plt.ylim(np.min(y.cumsum())-1, np.max(y.cumsum())+1)

# plt.title('A sample Plot')
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.axis('tight')



# Multiple data points plotting
y_mul = np.random.standard_normal((20,2)).cumsum(axis=0)
# plt.plot(y_mul[:,0],lw=1.5,label='1st')
# plt.plot(y_mul[:,1],lw=1.5,label='2nd')
# plt.plot(y_mul, 'ro')
# plt.grid(True)
# plt.axis('tight')
# plt.legend(loc=0)   
# plt.xlabel('Index')
# plt.ylabel('Value')
# plt.title('A Sample Plot')
# plt.show()


# Use of two subplots(Upper/Lower , Left and Right)
y_mul[:,0] = y_mul[:,0] * 100
# fig, ax1 = plt.subplots()
# plt.plot(y_mul[:,0] , 'b', lw=1.5, label ='1st')
# plt.plot(y_mul[:,0],'ro')
# plt.grid(True)
# plt.legend(loc=8)
# plt.axis('tight')
# plt.xlabel('index')
# plt.ylabel('value 1st')
# plt.title('A Sample Plot')
# ax2 = ax1.twinx()
# plt.plot(y_mul[:,1],'g', lw=1.5, label='2nd')
# plt.plot(y_mul[:,1],'ro')
# plt.legend(loc=0)
# plt.ylabel('value 2nd')
# plt.show()

# Use of two subplots with differet plots

plt.subplot(121)
plt.plot(y_mul[:,0] , 'b', lw=1.5, label ='1st')
plt.plot(y_mul[:,0],'ro')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.ylabel('value 1st')
plt.title('A Sample Plot 1st Data Set')
plt.subplot(122)
plt.bar(np.arange(len(y)), y_mul[:,1], width= 0.5, color='g',label='2nd')
plt.grid(True)
plt.legend(loc=0)
plt.axis('tight')
plt.xlabel('index')
plt.plot(y_mul[:,1],'g', lw=1.5, label='2nd')
plt.plot(y_mul[:,1],'ro')
plt.title('A Sample Plot 2nd Data Set')
plt.show()
