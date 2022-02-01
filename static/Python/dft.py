# Discrete Wavelet Transformation
import numpy as np
import pandas as pd

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()


def dft(time_series_data):
    return np.fft.fftn(time_series_data)


print(dft(data))
