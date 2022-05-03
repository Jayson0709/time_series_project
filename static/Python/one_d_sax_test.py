import pandas as pd
from memory_profiler import profile
import time
import one_d_sax
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

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


# Implement similarity search on two sets of time series data, calculate the accuracy based on Euclidean distance
def graph_accuracy_based_on_ed(raw_dataset, transformed_dataset):
    euclidean_distance = 0.0
    for i in range(len(raw_dataset)):
        euclidean_distance += abs(raw_dataset[i] - transformed_dataset[i])
    return euclidean_distance


# Implement similarity search on two sets of time series data, calculate the accuracy based on Dynamic Time Warping
def graph_accuracy_based_on_dtw(raw_dataset, transformed_dataset):
    return fastdtw(raw_dataset, transformed_dataset, dist=euclidean)


@profile
def test(data):
    start = time.time()
    ONE_D_SAX = one_d_sax.OneDSymbolicAggregateApproximation(30, 5, 5)
    reduced_data = ONE_D_SAX.transform(data)
    end = time.time()
    print('execution time is {}'.format(end-start))
    euclidean_distance = graph_accuracy_based_on_ed(data, reduced_data)
    dtw_distance, warping_path = graph_accuracy_based_on_dtw(data, reduced_data)
    print('Euclidean distance is {}'.format(euclidean_distance))
    print('Dynamic Time Warping distance is {}'.format(dtw_distance))


test(fifty_words_data[1][1:])
test(computers_data[1][1:])
test(earthquake_data[1][1:])
test(ECG_data[1][1:])
test(symbols_data[1][1:])
