#!/usr/bin/env python
# coding: utf-8

# In[1]:



all(x >= -29 for x in (20, -30, -24, -6, -6))


# In[2]:



any(x%3 == 2 or x%4 == 3 for x in {-21: -25, 5: -27, 5: 6, -23: -3})


# In[3]:



all(abs(int(x)) >= -15 for x in '45544')


# In[4]:


any(x > 9 for x in {-7: 7, -9: -14, 7: -19, 5: 10}.values())


# In[5]:



isinstance({-27, 10, 5, -24, 5}, (dict, range, str))


# In[6]:



isinstance(range(-7, -5), (int, range, dict))


# In[7]:



all(x <= 21 for x in [23, -13, -1, -13])


# In[8]:



any(abs(x) > 29 for x in (28, -20, -7, 28))


# In[9]:



all(x/7 <= 0 for x in {-17: 11, -19: -23, 2: -30})


# In[10]:



isinstance(4.0494e+23, (complex, set, int))


# In[11]:



any(x%3 == 2 or x%4 == 3 for x in range(-6, -11, -2))


# In[12]:


import math
isinstance(math.floor(1/121), (float, set, str))


# In[13]:


print(max(t[0] for t in zip([-21, -21, -21, -18, 17, -13, -29], [-1, 3, -30, -30, 13])))


# In[14]:


sum(range(13, 14)) + max((29, -7, 17, 20, -7, 17)) + min({-24, -17, -19, -23, -19, -17, 27})


# In[15]:


print(max(t[1] for t in zip([-16, -24, -2, -24], range(18, 22, 2))))


# In[16]:


min({22, -6, 1, 1, 29, -5}) + len(range(15, 17, 3)) + max({-18: 14, 22: -21, -15: 27})


# In[17]:


print(min(x for x, y in zip((3, 3, 10, 13), (-18, -20, 18, -23, -18, 21, 22))))


# In[18]:


print(sum(complex(t[0], -2*t[1]) for t in zip(range(19, 20, 3), (-3, -16, -23, 3, -3, 23, -18))))


# In[19]:


max(range(-23, -22)) + sum({-10: 10, 8: -9, -10: -23, 27: -14}) + len({0: 12, 19: 22, -29: -26})


# In[35]:


list(range(19, 20, 3))


# In[37]:


len({0: 12, 19: 22, -29: -26})


# In[41]:


sum({-10: 10, 8: -9, -10: -23, 27: -14}) 


# In[42]:


max(range(-23, -22)) 


# In[43]:


max({20: 21, 26: 13, 6: 4}.values())


# In[44]:



any(abs(x) > 16 for x in [0, -17, -17, -8])


# In[45]:



isinstance({13: -28, 13: -12, -27: 9, -23: 26}, (str, bool, dict))


# In[46]:



all(x/7 <= 2 for x in (7, 24, 24, -12, -23, 19, -19))


# In[47]:



isinstance({-15: 10, 4: 3, -30: -14, -15: 9}, (dict, str, tuple))


# In[48]:



all(abs(int(x)) >= 16 for x in '9258')


# In[49]:


isinstance([-17, 15, 11, -1, -17], (tuple, str, list))


# In[50]:



any(x/7 < 0 for x in {27, -4, -12, -4})


# In[51]:



isinstance(-18//151, (tuple, bool, float))


# In[53]:


type(-18//151)


# In[54]:


all(x%2 == 0 or x%3 > 0 for x in {-7, -17, -8, -7, 8, -7, -30})


# In[56]:



any(int(x)%3 == 2 or int(x)%4 == 3 for x in '61994')


# In[57]:



all(abs(x) >= 3 for x in (3, -15, 27, -15, 29, 11))


# In[58]:


max(range(-23, -22)) + sum({-10: 10, 8: -9, -10: -23, 27: -14}) + len({0: 12, 19: 22, -29: -26})


# In[59]:


min(range(1, 3, 2)) + len({-23, 5, -12, -23}) + max({20: 21, 26: 13, 6: 4}.values())


# In[60]:


max(range(-23, -22)) 


# In[61]:


sum({-10: 10, 8: -9, -10: -23, 27: -14})


# In[ ]:




