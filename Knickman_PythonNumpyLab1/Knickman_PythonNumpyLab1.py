#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Andrew Knickman
#ITEC 345
#Python Numpy Lab 1


# In[2]:


import numpy as np
list1=[0,1,2,3,4]
arr1d=np.array(list1)
print(type(arr1d))
arr1d


# In[3]:


arr1d+2


# In[4]:


list2=[[0,1,2],[3,4,5],[6,7,8]]
arr2d = np.array(list2)
arr2d


# In[5]:


arr2d_f = np.array(list2, dtype='float')
arr2d_f


# In[6]:


arr2d_f.astype('int')


# In[7]:


arr2d_f.astype('int').astype('str')


# In[8]:


list3 = [[1,2,3,4],[3,4,5,6],[5,6,7,8]]
arr3 = np.array(list2,dtype='float')
arr3


# In[9]:


arr3[:2,:2]


# In[10]:


b = arr3 > 4
b


# In[11]:


arr3[b]


# In[12]:


arr3[::-1,]


# In[13]:


arr3[::-1,::-1]


# In[14]:


arr3[1,1] = np.nan
arr3[1,2] = np.inf
arr3


# In[15]:


missing_bool = np.isnan(arr3) | np.isinf(arr3)
arr3[missing_bool] = -1
arr3


# In[16]:


print("Mean value is:", arr3.mean())
print("Max value is:", arr3.max())
print("Min value is:", arr3.min())


# In[17]:


print("Column wise min:",np.amin(arr3,axis=0))
print("Row wise min:",np.amin(arr3,axis=1))


# In[18]:


np.cumsum(arr3)


# In[19]:


arr3a = arr3[:2,:2]
arr3a[:1,:1] = 100
arr3


# In[20]:


arr3b = arr3[:2,:2].copy()
arr3b[:1,:1] = 101
arr3


# In[21]:


arr3.reshape(4,3)


# In[22]:


print(np.arange(5))
print(np.arange(0,10))
print(np.arange(0,10,2))
print(np.arange(10,0,-1))


# In[23]:


np.linspace(start=1,stop=50,num=10,dtype=int)
np.set_printoptions(precision=2)
np.logspace(start=1,stop=50,num=10,base=10)


# In[24]:


np.zeros([2,2])
np.ones([2,2])


# In[25]:


a = [1,2,3]
print('Tile:', np.tile(a,2))
print('Repeat:',np.repeat(a,2))


# In[26]:


print(np.random.rand(2,2))
print(np.random.randn(2,2))
print(np.random.randint(0, 10, size=[2,2]))
print(np.random.random())


# In[27]:


print(np.random.random(size=[2,2]))
print(np.random.choice(['a','e','i','o','u'], size=10))
print(np.random.choice(['a','e','i','o','u'], size=10, p=[0.3,.1,0.1,0.4,0.1]))


# In[28]:


rn = np.random.RandomState(100)
print(rn.rand(2,2))
np.random.seed(100)
print(np.random.rand(2,2))


# In[29]:


np.random.seed(100)
arr_rand = np.random.randint(0,10,size=10)
print(arr_rand)
uniqs, counts = np.unique(arr_rand, return_counts=True)
print("Unique Items:",uniqs)
print("Counts:",counts)

