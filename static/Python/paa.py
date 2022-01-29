# Piecewise Aggregate Approximate

import numpy as np


def paa(time_series, paa_size):
    length = len(time_series)
    if time_series == paa_size:
        return time_series
    if length % paa_size == 0:
        return
    return
