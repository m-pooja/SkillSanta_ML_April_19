# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 19:03:12 2019

@author: pooja
"""

"""SKILLSANTA_ML _ DAY2"""
# coding: utf-8

# # Introduction to Pandas

# In[37]:

import pandas as pd


# We will open the data set on list of passenger on ill-fated Titanic cruise

# In[38]:

# Use CSV reader  
df = pd.read_csv("TST.csv")


# See more about [read_csv](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html#pandas.read_csv) in pandas documentation

# See first few rows of the data frame

# In[39]:

df.head(15)


# In[40]:

# Display data type of the variable df
type(df)

	
# We can display data types of individual columns of the data read into data frame using *dtypes* 

# In[41]:

df.dtypes


# To find the size or the shape of dataframe object

# In[42]:

df.shape


# To get summarized information about data frame

# In[43]:

df.info()


# We can get statistical description of the data using *describe()* method of the dataframe

# In[44]:

df.describe()


# *describe()* is a part of descriptive statistics methods available to pandas object. See [documentation](http://pandas.pydata.org/pandas-docs/stable/api.html#computations-descriptive-stats) for different available functions.

# ## Referencing

# * Each column of the dataframe is referenced by its "Label".
# * Similar to numpy array we can use index based referencing to reference elements in each column of the data frame.

# In[45]:
df.columns
df['Age']
df['Age'][0:10]


# df['Age'].mean()

# Each column of the dataframe is pandas object series. So all descriptive statistics methods are available to each of the columns.

# In[46]:

# Compute median age
df['Age'].median()


# Check if the above median ignores *NaN* 
# 
# Multiple columns can be referenced by passing a list of columns to dataframe object as shown below.

# In[47]:

MyColumns = ['Sex', 'Pclass','Age']
df[MyColumns].head()


# ## Filtering

# Dataframe object can take logical statements as inputs. Depending upon value of this logical index, it will return the resulting dataframe object.

# In[48]:

# Select all passenger with age greater than 60
df2=df[df['Age']>60]
#df_AgeMoreThan60 = df[df['Age']>60]
df2.head()
df2['Age'].count()

len(df2)
# In[49]:

# Select all passengers with age less than or equal to 15
df_AgeLessThan15=df[df['Age']<=15]

# Number of passengers with Age less than or equal to 15
df_AgeLessThan15['Age'].count()


# Passengers whose age is more than 60 and are male

# Lets see only passengers who are male and above 60 years old

# In[50]:

# Method-1: apply two filters sepeartly
df_AgeMoreThan60 = df[df['Age'] > 60]
temp1 = df_AgeMoreThan60[df['Sex']=='male']
temp1 ['Sex'].head()


# In[51]:

# Method-2: Applying  filters together
SurvivedMaleMoreThan60 = df[(df['Age']>60) & (df['Sex']=='male') ]
dfsmmsixty= df[(df['Age']>60)&(df['Sex']=='male')]                        
SurvivedMaleMoreThan60['Sex'].head()


# In[52]:

# Method-2: Applying two or more filters together
SurvivedMaleMoreThan60 = df[(df['Age']>60) & (df['Sex']=='male') & (df['Survived']==1)]
SurvivedMaleMoreThan60['Sex'].head()


# ## Tabulation

# In[53]:

mySeries = df['Pclass']


# method *[value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html)* will return counts of unique values

# In[54]:

mySeries.value_counts()


# In[55]:

#Cross tabulation
pd.crosstab(df['Sex'],df['Pclass'])


# ## Dropping rows and columns

# In[56]:

# Drop columns
df3=df.drop('Age',axis=1).head() # Note 
#axis=1 indicates that label "Age" is along 
#dimension (index) 1 (0 for rows, 1 for column)


# ## Data frame with row lables and column labels

# In[57]:

#Generate some data
import numpy as np
data = np.random.random(16)
data=  data.reshape(4,4)
data


# In[58]:

# Generate column and row labels
ColumnLables=['One','Two','Three','Four']
RowLables =['Ohio','Colarado','Utah','New York']


# In[59]:

# Use DataFrame method to create dataframe object
df2=pd.DataFrame(data,RowLables,ColumnLables)


# In[60]:

df2.drop('Utah')
df2.shape

# In[61]:

df3=df.dropna()
df3.shape


# ## Combining, merging and concatenating two data frames

# We will create two dataframe objects

# In[62]:

df2=pd.DataFrame(data,RowLables,ColumnLables)
df3=pd.DataFrame(data*4,RowLables,ColumnLables)


# ### **Merge pandas objects **
# by performing a database-style join operation by columns or indexes.
# see [merge documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.merge.html#pandas.merge) for details

# In[63]:
"""

