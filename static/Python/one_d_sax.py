# Symbolic Aggregate Approximation
import numpy as np
from tslearn.piecewise import OneD_SymbolicAggregateApproximation


class OneDSymbolicAggregateApproximation:
    def __init__(self, segments, symbol_avg, symbol_slope):
        self.segments = segments
        self.size_avg = symbol_avg
        self.size_slope = symbol_slope

    def transform(self, time_series_data):
        try:
            if time_series_data.ndim == 1:
                time_series_data = np.reshape(time_series_data, (1, -1))
            one_d_sax = OneD_SymbolicAggregateApproximation(n_segments=self.segments, alphabet_size_avg=self.size_avg, alphabet_size_slope=self.size_avg)
            transformed_data = one_d_sax.fit_transform(time_series_data)
            one_d_sax_dataset_inv = one_d_sax.inverse_transform(transformed_data)
            return one_d_sax_dataset_inv[0].ravel()
        except Exception as e:
            raise e
