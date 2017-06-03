
# coding: utf-8

# In[11]:

import numpy as np
import matplotlib.pyplot as plt
x=np.array(range(200))


# In[5]:

print(x)


# In[7]:

y=np.sin(x)
print(y)


# In[ ]:




# In[ ]:




# In[19]:

cv=open("sub017_baseline_BloodPulse.csv",'r')


# In[20]:

txt=cv.read()


# In[21]:

print(txt)


# In[22]:

freq=np.fft.fft(y)


# In[23]:

print(freq)


# In[24]:

mag=np.absolute(freq)


# In[46]:

#plt.plot(x,mag)
#plt.show()


# In[33]:

dt=txt.split('\n')
#for i in range(len(train)):
#    train[i]=train[i].split(',')
#for j in range(len(test)):
#    test[j]=test[j].split(',')
print(len(dt[2]) )


# In[34]:

d0=dt[0].split(",")
print(d0)


# In[37]:

npd0=np.array(d0[1:])
#npd0E1=npd0[1:]
print(npd0)


# In[38]:

fd0=npd0.astype(float)


# In[39]:

print(fd0)


# In[40]:

fre=np.fft.fft(fd0)


# In[43]:

x=np.array(range(1000))
print(x)


# In[47]:

plt.plot(x,np.absolute(fre))
plt.show()


# In[ ]:



