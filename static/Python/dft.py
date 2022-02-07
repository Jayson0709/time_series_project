# Discrete Wavelet Transformation
import numpy as np
import pandas as pd

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()


class DiscreteFourierTransformation:

    def __init__(self):
        pass

    # the input parameter can be one array or be one matrix
    @staticmethod
    def transform(time_series_data):
        return np.fft.fftn(time_series_data)
