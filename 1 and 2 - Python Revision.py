#!/usr/bin/env python
# coding: utf-8

# ## 1 - Understanding Mutable and Immutable Data Types

# ### Boolean, Integer, Float, String, Tuple: Immutable

# In[1]:


raining_now = False


# In[2]:


type(raining_now)


# In[3]:


print(raining_now)


# In[4]:


id(raining_now)


# In[5]:


raining_now = True


# In[6]:


print(raining_now)


# In[7]:


id(raining_now)


# ### List, Dictionary, Set: Mutable

# In[8]:


student_name_list = ['Monika', 'Nikhil', "Lalit"]


# In[9]:


type(student_name_list)


# In[10]:


print(student_name_list)


# In[11]:


id(student_name_list)


# In[12]:


student_name_list.pop()


# In[13]:


print(student_name_list)


# In[14]:


id(student_name_list)


# ### Think how you can identify a data type as mutable or immutable without using the id() function

# Answer: By checking if the data type (or class in general) has methods that allow chaning the contents of its objects - you can use dir() or help().

# In[15]:


help(list) # multiple methods to change contents of object, such as append(), clear(), extend(), pop() ...


# In[16]:


help(bool) # no method to change contents of object


# ## 2 - Problem-Solving and Optimization

# ### Problem 1 Statement
# 
# The class starts when a certain number of students have joined. Until then, we wait.
# 
# Write Python code to simulate this scenario.

# #### Basic Solution

# In[17]:


student_count = 0
class_started = False

while (class_started == False):
    
    if (student_count == 5):
        class_started = True
        
    else:
        print('Waiting...')
        students_joined = input('Did a student join (y/n)? ')
        if (students_joined == 'y'):
            student_count += 1
            
print("Great! Let's start...")


# #### Optimised solution

# In[18]:


student_count = 0

while (student_count < 5):
    
    print('Waiting...')
    students_joined = input('Did a student join (y/n)? ')
    if (students_joined == 'y'):
        student_count += 1
            
print("Great! Let's start...")


# #### Further optimised solution

# In[19]:


students_count = 0

while (students_count < 5):
    
    print('Waiting...')
    students_count += int(input('How many students joined? '))
            
print("Great! Let's start...")


# ### Problem 2 Statement:
#     
# Identify given circuits as serial or parallel.

# #### Basic Solution

# In[20]:


circuits = [('Circuit A', True, True, 'On'), 
            ('Circuit B', True, False, 'On'),
            ('Circuit C', True, False, 'Off'),
            ('Circuit D', False, True, 'On'),
            ('Circuit E', False, True, 'Off'),
            ('Circuit F', False, False, 'On'),
            ('Circuit G', False, False, 'Off'),
            ('Circuit H', True, True, 'Off')]


# In[21]:


for circuit_name, switch_1, switch_2, bulb_status in circuits:
    
    if ((switch_1 and not(switch_2) and bulb_status == 'On') or (not(switch_1) and switch_2 and bulb_status == 'On')):
        circuit_type = 'a parallel circuit'
        
    if ((switch_1 and not(switch_2) and bulb_status == 'Off') or (not(switch_1) and switch_2 and bulb_status == 'Off')):
        circuit_type = 'a serial circuit'
        
    if ((switch_1 and switch_2 and bulb_status == 'On') or (not(switch_1) and not(switch_2) and bulb_status == 'Off')):
        circuit_type = 'either a parallel or a serial circuit'
        
    if (switch_1 and switch_2 and bulb_status == 'Off'):
        circuit_type = 'a broken circuit'
        
    if (not(switch_1) and not(switch_2) and bulb_status == 'On'):
        circuit_type = 'a impossible circuit'
        
    print("{} is {}".format(circuit_name, circuit_type))


# #### Optimised solution

# In[22]:


for circuit_name, switch_1, switch_2, bulb_status in circuits:
    
    if (not(switch_1 or switch_2) and bulb_status == 'On'):
        circuit_type = 'a impossible circuit'
        
    elif ((switch_1 and switch_2) and (bulb_status == 'Off')):
        circuit_type = 'a broken circuit'
        
    elif ((switch_1 and switch_2) or not(switch_1 or switch_2)):
        circuit_type = 'either a parallel or a serial circuit'
        
    elif ((switch_1 or switch_2) and (bulb_status == 'On')):
        circuit_type = 'a parallel circuit'
        
    elif ((switch_1 or switch_2) and (bulb_status == 'Off')):
        circuit_type = 'a serial circuit'
        
    print("{} is {}".format(circuit_name, circuit_type))


# ## 3 - Some more basics

# ### Left shift and right shift operators

# In[23]:


for i in range(21):
    print('{:>3} in decimal is {:>8} in binary'.format(i, bin(i)))


# In[24]:


x = 2
y = x * x * x
print(y)
y = x ** 3
print(y)
y = x << 2     # 00000010 << 2 = 00001000 = 8
print(y)


# In[25]:


x = 16
y = x >> 2    # 00010000 >> 2 = 00000100 = 4
print(y)


# ### Problem 3 Statement 
# 
# Generate the Fibonacci Series

# #### Iterative Solution (quite fast)

# In[26]:


fib_list = [1, 1]

for i in range(10):
    fib_list.append(fib_list[-1] + fib_list[-2])
    
print(fib_list)


# #### Recursive Solution (very slow)

# In[27]:


def fibr(n):
    
    if n < 2:
        return n
    
    return fibr(n-1) + fibr(n-2)

def generate_fibr(count=10):
    
    fib_list = []
    
    for n in range(count):
        fib_list.append(fibr(n))
        
    return fib_list


# In[28]:


generate_fibr()


# In[29]:


generate_fibr(15)


# In[30]:


print(generate_fibr(20)) # fast


# In[31]:


print(generate_fibr(30)) # can notice this one taking a split second


# In[32]:


print(generate_fibr(35)) # took a couple of secs!


# In[33]:


# print(generate_fibr(50)) 

# this will probably cause Jupyter to crash!


# #### Recursive Solution with Memoization (very fast)

# In[34]:


def fibrm(n, fib_dict):
    
    if n not in fib_dict:
        fib_dict[n] = fibrm(n-1, fib_dict) + fibrm(n-2, fib_dict)
    
    return fib_dict[n]

def generate_fibrm(count=10):
    
    fib_dict = {0: 0, 1: 1}
    
    for n in range(count):
        fibrm(n, fib_dict)
        
    return list(fib_dict.values())


# In[35]:


print(generate_fibrm(35)) # very fast


# In[36]:


print(generate_fibrm(70)) # very fast


# #### OO Recursive Solution with Memoization (very fast)

# In[37]:


class Fib:
    
    def __init__(self):
        self.fib_memo = {0: 0, 1: 1}

    def fib(self, n):
        if n not in self.fib_memo:
            self.fib_memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.fib_memo[n]

    def __str__(self):
        fib_memo_str = ''
        for val in self.fib_memo.values():
            fib_memo_str += str(val) + ', '
        return fib_memo_str


# In[38]:


fib_seq1 = Fib() 

# create an instance of the class; automatically calls __init__() method also 
# translated internally to something like: Fib.__init__(fib_seq1)


# In[39]:


print(fib_seq1) 

# automatically calls the __str__() method
# translated internally to something like: print(Fib.__str__(fib_seq1))


# In[40]:


print(fib_seq1.fib(50))

# translated internally to something like: print(Fib.fib(fib_seq1, 50))


# In[41]:


print(fib_seq1)

