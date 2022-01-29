# Discrete Fourier Transformation

import numpy as np
import matplotlib.pyplot as plt


sampling_frequency = 100
time = np.arange(0, 1, 1/sampling_frequency)
sine1 = np.sin(2*np.pi*2*time)
sine2 = np.sin(2*np.pi*7*time)
ts = sine1 + sine2
plt.plot(time, ts, label="Time Series")
plt.plot(time, 2, label="Sine 2 Hz")
plt.plot(time, 7, label="Sine 7 Hz")
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.legend(loc='Best')
plt.show()

fourier_transform = np.fft.fft(ts)/len(ts)
fourier_transform = fourier_transform[range(int(len(ts)/2))]
tp_count = len(ts)
values = np.arange(int(tp_count/2))
time_period = tp_count / sampling_frequency
frequencies = values / time_period
plt.plot(frequencies, abs(fourier_transform))
plt.xlabel('Frequency')
plt.ylabel('Amplitude')
plt.show()


