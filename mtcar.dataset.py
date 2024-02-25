#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


from collections import Counter


# In[4]:


df=pd.read_csv("C:\\Users\\hinaa\\Documents\\Data Analyst\\DataAnalysisUsingPythonproject\\mtcars.csv")
print(df)


# In[5]:


df.isnull()


# In[6]:


df.describe()


# In[7]:


mean_values=df[['mpg', 'cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']].mean()
print(mean_values)


# In[8]:


median_values=df[['mpg', 'cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']].median()
print(median_values)


# In[9]:



mode_values=df[['mpg', 'cyl','disp','hp','drat','wt','qsec','vs','am','gear','carb']].mode()
print(mode_values)


# In[10]:


plt.hist(df["mpg"],bins=8,color= 'yellow',  edgecolor='black')
plt.xlabel=("Miles per Gallon (mpg)")
plt.ylabel=("Frequency")
plt.title("Histogram of MPG")
plt.show()


# In[15]:


plt.bar(df.index, df['gear'], color='skyblue', edgecolor='black')
plt.title('Number of Gears for Each Car')
#plt.xlabel('a')

plt.show()


# In[16]:


vs_counts=df['vs'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(vs_counts, labels=vs_counts.index, autopct='%1.1f%%', colors=['pink', 'yellow'])
plt.title('Distribution of Engine Type (V/S) in Cars')
plt.show()


# In[17]:


numerical_columns = df.select_dtypes(include=['number'])
plt.figure(figsize=(12, 8))
numerical_columns.boxplot(patch_artist=True, showfliers=False)
plt.title("Boxplots of  Mtcar Dataset")
plt.show()


# In[19]:


plt.figure(figsize=(10,6))
plt.scatter(df["mpg"],df["hp"],color="green", alpha=0.7)
plt.title("Scatter Plot of Miles Per Gallon  vs Horsepower ")
#plt.xlabel("Miles per Gallon ")
#plt.ylabel("Horsepower ")
plt.grid(True)
plt.show()


# In[ ]:




