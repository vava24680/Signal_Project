
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

cv=open("./data/physiology/sub021_baseline_C1.csv",'r')

txt=cv.read()


#print(txt)


freq=np.fft.fft(y)


#print(freq)

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
#print(len(dt[2]) )


d0=dt[0].split(",")
#print(d0)


npd0=np.array(d0[1:])
#npd0E1=npd0[1:]
#print(npd0)

print(len(npd0))
fd0=npd0.astype(float)


#print(fd0)
print(len(fd0))

fre=np.fft.fft(fd0)
print(len(fre))

x=np.array(range(1000))
#print(x)


#plt.plot(x,np.absolute(fre))
#plt.show()


# In[ ]:



