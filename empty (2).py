#!/usr/bin/env python
# coding: utf-8

# In[1]:



any(x%3 == 2 or x%4 == 3 for x in [-2, -18, -9, -2, 25])


# In[3]:


import math
isinstance(math.sqrt(25), (tuple, str, float))


# In[4]:



any(int(x) < -1 for x in '7950')


# In[5]:



all(int(x) >= 0 for x in '235031')


# In[6]:


isinstance((-6, 8, 27, -6), (int, tuple, str))


# In[7]:



all(abs(x) >= 6 for x in {-25, 17, -16, -16, -10, 5})


# In[8]:


type(math.sqrt(25))


# In[10]:


print(sum(complex(t[0], t[1]) for t in zip((10, -30, 19, 19, -18, 1), (18, -26, 22, -29, 2, -29))))


# In[11]:


len({-3, 18, 6, 1, -28}) + min({1: 16, 16: -8, 16: -14, -24: 4, 16: 17}) + max(range(1))


# In[12]:


min({1: 16, 16: -8, 16: -14, -24: 4, 16: 17})


# In[13]:


print(max(t[1] for t in zip((-4, -11, -11, 20, 17), range(-8, -22, -3))))


# In[16]:


[x for x in range(-8, -22, -3)]


# In[18]:


[t[1] for t in zip((-4, -11, -11, 20, 17), range(-8, -22, -3))]


# In[19]:


any(x/7 < -3 for x in {-11: 27, 28: -30, -6: 16}.values())


# In[20]:


isinstance((17, 3, 17, -29, 4), (int, str, tuple))


# In[21]:


all(x/7 <= -1 for x in range(4))


# In[22]:


any(x > 12 for x in [3, -27, -27, 13, -7, -6])


# In[23]:



isinstance((20, 11, -14, 20), (int, float, range))


# In[24]:


all(x/7 <= -1 for x in [-21, -4, -10, -21, 0])


# In[27]:


{-11: 27, 28: -30, -6: 16}.values()


# In[28]:


min([11, 12, -15, 11]) + len((29, -30, 23, 12, 29)) + max({-16: -14, -25: 10, -24: 10})


# In[30]:


print(min(t[0] for t in zip((19, -15, -28, 19), (-24, 8, -21, -29, -24, 12, -12))))


# In[31]:


max({-24: -2, 11: -3, 18: -25, 18: -7})


# In[32]:


sum(range(0, 1))


# In[33]:


max({-24: -2, 11: -3, 18: -25, 18: -7}) + sum(range(0, 1)) + len('911385')


# In[34]:


print(max(x for x, y in zip([-23, 12, -29, -2, -2, 5, -25], (1, -21, 8, 8, 16))))


# In[35]:


max(range(-21, -16)) 


# In[36]:


sum((-10, 17, 18, 19, 17))


# In[37]:


type(6.1251e+23)


# In[38]:



any(x%3 == 2 or x%4 == 3 for x in range(13, 10, -1))


# In[39]:



all(x%2 == 0 or x%3 > 0 for x in [-10, 4, 3, 3, 11])


# In[40]:



any(x%3 == 2 or x%4 == 3 for x in {5: 28, -8: 1, 12: -24, 2: -1})


# In[41]:



any(abs(x) > 30 for x in {29: 27, -22: -24, 0: 22, 0: -27})


# In[42]:



any(x/7 < -1 for x in {-12: -18, -1: -30, -1: -12, -23: -14}.values())


# In[43]:


isinstance(False, (complex, float, int))


# In[45]:


type(False)


# In[ ]:




