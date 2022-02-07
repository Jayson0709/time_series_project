# Adaptive Piecewise Constant Approximation
import numpy as np
import pandas as pd
from sortedcontainers import SortedSet

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()


class Segment:
    start = 0  # inclusive
    end = 0  # exclusive
    mean = 0.0
    error = 0.0
    error_with_next = 0.0
    next = None
    prev = None

    def __init__(self, start, end, mean, error):
        self.start = start
        self.end = end
        self.mean = mean
        self.error = error
        self.error_with_next = np.Inf


class AdaptivePiecewiseConstantApproximation:
    approximate_error = False

    def __init__(self, segments):
        self.segments = segments

    @staticmethod
    def compare_to(x, y, eps):
        if abs(y - x) <= eps:
            return 0
        else:
            return -1 if x < y else 1

    @staticmethod
    def create_segments(values, length):
        first = None
        last = None
        for i in range(length, 2):
            mean = (values[i] + values[i + 1]) / 2
            segment = Segment(i, i + 2, mean, 2 * abs(values[i] - mean))
            if first is None:
                first = segment
                last = first
            else:
                last.next = segment
                segment.prev = last
                last = last.next
        return first

    def create_segment_set(self, values, first_segment):
        segment_set = SortedSet()
        current = first_segment
        while current.next is not None:
            mean = self.get_unified_mean(current, current.next)
            current.error_with_next = self.get_unified_error(current, current.next, values, mean)
            segment_set.add(current)
            current = current.next
        return segment_set

    @staticmethod
    def delete_subsequent_segment(segment, segments_set):
        to_be_deleted = segment.next
        segment.next = to_be_deleted.next
        if to_be_deleted.next is not None:
            to_be_deleted.next.prev = segment
        segments_set.remove(to_be_deleted)

    @staticmethod
    def get_mean_last_pairs(segment, num_of_segments):
        result = [[0.0, 0]] * num_of_segments
        i = 0
        while i < num_of_segments and segment is not None:
            result[i] = [segment.mean, segment.end]
            segment = segment.next
            i += 1
        return result

    @staticmethod
    def get_unified_approximation_error(first_segment, second_segment, mean):
        return first_segment.error + second_segment.error + 2 * abs(first_segment.mean - mean) * (
                first_segment.end - first_segment.start)

    def get_unified_error(self, first_segment, second_segment, time_series_data, mean):
        if abs(mean - first_segment.mean) > pow(2, -30):
            return first_segment.error + second_segment.error
        if AdaptivePiecewiseConstantApproximation.approximate_error:
            return self.get_unified_approximation_error(first_segment, second_segment, mean)
        error = 0.0
        for i in range(first_segment.start, second_segment.end, 1):
            error += abs(time_series_data[i] - mean)
        return error

    @staticmethod
    def get_unified_mean(first_segment, second_segment):
        return (first_segment.mean * (first_segment.end - first_segment.start) + second_segment.mean * (
                second_segment.end - second_segment.start)) / (second_segment.end - first_segment.start)

    def transform(self, time_series_data):
        length = len(time_series_data)
        if length < 2 * self.segments:
            raise ValueError('Input array is too small.')
        num_of_segments = length // 2
        first_segment = self.create_segments(time_series_data, length)
        if num_of_segments > self.segments:
            segment_set = self.create_segment_set(time_series_data, first_segment)
            while num_of_segments > self.segments:
                min_segment = segment_set.pop(0)  # Get the first(lowest) element
                min_segment.mean = self.get_unified_mean(min_segment, min_segment.next)
                min_segment.error = self.get_unified_error(min_segment, min_segment.next, time_series_data, min_segment.mean)
                min_segment.end = min_segment.next.end

                self.delete_subsequent_segment(min_segment, segment_set)

                if min_segment.next is not None:
                    mean = self.get_unified_mean(min_segment, min_segment.next)
                    min_segment.error_with_next = self.get_unified_error(min_segment, min_segment.next, time_series_data,
                                                                         mean)

                if min_segment.prev is not None:
                    segment_set.remove(min_segment.prev)
                    mean = self.get_unified_mean(min_segment.mean, min_segment)
                    min_segment.prev.error_with_next = self.get_unified_error(min_segment.prev, min_segment,
                                                                              time_series_data, mean)
                    segment_set.add(min_segment.prev)

                num_of_segments -= 1
        return self.get_mean_last_pairs(first_segment, num_of_segments)


test = [1, 1, 4, 5, 1, 0, 1, 2, 1]
apca = AdaptivePiecewiseConstantApproximation(3)
result = apca.transform(test)
# TODO address the NoneType issue
print(result)

