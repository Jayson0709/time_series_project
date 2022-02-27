# Discrete Wavelet Transformation
import pywt


class DiscreteHaarWaveletTransformation:
    def __init__(self):
        pass

    # the parameter of this function has to be a matrix, cannot be an simple array
    @staticmethod
    def haar_transformation(time_series_data):
        try:
            length = len(time_series_data)
            # Be default, we would use 'haar' as our wavelet object
            # the DWT function will return approximation and detail coefficients
            reduced_data, coefficients = pywt.dwt(time_series_data, 'haar')
            dwt_dataset = [item for item in reduced_data for _ in range(2)]
            if len(dwt_dataset) > length:
                dwt_dataset = dwt_dataset[:length]
            elif len(dwt_dataset) < length:
                exceed = length - len(dwt_dataset)
                for _ in range(exceed):
                    dwt_dataset.append(dwt_dataset[-1])
            return dwt_dataset, reduced_data, coefficients
        except Exception as e:
            raise e
