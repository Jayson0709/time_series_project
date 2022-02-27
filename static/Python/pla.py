# Piecewise Linear Aggregate Approximation
import numpy as np
import statistics


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
            raise e

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
            pla_dataset = []
            for i in range(self.segments):
                for j in range(i * segment_size, (i + 1) * segment_size):
                    pla_dataset.append(reduced_data[i][1] * j + reduced_data[i][0])
            return pla_dataset, reduced_data
        except Exception as e:
            raise e
