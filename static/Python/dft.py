# Discrete Wavelet Transformation
import numpy as np
import pandas as pd

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()


# the input parameter can be one array or be one matrix
def dft_transformation(time_series_data):
    return np.fft.fftn(time_series_data)

