# Piecewise Aggregate Approximate

class PiecewiseAggregateApproximation:
    def __init__(self, _segments):
        self.segments = _segments

    def transform(self, time_series_data):
        try:
            if self.segments < 1:
                raise ValueError('Segments value is too small.')
            length = len(time_series_data)
            if length < self.segments:
                raise ValueError('Input array length is smaller than segments value.')

            reduced_data = [0.0] * self.segments
            segment_size = length / self.segments
            if length % self.segments == 0:
                local_sum = 0
                _n = 0
                for i in range(length):
                    local_sum += time_series_data[i]
                    if (i + 1) % segment_size == 0:
                        reduced_data[_n] = round(local_sum / segment_size, 3)
                        _n += 1
                        if _n == self.segments:
                            break
                        local_sum = 0
            else:
                k = 0
                local_sum = 0
                for i in range(self.segments - 1):
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
                reduced_data[self.segments - 1] = round(local_sum / segment_size, 3)
            paa_dataset = [item for item in reduced_data for _ in range(length // len(reduced_data))]
            if len(paa_dataset) > length:
                paa_dataset = paa_dataset[:length]
            elif len(paa_dataset) < length:
                exceed = length - len(paa_dataset)
                for _ in range(exceed):
                    paa_dataset.append(paa_dataset[-1])
            return paa_dataset, reduced_data
        except Exception as e:
            raise e
