import numpy as np
import matplotlib.pyplot as plt

fptr=open("./data/physiology/sub021_baseline_ECG.csv",'r')
raw_data = fptr.read()
ts_data = raw_data.split('\n')#time_split data
len_of_tsdata = len(ts_data)-1
print(len_of_tsdata)
#print(len_of_tsdata)
for i in range(len(ts_data)):
    ts_data[i]=ts_data[i].split(',')

final_data = np.append(ts_data[0][1:],ts_data[1][1:])
for i in range(2,10):
    final_data = np.append(final_data,ts_data[i][1:])
final_data = final_data.astype(float)
time_axix = np.arange(0,10,0.001,float)
plt.plot(time_axix,(final_data))
plt.show()