# Discrete Wavelet Transformation

import pywt
import pandas as pd

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()


def dwt(time_series_data):
    # Be default, we would use 'db1' as our wavelet object
    # the DWT function will return approximation and detail coefficients
    return pywt.dwt(time_series_data, 'db1')


print(dwt(data))

