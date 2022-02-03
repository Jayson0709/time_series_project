# Discrete Wavelet Transformation
import pywt
import pandas as pd

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()


# the parameter of this function has to be a matrix, cannot be an simple array
def dwt_haar_transformation(time_series_data):
    # Be default, we would use 'haar' as our wavelet object
    # the DWT function will return approximation and detail coefficients
    return pywt.dwt(time_series_data, 'haar')

