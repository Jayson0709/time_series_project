# Singular Value Decomposition
import numpy as np
from sklearn.decomposition import TruncatedSVD


class SingularValueDecomposition:
    def __init__(self):
        pass

    @staticmethod
    def transform(time_series_data, n_components):
        try:
            length = len(time_series_data)
            time_series_data = np.array(time_series_data)
            time_series_data = np.reshape(time_series_data, (1, -1))
            # Singular Value Decomposition
            _svd = TruncatedSVD(n_components=n_components)
            _svd.fit(time_series_data)
            reduced_data = _svd.transform(time_series_data)
            return [item for item in reduced_data[0] for _ in range(length // len(reduced_data))]
        except Exception as e:
            raise e
