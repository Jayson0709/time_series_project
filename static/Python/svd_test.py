import pandas as pd
from memory_profiler import profile
import time
import svd

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
def test(data, n_component):
    start = time.time()
    SVD = svd.SingularValueDecomposition()
    svd_dataset, reduced_data = SVD.transform(data, n_component)
    end = time.time()
    print('execution time is {}'.format(end-start))
    return svd_dataset, reduced_data


test(fifty_words_data, 30)
test(computers_data, 10)
test(earthquake_data, 20)
test(ECG_data, 100)
test(symbols_data, 50)
