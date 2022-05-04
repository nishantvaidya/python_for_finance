# Scatter plots example
import numpy as np
from numpy.random import default_rng
import random as rd
import matplotlib as mlt
import matplotlib.pyplot as plt

rng = default_rng()
y = rng.standard_normal((1000,2))

print(y[0:5])
plt.figure(figsize=(7,5))
# plt.scatter(y[:, 0],y[:, 1], marker='o')
# plt.grid(True)
# plt.xlabel('1st')
# plt.ylabel('2nd')   
# plt.title('Scatter Plot')

# Histogram  plotting

plt.hist(y,bins=25,stacked=True,label=['1st','2nd'],color=['b', 'g'])
plt.grid(True)
plt.legend(loc=0)
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')
plt.show()