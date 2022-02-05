# Piecewise Aggregate Approximate
import pandas as pd

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()[3]


# TODO In the webpage, use a slide for user input to define the value of "segments"
def paa_transformation(time_series_data, segments):
    # PAA transformation based on the input segments
    if segments < 1:
        raise ValueError('Segments value is too small.')
    length = len(time_series_data)
    if length < segments:
        raise ValueError('input array length is smaller than segments value.')

    reduced_data = [0.0] * segments
    segment_size = length / segments
    if length % segments == 0:
        local_sum = 0
        _n = 0
        for i in range(length):
            local_sum += time_series_data[i]
            if (i + 1) % segment_size == 0:
                reduced_data[_n] = round(local_sum / segment_size, 3)
                _n += 1
                if _n == segments:
                    break
                local_sum = 0
    else:
        k = 0
        local_sum = 0
        for i in range(segments - 1):
            _x = (i + 1) * segment_size - 1
            while k < _x:
                local_sum += time_series_data[k]
                k += 1
            delta = _x - int(_x)
            local_sum += delta * time_series_data[k]
            reduced_data[i] = round(local_sum / segment_size, 3)

            local_sum = (1 - delta) * time_series_data[k]
            k += 1

        while k < length:
            local_sum += time_series_data[k]
            k += 1
        reduced_data[segments - 1] = round(local_sum / segment_size, 3)
    return reduced_data
