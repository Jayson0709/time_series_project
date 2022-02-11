# Singular Value Decomposition
import numpy as np
import pandas as pd
from scipy.linalg import svd

# Get sample data
n = r"../../datasets/Beef_TRAIN"
data = pd.read_csv(n).to_numpy()


class SingularValueDecomposition:
    def __init__(self):
        pass

    # TODO In the webpage, use a slide for user input to define the value of "n_elements"
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
