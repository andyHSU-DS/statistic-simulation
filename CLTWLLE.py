#!/usr/bin/env python
# coding: utf-8

# # 大數法則

# In[1]:


import random 
import numpy as np


# In[2]:


p = np.random.randint(0,100,size=1000)


# In[3]:


p.mean()


# In[4]:


np.random.choice(p,3)


# In[5]:


times = [x for x in range(1,401,2)]
x_time_mean = []
for x in times:
    print(x)
    sample_mean = []
    for y in range(100):
        sample = np.random.choice(p,x)
        sample_mean.append(sum(sample)/len(sample))
    print(sum(sample_mean)/len(sample_mean))
    x_time_mean.append(sum(sample_mean)/len(sample_mean))


# In[6]:


import matplotlib.pyplot as plt
plt.plot(times,x_time_mean)
plt.axhline(y=p.mean(),ls = '--',lw = 2)


# # 大數法則

# In[7]:


p = np.random.randint(0,100,size=1000)


# In[137]:


sample_error = []
times = [y for y in range(1,401,2)]
for x in times:
    t = []
    for q in range(100):
        sample = np.random.choice(p,x)
        sample_mean = sum(sample)/len(sample)
        t.append(sample_mean)
    t_array = np.array(t)
    t_array_std = np.std(t_array,ddof =1 )
    sample_error.append(t_array_std)


# In[22]:


plt.plot(times,sample_error)


# # 中央極限定理

# In[116]:


from scipy.stats import chi2
df = 78
r = chi2.rvs(df, size=250000)


# In[117]:


import seaborn as sns
sns.distplot(r)


# In[148]:


from scipy.stats import expon
rvs = expon.rvs(size=10000)


# In[158]:


from scipy.stats import norm
import random
rvss = norm.rvs(size = 10000)


# In[172]:


times = [y for y in range(1,40002,20000)]
fig,ax = plt.subplots(1,3,figsize = (20,5))
for x,z in enumerate(times):
    g = []
    for t in range(300):#每次抽50組
        sample = random.choices(r,k = z)
        sample_mean = np.mean(sample)
        g.append(sample_mean)
    g_array = (np.array(g)-np.mean(np.array(r)))/(np.std(np.array(r))/np.sqrt(z))##做正規化
        
    sns.distplot(g_array,ax=ax[x-1])


# In[154]:


rvs


# In[152]:


times


# In[ ]:




