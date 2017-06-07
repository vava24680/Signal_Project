import numpy as np
import matplotlib.pyplot as plt
import datetime

fptr=open("./data/physiology/sub021_film_2_C3.csv",'r')
raw_data = fptr.read()
ts_data = raw_data.split('\n')#time_split data
len_of_tsdata = len(ts_data)-1

for i in range(len(ts_data)):
    ts_data[i]=ts_data[i].split(',')
start_time=datetime.datetime.strptime("13:53:58","%H:%M:%S")
end_time=datetime.datetime.strptime("14:00:11","%H:%M:%S")
total_sec=0
start_index=0;
for i in range(0,len_of_tsdata):
    temp_time=datetime.datetime.strptime(ts_data[i][0]," %H:%M:%S.")
    if(start_time<=temp_time):
        total_sec+=1
        break;
    else:
        start_index=i+1

final_data=np.array(ts_data[start_index][1:])

for i in range(start_index+1,len_of_tsdata):
	temp_time=datetime.datetime.strptime(ts_data[i][0]," %H:%M:%S.")
	if(start_time<=temp_time and temp_time<=end_time):
		total_sec+=1
		final_data = np.append(final_data,ts_data[i][1:])
	else:
		break;

total_amplitude=0.0
total_round=0;
for i in range(start_index,start_index+total_sec):
	if((i-start_index)%6==5):
		temp_arr=np.concatenate((ts_data[i-5][1:],ts_data[i-4][1:],ts_data[i-3][1:],ts_data[i-2][1:],ts_data[i-1][1:],ts_data[i][1:]))
		peak = max(temp_arr)
		down = min(temp_arr)
		total_amplitude+=(peak.astype(float)-down.astype(float))
		total_round+=1
	else:
		continue
#print(total_round)

average_amplitude=total_amplitude/total_round
final_data = final_data.astype(float)
print("Avreage amplitude : ",average_amplitude)
time_asix = np.arange(0,total_sec,0.001,float)
#plt.plot(time_asix,final_data[0:])
#plt.show()