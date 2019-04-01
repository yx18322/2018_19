import numpy as np
import matplotlib.pyplot as plt

def load_data(filename,T):
    data_array = [T(line.strip()) for line in open(filename, 'r')]
    return data_array

def compute_sta(stim, rho, width,interval):
    num_timesteps = int(width/interval)
    sta_ = zeros(num_timesteps)
    spike_times = np.nonzero(rho)[0]           
    num = len(spike_times)
    for i in range(0, num_timesteps):
        x=0
        window=[]
        j=0
        while j<num:
            if spike_times[j]<i:
                x+=1
            window.append(stim[spike_times[j]-i])
            j+=1
        sta_[i]=sum(window)/(num-x)
    return sta_

ms=0.001
interval=2*ms
width = 100*ms

stimulus=load_data("stim.dat",float)


spikes=load_data("rho.dat",int)


sta = compute_sta(stimulus, spikes, width, interval)
time = np.arange(0,width/interval)
print(sta)
print(len(sta))
print(len(stimulus))
print(stimulus[0:5])
print(len(spikes))
print(spikes[0:5])

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')
plt.show()

