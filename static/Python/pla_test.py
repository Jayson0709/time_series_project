import pandas as pd
from memory_profiler import profile
import time
import pla

# Get the test data
fifty_words_file_path = r"./test_datasets/50words_TEST"
computer_file_path = r"./test_datasets/Computers_TEST"
earthquake_file_path = r"./test_datasets/Earthquakes_TEST"
ECG_file_path = r"./test_datasets/ECG5000_TEST"
symbols_file_path = r"./test_datasets/Symbols_TEST"

fifty_words_data = pd.read_csv(fifty_words_file_path, header=None).to_numpy()
computers_data = pd.read_csv(computer_file_path, header=None).to_numpy()
earthquake_data = pd.read_csv(earthquake_file_path, header=None).to_numpy()
ECG_data = pd.read_csv(ECG_file_path, header=None).to_numpy()
symbols_data = pd.read_csv(symbols_file_path, header=None).to_numpy()


@profile
def test(segment_size, data):
    start = time.time()
    PLA = pla.PiecewiseLinearAggregateApproximation(segment_size)
    pla_dataset, reduced_data = PLA.transform(data)
    end = time.time()
    print('execution time is {}'.format(end-start))
    return pla_dataset, reduced_data


test(91, fifty_words_data)
test(50, computers_data)
test(80, earthquake_data[2:])
test(100, ECG_data)
test(199, symbols_data)
