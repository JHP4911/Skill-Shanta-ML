#!/usr/bin/env python
# coding: utf-8

# ## 1 - Introduction to Vectorized Code

# ### Problem 1 Statement 
# 
# Convert given celcius temperatures to fahrenheit

# In[1]:


temp_in_celcius = [25.0, 26, 5, 28.2, 45.5, 10.2]
temp_in_celcius


# #### Iterative Solution

# In[2]:


temp_in_far = []
for c in temp_in_celcius:
    temp_in_far.append(c * 9/5 + 32)
temp_in_far


# #### List Comprehension solution

# In[3]:


temp_in_far = [(c * 9/5 + 32) for c in temp_in_celcius]
temp_in_far


# #### Numpy Vectorised solution

# In[4]:


import numpy as np


# In[5]:


temp_in_celcius = np.array(temp_in_celcius)


# In[6]:


temp_in_far = temp_in_celcius * 9/5 + 32
temp_in_far


# ### Comparing time performances of the 3 methods - Part 1

# In[7]:


import timeit


# In[8]:


method_1 = """temp_in_far = []
for c in temp_in_celcius:
    temp_in_far.append(c * 9/5 + 32)"""

method_2 = 'temp_in_far = [(c * 9/5 + 32) for c in temp_in_celcius]'

method_3 = 'temp_in_far = temp_in_celcius * 9/5 + 32'


# In[9]:


timeit.timeit(method_1, setup='temp_in_celcius = [25.0, 26, 5, 28.2, 45.5, 10.2]')


# In[10]:


timeit.timeit(method_2, setup='temp_in_celcius = [25.0, 26, 5, 28.2, 45.5, 10.2]')


# In[11]:


timeit.timeit(method_3, setup='import numpy; temp_in_celcius = numpy.array([25.0, 26, 5, 28.2, 45.5, 10.2])')


# #### As you can see, the winner is method_2: using list comprehension. Method_2 being more efficient than method_1 makes sense. But method_3 seems to have the poorest performance, which does not make sense!

# ### Comparing time performances of the 3 methods - Part 2

# In[12]:


import random


# In[13]:


a_million_temps_in_celcius = [random.uniform(10.0, 40.0) for _ in range(1000000)]
print(len(a_million_temps_in_celcius), '\n', a_million_temps_in_celcius[:5])


# In[14]:


timeit.timeit(method_1, number=1000, setup='import random; temp_in_celcius = [random.uniform(10.0, 40.0) for _ in range(1000000)]')


# In[15]:


timeit.timeit(method_2, number=1000, setup='import random; temp_in_celcius = [random.uniform(10.0, 40.0) for _ in range(1000000)]')


# In[16]:


timeit.timeit(method_3, number=1000, setup='import random; import numpy; temp_in_celcius = numpy.array([random.uniform(10.0, 40.0) for _ in range(1000000)])')


# #### This time, you can see that the clear winner by far is method_3: vectorized code using numpy. This is due to the size of N, which in the previous comparision was 5, and in this comparision it is a million.

# ## 2 - Characteristics of ndarrays

# ### Slicing ndarrays: creates a view, not a copy (unlike slicing built in sequence types)!

# In[17]:


temp_in_far


# In[18]:


two_temps = temp_in_far[1:3]
print(two_temps)
two_temps += 10
print(two_temps)


# In[19]:


temp_in_far


# ### A few important properties of ndarrays

# In[20]:


type(temp_in_far)


# In[21]:


temp_in_far.ndim


# In[22]:


temp_in_far.shape


# In[23]:


temp_in_far.size


# In[24]:


temp_in_far.dtype


# In[25]:


temp_in_far.itemsize


# ### A few important methods of ndarrays

# In[26]:


temp_in_far.min()


# In[27]:


temp_in_far.max()


# In[28]:


temp_in_far.sum()


# In[29]:


temp_in_far.mean()


# In[30]:


temp_in_far.std()


# ### A taste of 2-D arrays

# In[31]:


student_stats = np.array([(20, 30, 90), (40, 20, 80)])
student_stats


# In[32]:


student_stats.ndim


# In[33]:


student_stats.shape


# In[34]:


student_stats.size


# In[35]:


student_stats.dtype


# In[36]:


student_stats = np.array([(20, 30, 90), (40, 20, 80)], dtype=np.uint8)
student_stats


# In[37]:


student_stats.dtype


# ### Dicing ndarrays

# In[38]:


student_stats_flattened = student_stats.ravel()
student_stats_flattened


# In[39]:


student_stats_reshaped = student_stats_flattened.reshape(2, 3)
student_stats_reshaped


# In[40]:


student_stats_reshaped_2 = student_stats_reshaped.reshape(3, 2)
student_stats_reshaped_2


# In[41]:


student_stats_reshaped_2.T


# ### Problem 2 Statement
# 
# Given a series of sales revenues for each day, find the number of times the sales increased from one day to another. 
# 
# <pre>
# Example:
#     
#     given: [20, 22, 34, 31, 30, 22, 40, 41]
#     ouput: 4
# </pre>

# In[42]:


daily_revenues = [20, 22, 34, 31, 30, 22, 40, 41]
np_daily_revenues = np.array(daily_revenues)


# #### Naive solution

# In[43]:


def naive_count_rev_inc(x):
    count = 0
    for ind, e1 in enumerate(x):
        if ind == len(x) - 1:
            break
        e2 = x[ind+1]
        if e2 > e1:
            count += 1
    return count


# In[44]:


naive_count_rev_inc(daily_revenues)


# #### Optimized solution

# <pre>
# The following code:
# 
# np_daily_revenues[:-1] < np_daily_revenues[1:]
# 
# produces the following result:
# 
# array([ True,  True, False, False, False,  True,  True])
# </pre>

# In[45]:


def np_count_rev_inc(x):
    return np.count_nonzero(x[:-1] < x[1:])


# In[46]:


np_count_rev_inc(np_daily_revenues)


# In[47]:


method_1 = """
count = 0
for ind, e1 in enumerate(daily_revenues):
    if ind == len(daily_revenues) - 1:
        break
    e2 = daily_revenues[ind+1]
    if e2 > e1:
        count += 1"""

method_2 = 'np.count_nonzero(np_daily_revenues[:-1] < np_daily_revenues[1:])'


# In[48]:


timeit.timeit(method_1, setup='daily_revenues = [20, 22, 34, 31, 30, 22, 40, 41]')


# In[49]:


timeit.timeit(method_2, setup='import numpy as np; np_daily_revenues = np.array([20, 22, 34, 31, 30, 22, 40, 41])')


# In[50]:


timeit.timeit(method_1, number=1000, setup='import random; daily_revenues = random.choices(range(1000), k=1000000)')


# In[51]:


timeit.timeit(method_2, number=1000, setup='import random; import numpy as np; np_daily_revenues = np.array(random.choices(range(1000), k=1000000))')


# ### Some more important methods

# In[52]:


np.zeros((2, 3))


# In[53]:


np.ones((3, 3), dtype=np.int8)


# In[54]:


np.arange(10, 25, 5)


# In[55]:


np.linspace(10, 25, 5)