how : {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’
Type of merge to be performed.

left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
inner: use intersection of keys from both frames, similar to a SQL inner join;
 preserve the order of the left keys.
"""
#merge
df4=pd.merge(df2,df3, how='inner') # default inner join
df4


# In[64]:

df5=pd.merge(df2,df3,how='outer')
df5


# ### **Concatenate pandas objects** 
# along a particular axis with optional set logic along the other axes.
# see [concat documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.concat.html#pandas.concat) for details

# In[65]:

pd.concat([df2,df2])


# ## Removing duplicates
# 
# *drop_duplicates* will drop duplicate rows

# In[66]:

df6=pd.concat([df2,df2])

df6.drop_duplicates()


# ## Discreatization and Binning

# ### Cut method
# *[cut](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.cut.html#pandas.cut)* method return indices of half-open bins to which each value of x belongs. See documentation details for different options.

# In[67]:

PassengerAge = PassengerAge.dropna()
Bins = [0, 10,15,30, 40, 60, 80]
PassengerAge = df['Age']

pd.cut(PassengerAge,Bins,labels=['child','crawling','adult','h','g','ht']).head()


# ### Cut with labels for generated bins
# 
# We can also apply "Labels" to each of the generated bin

# In[68]:

PassengerAge = df['Age']

PassengerAge = PassengerAge.dropna()

Bins = [0, 10,15,30, 40, 60, 80]

BinLabels = ['Toddler','Young', 'Adult','In Early 50s', 'In 60s', 'Gerand'] #labels for generated bins

pd.cut(PassengerAge,Bins,labels=BinLabels).head()


# ### Use of precision to cut numbers

# In[69]:

import numpy as np
data = np.random.rand(20)
pd.cut(data,4,precision=2)



#Import the necessary libraries
import pandas as pd
#Import the dataset and assign to a variable
data=pd.read_csv('drinks.csv')
#Display top 5 rows of data
data.head()
#Which continent drinks more beer on average?
a=data.groupby('continent').beer_servings.mean()
print(a.idxmax())
#For each continent print the statistics for wine consumption.
data.groupby('continent').wine_servings.describe()
#Print the mean alcoohol consumption per continent for every column
data.groupby('continent').mean()
#Print the median alcoohol consumption per continent for every column
data.groupby('continent').median()
#Print the mean, min and max values for spirit consumption(output a dataframe).
data.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])




#----------------------------------------------------------------------------
#Import the necessary libraries
import numpy as np
import pandas as pd

#Import the dataset and assign to a variable
data1=pd.read_csv('student-mat.csv', sep=';')
data1.shape
data1.head()
data1.info()
data1.index
a=data1.columns

#Display top 5 rows of data
data1.head()
#For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
stud_alcoh = data1.iloc[: , :12]
data1.columns
stud_alcoh.head()
#Create a lambda function that captalize strings.
c = lambda x: x.capitalize()




#Capitalize both Mjob and Fjob
stud_alcoh['Mjob'].apply(c)
stud_alcoh['Fjob'].apply(c)

#stud_alcoh[['Mjob','Fjob']].apply(c)
#Print the last elements of the data set.
stud_alcoh.tail


#Did you notice the original dataframe is still lowercase? Why is that?
# Fix it and captalize Mjob and Fjob.
stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(c)
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(c)
stud_alcoh.tail()
"""
Create a function called majority that return 
a boolean value to a new 
column called legal_drinker 
(Consider majority as older than 17 years old)
"""

def majority(x):
    if x > 17:
        return True
    else:
        return False
  
        
        
        
stud_alcoh['legal_drinker'] = stud_alcoh['age']
                                  .apply(majority)
stud_alcoh.head()

"""
Multiply every number of the dataset by 10.
I know this makes no sense, 
don't forget it is just an exercise
"""
def times10(x):
    if type(x) is int:
        return 10 * x
    return x

    
stud_alcoh.applymap(times10).head(10)


