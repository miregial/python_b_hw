#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("abcdefgh"[0] + "ABCDEFGH"[:1:2] + "hgfedcba"[-2:-1])


# In[2]:


def f(a, b, c):
    if True and a<=c:
        d = 3 if not(c==c%b) and not(a%b==a) or c<=a else 4
    elif a==b or True:
        if c==a and not(a<=a//c):
            d = 1
        else:
            d = 2
    else:
        d = 5
    return d
f(8,9,9)


# In[3]:


lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lst[:] = [0]
print(lst[:1:2])


# In[4]:


print("87654321"[2] + "abcdefgh"[:-2] + "hgfedcba"[:1:])


# In[5]:


(0 or False) and True


# In[6]:


def f(a, b, c):
    if (c<=b or False) and True:
        if not(a%c<=b%c and not(False)):
            d = 1
        else:
            d = 2
    elif False or c!=c//b:
        d = 3 if a!=c or not(True) else 4
    else:
        d = 5
    return d
f(12,2,12)


# In[23]:


for k in range(3, 12, 2):
    print(k )
   


# In[11]:


s = 0
for k in range(3, 13, 3):
    if k == 11:
        break
    s += 1
s


# In[16]:


12==12


# In[26]:


s = 0
for k in range(3, 12, 2):
    if k == 11:
        break
    s += 1
s


# In[29]:


s = 0
for k in range(3, 11, 3):
    if k == 10:
        break
    s += 1
s


# In[31]:


lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lst[1:1] = [1]
print(lst)
#print(lst[4:2:-2])


# In[32]:


lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lst[1:1] = [1]
print(lst[4:2:-2])


# In[33]:


print("76543210"[0] + "01234567"[1::-1] + "12345678"[:0:])


# In[34]:


print("abcdefgh"[-1] + "hgfedcba"[:1:-1] + "01234567"[0:-1])


# In[35]:


lst = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
lst[1:1] = [512, 256, 128, 64, 32, 16, 8, 4]
print(lst[3:0:-1])


# In[36]:


def f(a, b, c):
    if not(b!=c) or b!=b:
        if c//b==b and not(b<=a):
            d = 1
        else:
            d = 2
    elif not(b!=a) or b>=b and b==c:
        d = 3 if not(True and c<=c) else 4
    else:
        d = 5
    return d
f(6,6,9)


# In[38]:


s = 0
for k in range(5):
    if k == 2:
        continue
    s += 1
s


# In[41]:


lst = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lst[1:1] = [256]
print(lst[1::-2])


# In[43]:


s = 0
for k in range(6):
    s += k
s


# In[44]:


def f(a, b, c):
    if not(False or a!=b//c):
        if not(a%c==c and b%c<=a and c<=c):
            d = 1
        else:
            d = 2
    elif a%c>=c%a or c>=b:
        d = 3 if not(c>=a//b or b==c) else 4
    else:
        d = 5
    return d
f(12,2,3)


# In[ ]:




