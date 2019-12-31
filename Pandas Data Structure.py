#!/usr/bin/env python
# coding: utf-8

# # Pandas Series

# In[1]:


# pandas series
# must need to import pandas
import pandas as pd
obj=pd.Series([4,6,7,6])
print (obj)


# # pandas Series has two things in one object¶
# 

# # 1 values

# # 2 index

# In[2]:


sales=pd.Series([100,200,300,400])
print(sales.values)
print(sales.index)


# In[3]:


sales=pd.Series([100,200,300,400] ,index=["jan","feb","march","april"])
print(sales)
print(sales.values)
print(sales.index)


# In[4]:


sales=pd.Series([100,200,300,400],index=["Jan","Feb","Mar","Apr"],name="4 month sales")
sales


# # create a pandas series to store a canteen data to hold values of how many sandwithes are sold each days (one week)

# In[5]:


Sw=pd.Series([20, 30, 20, 25, 30, 40, 0],index = ['mon', 'tue', 'wed', 'thr','fri', 'sat', 'sun'])
Sw


# In[6]:


print(Sw[1])
print(Sw["mon"])
print(Sw["tue"])


# In[7]:


print(Sw[[3,5]])
print(Sw[["mon","sun"]])


# # for providing multipe index for selecting element in an pd series, use array notation¶# 

# In[8]:


print(Sw>20)
print(Sw[Sw>20])
print(Sw[Sw<10])
print()


# In[9]:


Sw*2
Sw=Sw*2
print(Sw)


# In[10]:


print(Sw)


# In[11]:


Sw=Sw/2
print(Sw)


# In[12]:


print("mon" in Sw)
print("monday" in Sw)


# In[13]:


#taking input from numpy arrays
import numpy as np

arr=np.array([4,5,6,7,8])
ind=np.array(["a","b","c","d","e"])
obj=pd.Series(arr,index=ind,name="data from numpy array")
print(obj)


# In[14]:


"b" in obj


# In[15]:



sdata={"sindh":35000,"kpk":3000,"punjab":4500,"Balochistan":2000} #dic
tax=pd.Series(sdata) #data from numpy dic
print(tax)
print(tax.index)
print(tax.values)


# In[16]:


tax1=pd.Series(sdata,index=["punjab","sindh","kpk","Balochistan"])
print(tax1)


# In[17]:


tax1=pd.Series(sdata,index=["punjab","sindh","kpk","Balochistan","GB"])#NaN means values does not exist in pandas series.
print(tax1)
print(pd.isnull(tax1))
tax1.isnull()


# # Pandas Data frame

# In[18]:


import pandas as pd 
apple=pd.Series([3,4,5,6])
orange=pd.Series([6,5,7,8])
data={"apple":apple,"orange":orange}
obj=pd.DataFrame(data)   #DataFrame is used for handle multi dimensional array
print (obj)


# In[19]:


data={"state":["ohio","ohio","ohio","nevada","nevada","nevada"],
     "year":[2000,2001,2003,2004,2005,2006],
     "pop":[1.3,1.4,1.5,3.2,6.1,4.2]}
frame=pd.DataFrame(data,index=["1st","2nd","3rd","4th","5th","6th"])
print(frame)


# In[20]:


frame.head(6)


# In[21]:



frame1=pd.DataFrame(data,index=["1st","2nd","3rd","4th","5th","6th"],  columns=['year','state','pop'])
frame1.head()


# In[22]:


frame2=pd.DataFrame(data,index=["1st","2nd","3rd","4th","5th","6th"], columns=["year","state","pop","debt"])
frame2.head()


# In[23]:


frame2.columns


# In[24]:


frame2.index


# In[25]:


frame2.debt


# In[26]:


frame2["state"] # dictionary like notation to access or extract


# In[27]:


#there is another method ,attribute style of accessing 
frame2.state


# In[28]:


frame2.loc["1st"]#in pandas loc function is used for access all detail from any row and columns


# In[29]:


frame2["debt"]=16.5 # column can be modified
frame2


# In[39]:


import pandas as pd
import numpy as np
data={"state":["ohio","ohio","ohio","nevada","nevada","nevada"],
     "year":[2000,2001,2003,2004,2005,2006],
     "pop":[1.3,1.4,1.5,3.2,6.1,4.2]}
A=pd.DataFrame(data, columns=["state","year","pop","debt"],index=["one","two","three","four","five","six"])

B =(len(A))
rng=np.arange(B)
A["debt"]= rng
A


# In[50]:


a=np.random.randn(4,4)


# In[51]:


a


# In[84]:


f=pd.DataFrame(np.random.randn(4,4), columns=list("abcd"),index=["otah","ohio","texas","origin"])
print (f)
#print(np.abs(f))
#print(f["d"].min())
#print(f["d"].max())
#print(f["d"].max()-f["d"].min())

d=lambda x: x.max() - x.min()
df=f.apply(d)
print(df,type(df))
#df=f.apply(d,axis=1)
#print(df)

#def min_max(x):
#    minimum=x.min()
 #   maximum=x.max()
 #   return pd.Series([x.min(),x.max()],index=["min","max"])
#df=f.apply(min_max)
#print (df,type(df))
    


# In[ ]:




