#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## Problem 1 Statement
# 
# Given a series of revenues and expenses, analyze the profits.

# In[2]:


daily_revenues = [20, 22, 34, 31, 30, 22, 40, 41]
daily_expenses = [10, 12, 14, 21, 40, 2, 10, 14]


# ### Creating a Series

# In[3]:


sr_daily_revenues = pd.Series(daily_revenues)
sr_daily_expenses = pd.Series(daily_expenses)


# In[4]:


sr_daily_revenues


# ### Creating a Dataframe

# In[5]:


df_daily_revenues_and_expenses = pd.DataFrame({'daily_revenue': sr_daily_revenues, 
                                               'daily_expense': sr_daily_expenses})
df_daily_revenues_and_expenses


# ### Basic Data Wrangling: Calculate daily profits

# In[6]:


df_daily_revenues_and_expenses['daily_profit'] = df_daily_revenues_and_expenses.daily_revenue - df_daily_revenues_and_expenses.daily_expense


# ### Basic EDA using a few important properties and methods 

# In[7]:


df_daily_revenues_and_expenses


# In[8]:


df_daily_revenues_and_expenses.shape


# In[9]:


df_daily_revenues_and_expenses.info()


# In[10]:


df_daily_revenues_and_expenses.head()


# In[11]:


df_daily_revenues_and_expenses.tail()


# In[12]:


df_daily_revenues_and_expenses.nunique()


# In[13]:


df_daily_revenues_and_expenses.describe()


# In[14]:


df_daily_revenues_and_expenses.daily_profit.value_counts()


# In[15]:


df_daily_revenues_and_expenses.daily_profit.hist()


# ## Problem 2 Statement
# 
# Explore and understand the data from the last 5 batches of students.

# ### Read the data from given csv file

# In[16]:


file_path = '../data/demo1_historic.csv'

df_student_historic_data = pd.read_csv(file_path)


# ### EDA

# In[17]:


df_student_historic_data.head()


# In[18]:


df_student_historic_data.info()


# In[19]:


df_student_historic_data.nunique()


# In[20]:


df_student_historic_data.describe()


# In[21]:


df_student_historic_data.hist(figsize=(16, 12))


# In[22]:


df_student_historic_data.corr() # Pearson correlation coefficients


# ### Slicing dataframes using absolute numeric index

# In[23]:


df_slice_1 = df_student_historic_data.iloc[1:3, 0:4]
df_slice_1


# In[24]:


type(df_student_historic_data)


# In[25]:


type(df_slice_1)


# In[26]:


df_slice_1.iloc[0, 1] += 10
df_slice_1


# In[27]:


df_student_historic_data.iloc[1:3, 0:4]


# ### Slicing dataframes using names

# In[28]:


df_slice_1.loc[1, 'Age'] -= 10


# In[29]:


df_slice_1


# In[30]:


df_slice_2 = df_student_historic_data.loc[1:3, ['ID', 'Age', 'Is_Married', 'Has_Children']]
df_slice_2


# In[31]:


df_slice_3 = df_student_historic_data.loc[1:3, 'ID':'Has_Children']
df_slice_3


# ### Conditional slicing using loc

# In[32]:


df_slice_4 = df_student_historic_data.loc[df_student_historic_data.Is_Married == 0]
df_slice_4


# In[33]:


df_slice_5 = df_student_historic_data.loc[(df_student_historic_data.Is_Married == 0) & (df_student_historic_data.Drinks_Tea == 0)]
df_slice_5


# ### Conditional slicing using the query method

# In[34]:


df_slice_6 = df_student_historic_data.query('Is_Married == 0')
df_slice_6


# In[35]:


df_slice_7 = df_student_historic_data.query('(Is_Married == 0) and (Drinks_Tea == 0)')
df_slice_7


# ### A few more attributes

# In[36]:


list(df_student_historic_data.columns)


# In[37]:


print(list(df_student_historic_data.columns))


# In[38]:


df_student_historic_data.index


# In[39]:


print(list(df_student_historic_data.index))


# In[40]:


df_student_historic_data.values


# In[41]:


df_student_historic_data.T


# In[42]:


df_student_historic_data.T.info()


# In[43]:


df_student_historic_data.info()


# ### Creating a (deep) copy of a dataframe 

# In[44]:


df_student_historic_data_copy = df_student_historic_data.copy()


# ### Adding a column; apply() method to process data

# In[45]:


df_student_historic_data_copy['Age_in_Days'] = df_student_historic_data_copy.Age.apply(lambda x: int(x * 365.25))
df_student_historic_data_copy.head()


# ### Converting a column's data type using astype()

# In[46]:


df_student_historic_data_copy.Age = df_student_historic_data_copy.Age.astype(float)
df_student_historic_data_copy.head()


# ### A few more methods

# In[47]:


df_student_historic_data_copy.Exam_Result.value_counts()


# In[48]:


df_student_historic_data_copy.Exam_Result.replace(1, 0)


# In[49]:


df_student_historic_data_copy.head()


# In[50]:


df_student_historic_data_copy.Exam_Result.replace(1, 0, inplace=True)


# In[51]:


df_student_historic_data_copy.head()


# In[52]:


df_student_historic_data_copy.Exam_Result = df_student_historic_data_copy.Exam_Result.replace(0, 1)


# In[53]:


df_student_historic_data_copy.Exam_Result.value_counts()


# In[54]:


df_student_historic_data_copy_2 = df_student_historic_data.copy()


# In[55]:


df_student_historic_data_copy_2.Exam_Result.value_counts()


# ### TODO for YOU: replace all 1's to 0's and all 0's to 1's in df_student_historic_data_copy_2

# ### Adding a row to a dataframe

# In[56]:


df_student_historic_data_copy = df_student_historic_data.copy()
df_student_historic_data_copy.head(1)


# In[57]:


df_student_historic_data_copy.loc[1000] = ('S1', 41, 1, 1, 3, 23, 0, 1, 41, 1)


# In[58]:


df_student_historic_data_copy.tail()


# ### Finding and removing duplicate rows

# In[59]:


df_student_historic_data_copy.duplicated()


# In[60]:


df_student_historic_data_copy.duplicated().sum()


# In[61]:


df_student_historic_data_copy.loc[[0, 1000], :]


# In[62]:


df_student_historic_data_copy.drop_duplicates()


# In[63]:


df_student_historic_data_copy


# In[64]:


df_student_historic_data_copy.drop_duplicates(inplace=True)


# In[65]:


df_student_historic_data_copy.loc[1000] = ('S1', 41, 1, 1, 3, 23, 0, 1, 41, 1)


# In[66]:


df_student_historic_data_copy.drop_duplicates(inplace=True, keep='last')


# In[67]:


df_student_historic_data_copy

