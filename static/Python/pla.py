# Piecewise Linear Aggregate Approximation
import pandas as pd
import numpy as np
import statistics

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()[3][1:]


class PiecewiseLinearAggregateApproximation:
    def __init__(self, segments):
        self.segments = segments

    @staticmethod
    def calculate_covariance(array_x, array_y, bias=False):
        try:
            result = 0.0
            length = len(array_x)
            if length != len(array_y):
                raise ValueError('length of array x is not equal to array y --- dimensions mismatch.')
            elif length < 2:
                raise ValueError('array x is too small --- insufficient observed points in sample.')
            else:
                x_mean = np.mean(array_x)
                y_mean = np.mean(array_y)
                for i in range(length):
                    x_deviation = array_x[i] - x_mean
                    y_deviation = array_y[i] - y_mean
                    result += (x_deviation * y_deviation - result) / (i + 1)
            return result * (length / (length - 1)) if bias else result
        except Exception as e:
            print(e)

    # TODO In the webpage, use a slide for user input to define the value of "segments"
    def transform(self, time_series_data):
        try:
            length = len(time_series_data)
            if length < self.segments:
                raise ValueError('input array length is smaller than segments value.')

            if length % self.segments != 0:
                raise ValueError('input array length is not divisible to segments.')

            reduced_data = [[0.0, 0.0]] * self.segments
            segment_size = length // self.segments
            x = [0.0] * segment_size
            for i in range(segment_size):
                x[i] = i + 1

            variance = statistics.variance(x)
            for i in range(self.segments):
                y = time_series_data[i * segment_size: (i + 1) * segment_size]
                covariance = self.calculate_covariance(x, y, True)
                mean = np.mean(y)
                reduced_data[i] = [mean, covariance / variance]

            # each of element of the array will be like a list of [mean, slope]
            return reduced_data
        except Exception as e:
            print(e)
