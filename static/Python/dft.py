# Discrete Wavelet Transformation
import numpy as np
from pyts.approximation import DiscreteFourierTransform


class DiscreteFourierTransformation:

    def __init__(self, n_coefficients):
        self.n_coefficients = n_coefficients

    def transform(self, time_series_data):
        try:
            time_series_data = np.array(time_series_data)
            if self.n_coefficients < 1:
                raise ValueError('n_coefficients must be greater than or equal to 1 if n_coefficients is an integer.')
            if time_series_data.size < self.n_coefficients:
                raise ValueError('n_coefficients must be lower than or equal to the length of the input array.')
            if time_series_data.ndim == 1:
                time_series_data = np.reshape(time_series_data, (1, -1))
            # DFT transformation
            _dft = DiscreteFourierTransform(n_coefs=self.n_coefficients, norm_mean=False, norm_std=False)
            X_dft = _dft.fit_transform(time_series_data)

            # Compute the inverse transformation
            if self.n_coefficients % 2 == 0:
                real_idx = np.arange(1, self.n_coefficients, 2)
                imag_idx = np.arange(2, self.n_coefficients, 2)
                X_dft_new = np.c_[
                    X_dft[:, :1],
                    X_dft[:, real_idx] + 1j * np.c_[X_dft[:, imag_idx],
                                                    np.zeros((time_series_data.shape[0],))]
                ]
            else:
                real_idx = np.arange(1, self.n_coefficients, 2)
                imag_idx = np.arange(2, self.n_coefficients + 1, 2)
                X_dft_new = np.c_[
                    X_dft[:, :1],
                    X_dft[:, real_idx] + 1j * X_dft[:, imag_idx]
                ]
            X_irfft = np.fft.irfft(X_dft_new, time_series_data.shape[1])
            result = []
            for num in X_irfft[0]:
                result.append(num)
            return result
        except Exception as e:
            raise e
