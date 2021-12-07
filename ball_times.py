import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import os

def df_list(size,file_path):
    df_list = []
    for i in range(size):
        i = pd.read_csv(f'{file_path}{i+1}.csv')
        df_list.append(i)
    return df_list
df_noise = pd.concat(df_list(6,'noise'))
print(df_noise['Channel 1 (V)'].mean())
df_times = df_list(30,'ball_time measurments/morten')

test1 =np.array(df_times[0]['Time (s)'])
test2 =np.array(df_times[0]['Channel 1 (V)'])
testgrad = np.gradient(test2)

peak_i = find_peaks(test2,height=4, distance=200)
print(peak_i[0])
# #plt.scatter(data = df_times[5:], y = 'Channel 1 (V)', x = 'Time (s)', s = 5 )
# # # plt.scatter(test1[peak_i], test2[peak_i])
# # # plt.xlim(0.25,1.25)
plt.plot(test2)
plt.xlim(4800,5000)
plt.show()
