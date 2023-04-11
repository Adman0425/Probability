#!/usr/bin/env python
# coding: utf-8

# In[1]:


from scipy import random
import numpy as np

def cal(n):
    a = -1
    b = 1
    print("n =", n)

    integral = 0.0
    for j in range(n):
        x = np.random.uniform(a, b)
        y = np.random.uniform(a, b)
        if (((x-0.2)**2) + (2*(y+0.3)**2) <= 0.25):
            ran = 1
        else:
            ran = 0
        integral += ran

    ans = 4*integral / n
    print(ans)

cal(10)
cal(1000)
cal(100000)
cal(10000000)


# In[ ]:




