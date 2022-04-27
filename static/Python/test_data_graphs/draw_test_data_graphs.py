import matplotlib.pyplot as plt
import numpy as np

# test datasets' name
dataset_name_list = ["50Words", "Computers", "Earthquakes", "ECG5000", "Symbols"]
patterns = ['/', '\\', '*', '-', 'O', '|', '.']

########################################################################################
# Time and space complexity graphs
width = 0.12
x_axis = np.arange(len(dataset_name_list))

# Time complexity data
apca_time = [0.089, 0.361, 0.123, 0.029, 0.141]
dft_time = [0.009, 0.009, 0.011, 0.012, 0.009]
dwt_time = [0.005, 0.007, 0.009, 0.008, 0.011]
one_d_sax_time = [0.059, 0.061, 0.066, 0.062, 0.069]
paa_time = [0.009, 0.005, 0.011, 0.004, 0.005]
pla_time = [0.012, 0.015, 0.017, 0.013, 0.039]
svd_time = [0.015, 0.011, 0.009, 0.011, 0.015]

plt.subplot(1, 2, 1)
plt.bar(x_axis, apca_time, width, label='APCA', hatch=patterns[0])
plt.bar(x_axis + width, dft_time, width, label='DFT', hatch=patterns[1])
plt.bar(x_axis + width * 2, dwt_time, width, label='DWT', hatch=patterns[2])
plt.bar(x_axis + width * 3, one_d_sax_time, width, label='OneD_SAX', hatch=patterns[3])
plt.bar(x_axis + width * 4, paa_time, width, label='PAA', hatch=patterns[4])
plt.bar(x_axis + width * 5, pla_time, width, label='PLA', hatch=patterns[5])
plt.bar(x_axis + width * 6, svd_time, width, label='SVD', hatch=patterns[6])

plt.yscale('log')
plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title("Average Execution Time of the Implemented Algorithms on the Datasets")
plt.xlabel('Datasets')
plt.ylabel('Execution Time (sec)')
plt.legend()


# Space complexity data
apca_space = [80.4, 81.3, 83.5, 83.5, 83.5]
dft_space = [142.6, 143.5, 145.9, 145.9, 145.9]
dwt_space = [80.4, 81.6, 83.2, 83.4, 83.4]
one_d_sax_space = [149.8, 151.1, 153.1, 153.1, 153.1]
paa_space = [79.7, 80.7, 82.6, 82.9, 82.9]
pla_space = [79.7, 80.8, 82.9, 82.9, 82.9]
svd_space = [106.4, 108.1, 110.4, 110.5, 110.6]

plt.subplot(1, 2, 2)
plt.bar(x_axis, apca_space, width, label='APCA', hatch=patterns[0])
plt.bar(x_axis + width, dft_space, width, label='DFT', hatch=patterns[1])
plt.bar(x_axis + width * 2, dwt_space, width, label='DWT', hatch=patterns[2])
plt.bar(x_axis + width * 3, one_d_sax_space, width, label='OneD_SAX', hatch=patterns[3])
plt.bar(x_axis + width * 4, paa_space, width, label='PAA', hatch=patterns[4])
plt.bar(x_axis + width * 5, pla_space, width, label='PLA', hatch=patterns[5])
plt.bar(x_axis + width * 6, svd_space, width, label='SVD', hatch=patterns[6])
plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Average Memory Usage of the Implemented Algorithms on the Datasets')
plt.xlabel('Datasets')
plt.ylabel('Used Memory (MiB)')
plt.legend()
plt.show()

########################################################################################
# Euclidean and dynamic time warping distances for five datasets
# Euclidean distance data
apca_ed = [26.696, 107.612, 275.576, 17.236, 25.579]
dft_ed = [41.395, 144.807, 287.761, 21.596, 14.135]
dwt_ed = [99.131, 189.964, 217.914, 41.043, 143.509]
one_d_sax_ed = [102.93, 308.565, 309.957, 40.679, 72.523]
paa_ed = [51.235, 150.437, 283.86, 74.981, 40.783]
pla_ed = [16.757, 111.961, 250.157, 13.159, 3.294]
svd_ed = [5495.37, 19345.57, 11596.508, 1167.33, 8296.6523]


plt.subplot(1, 2, 1)
plt.bar(x_axis, apca_ed, width, label='APCA', hatch=patterns[0])
plt.bar(x_axis + width, dft_ed, width, label='DFT', hatch=patterns[1])
plt.bar(x_axis + width * 2, dwt_ed, width, label='DWT', hatch=patterns[2])
plt.bar(x_axis + width * 3, one_d_sax_ed, width, label='OneD_SAX', hatch=patterns[3])
plt.bar(x_axis + width * 4, paa_ed, width, label='PAA', hatch=patterns[4])
plt.bar(x_axis + width * 5, pla_ed, width, label='PLA', hatch=patterns[5])
plt.bar(x_axis + width * 6, svd_ed, width, label='SVD', hatch=patterns[6])

plt.yscale('log')
plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Average Euclidean Distances of the Implemented Algorithms on the Datasets')
plt.xlabel('Datasets')
plt.ylabel('Euclidean Distance')
plt.legend()


# Dynamic time warping distance data
apca_dtw_dis = [35.324, 93.432, 270.136, 16.131, 24.643]
dft_dtw_dis = [34.699, 131.384, 287.932, 17.1642, 9.355]
dwt_dtw_dis = [73.026, 219.857, 185.549, 30.3367, 65.226]
one_d_sax_dtw_dis = [88.65, 302.719, 306.771, 29.954, 45.775]
paa_dtw_dis = [46.146, 140.463, 283.564, 34.618, 29.045]
pla_dtw_dis = [13.102, 15.749, 99.349, 249.876, 13.102]
svd_dtw_dis = [5495.37, 19345.57, 11596.508, 1167.33, 8296.653]

plt.subplot(1, 2, 2)
plt.bar(x_axis, apca_dtw_dis, width, label='APCA', hatch=patterns[0])
plt.bar(x_axis + width, dft_dtw_dis, width, label='DFT', hatch=patterns[1])
plt.bar(x_axis + width * 2, dwt_dtw_dis, width, label='DWT', hatch=patterns[2])
plt.bar(x_axis + width * 3, one_d_sax_dtw_dis, width, label='OneD_SAX', hatch=patterns[3])
plt.bar(x_axis + width * 4, paa_dtw_dis, width, label='PAA', hatch=patterns[4])
plt.bar(x_axis + width * 5, pla_dtw_dis, width, label='PLA', hatch=patterns[5])
plt.bar(x_axis + width * 6, svd_dtw_dis, width, label='SVD', hatch=patterns[6])

plt.yscale('log')
plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Average DTW Distances of the Implemented Algorithms on the Datasets')
plt.xlabel('Datasets')
plt.ylabel('Dynamic Time Warping Distances')
plt.legend()
plt.show()

########################################################################################
# Euclidean and dynamic time warping distances for DFT with different coefficients.
# Euclidean distance data
list1_ed = [44.632, 144.364, 290.920, 30.251, 16.263]
list2_ed = [40.842, 118.312, 272.183, 14.969, 14.887]
list3_ed = [41.550, 115.887, 263.102, 10.652, 14.520]
list4_ed = [40.893, 109.477, 271.379, 10.065, 14.269]
list5_ed = [40.361, 109.611, 259.981, 8.875, 13.947]
list6_ed = [39.389, 108.632, 253.425, 6.605, 14.115]
list7_ed = [37.806, 106.413, 244.446, 0.135, 13.855]

plt.subplot(1, 2, 1)
plt.bar(x_axis, list1_ed, width, label='n_coefficients=20', hatch=patterns[0])
plt.bar(x_axis + width, list2_ed, width, label='n_coefficients=40', hatch=patterns[1])
plt.bar(x_axis + width * 2, list3_ed, width, label='n_coefficients=60', hatch=patterns[2])
plt.bar(x_axis + width * 3, list4_ed, width, label='n_coefficients=80', hatch=patterns[3])
plt.bar(x_axis + width * 4, list5_ed, width, label='n_coefficients=100', hatch=patterns[4])
plt.bar(x_axis + width * 5, list6_ed, width, label='n_coefficients=120', hatch=patterns[5])
plt.bar(x_axis + width * 6, list7_ed, width, label='n_coefficients=140', hatch=patterns[6])

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Euclidean Distances of DFT with Different n_coefficients')
plt.xlabel('Datasets')
plt.ylabel('Euclidean Distance')
plt.legend()


# Dynamic time warping distance data
list1_dtw = [34.568, 129.263, 296.959, 20.700, 8.699]
list2_dtw = [35.031, 112.255, 271.128, 12.509, 10.144]
list3_dtw = [37.096, 113.295, 261.791, 9.637, 11.205]
list4_dtw = [38.270, 108.539, 271.188, 9.646, 11.678]
list5_dtw = [38.630, 109.489, 259.177,8.119, 12.157]
list6_dtw = [38.093, 109.061, 251.924, 6.373, 12.520]
list7_dtw = [36.959, 106.374, 243.237, 0.135, 12.715]

plt.subplot(1, 2, 2)
plt.bar(x_axis, list1_dtw, width, label='n_coefficients=20', hatch=patterns[0])
plt.bar(x_axis + width, list2_dtw, width, label='n_coefficients=40', hatch=patterns[1])
plt.bar(x_axis + width * 2, list3_dtw, width, label='n_coefficients=60', hatch=patterns[2])
plt.bar(x_axis + width * 3, list4_dtw, width, label='n_coefficients=80', hatch=patterns[3])
plt.bar(x_axis + width * 4, list5_dtw, width, label='n_coefficients=100', hatch=patterns[4])
plt.bar(x_axis + width * 5, list6_dtw, width, label='n_coefficients=120', hatch=patterns[5])
plt.bar(x_axis + width * 6, list7_dtw, width, label='n_coefficients=140', hatch=patterns[6])

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Dynamic Time Warping Distances of DFT with Different n_coefficients')
plt.xlabel('Datasets')
plt.ylabel('Dynamic Time Warping Distances')
plt.legend()
plt.show()

########################################################################################
