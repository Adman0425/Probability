#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing the modules
from scipy import random
import numpy as np
 
# limits of integration
a = 0
b = 1
N = 1000
#N = 100000
 
# function to calculate the sin of a particular value of z
def f(z):
    return np.cos(z) + np.sin(2*z)

print("N =", N)
# iterates and sums up values of different functions of x
for j in range(20):
    integral = 0.0
    for i in range (N):
        ran = random.normal(a,b)
        integral += f(ran)
    
    ans = integral/N
    print (ans)


# In[ ]:




