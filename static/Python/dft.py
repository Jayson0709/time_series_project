# Discrete Wavelet Transformation
import numpy as np


class DiscreteFourierTransformation:

    def __init__(self):
        pass

    # the input parameter can be one array or be one matrix
    @staticmethod
    def transform(time_series_data):
        try:
            return np.fft.fftn(time_series_data)
        except Exception as e:
            raise e
