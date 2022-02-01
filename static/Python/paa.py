# Piecewise Aggregate Approximate
from pyts.approximation import PiecewiseAggregateApproximation
import pandas as pd

# TODO In the webpage, use a slide for user input to define the value of "window_size"

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()


def paa(time_series_data, window_size):
    # PAA transformation based on the input window_size
    # if window_size is 1,
    # if window_size is n, return the average of the time series data.
    paa_set = PiecewiseAggregateApproximation(window_size=window_size)
    X_paa = paa_set.transform(time_series_data)
    return X_paa


print(paa(data, 6))
