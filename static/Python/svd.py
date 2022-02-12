# Singular Value Decomposition
import numpy as np
from scipy.linalg import svd


class SingularValueDecomposition:
    def __init__(self):
        pass

    @staticmethod
    def transform(time_series_data, n_elements):
        try:
            # Singular Value Decomposition
            U, s, VT = svd(time_series_data)
            # create m x n Sigma matrix
            Sigma = np.zeros((time_series_data.shape[0], time_series_data.shape[1]))
            # populate Sigma with n x n diagonal matrix
            Sigma[: time_series_data.shape[0], : time_series_data.shape[0]] = np.diag(s)
            # select based on the input n_elements to do dimensionality reduction
            Sigma = Sigma[:, : n_elements]
            # Transform and return
            return U @ Sigma
        except Exception as e:
            print(e)
