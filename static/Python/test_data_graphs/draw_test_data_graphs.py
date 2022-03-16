import matplotlib.pyplot as plt
import numpy as np

# test datasets' name
dataset_name_list = ["50Words", "Computers", "Earthquakes", "ECG5000", "Symbols"]

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

plt_1 = plt.figure(figsize=(8, 8))

plt.bar(x_axis, apca_time, width, label='APCA')

plt.bar(x_axis + width, dft_time, width, label='DFT')

plt.bar(x_axis + width * 2, dwt_time, width, label='DWT')

plt.bar(x_axis + width * 3, one_d_sax_time, width, label='OneD_SAX')

plt.bar(x_axis + width * 4, paa_time, width, label='PAA')

plt.bar(x_axis + width * 5, pla_time, width, label='PLA')

plt.bar(x_axis + width * 6, svd_time, width, label='SVD')

plt.yscale('log')
plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Execution Time')
plt.xlabel('Datasets')
plt.ylabel('Time')
plt.legend()
plt.show()


# Space complexity data
apca_space = [80.4, 81.3, 83.5, 83.5, 83.5]
dft_space = [142.6, 143.5, 145.9, 145.9, 145.9]
dwt_space = [80.4, 81.6, 83.2, 83.4, 83.4]
one_d_sax_space = [149.8, 151.1, 153.1, 153.1, 153.1]
paa_space = [79.7, 80.7, 82.6, 82.9, 82.9]
pla_space = [79.7, 80.8, 82.9, 82.9, 82.9]
svd_space = [106.4, 108.1, 110.4, 110.5, 110.6]

plt_2 = plt.figure(figsize=(8, 8))

plt.bar(x_axis, apca_space, width, label='APCA')

plt.bar(x_axis + width, dft_space, width, label='DFT')

plt.bar(x_axis + width * 2, dwt_space, width, label='DWT')

plt.bar(x_axis + width * 3, one_d_sax_space, width, label='OneD_SAX')

plt.bar(x_axis + width * 4, paa_space, width, label='PAA')

plt.bar(x_axis + width * 5, pla_space, width, label='PLA')

plt.bar(x_axis + width * 6, svd_space, width, label='SVD')

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Used Memory')
plt.xlabel('Datasets')
plt.ylabel('Memory')
plt.legend()
plt.show()


# Euclidean distance data
apca_ed = [26.696, 107.612, 275.576, 17.236, 25.579]
dft_ed = [41.395, 144.807, 287.761, 21.596, 14.135]
dwt_ed = [99.131, 189.964, 217.914, 41.043, 143.509]
one_d_sax_ed = [102.93, 308.565, 309.957, 40.679, 72.523]
paa_ed = [51.235, 150.437, 283.86, 74.981, 40.783]
pla_ed = [16.757, 111.961, 250.157, 13.159, 3.294]
svd_ed = [5495.37, 19345.57, 11596.508, 1167.33, 8296.6523]

plt_3 = plt.figure(figsize=(8, 8))

plt.bar(x_axis, apca_ed, width, label='APCA')

plt.bar(x_axis + width, dft_ed, width, label='DFT')

plt.bar(x_axis + width * 2, dwt_ed, width, label='DWT')

plt.bar(x_axis + width * 3, one_d_sax_ed, width, label='OneD_SAX')

plt.bar(x_axis + width * 4, paa_ed, width, label='PAA')

plt.bar(x_axis + width * 5, pla_ed, width, label='PLA')

plt.bar(x_axis + width * 6, svd_ed, width, label='SVD')

plt.yscale('log')
plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Euclidean Distances of Different Algorithms')
plt.xlabel('Datasets')
plt.ylabel('Distance')
plt.legend()
plt.show()


# Dynamic time warping distance data
apca_dtw_dis = [35.324, 93.432, 270.136, 16.131, 24.643]
dft_dtw_dis = [34.699, 131.384, 287.932, 17.1642, 9.355]
dwt_dtw_dis = [73.026, 219.857, 185.549, 30.3367, 65.226]
one_d_sax_dtw_dis = [88.65, 302.719, 306.771, 29.954, 45.775]
paa_dtw_dis = [46.146, 140.463, 283.564, 34.618, 29.045]
pla_dtw_dis = [13.102, 15.749, 99.349, 249.876, 13.102]
svd_dtw_dis = [5495.37, 19345.57, 11596.508, 1167.33, 8296.653]

plt_4 = plt.figure(figsize=(8, 8))

plt.bar(x_axis, apca_dtw_dis, width, label='APCA')

plt.bar(x_axis + width, dft_dtw_dis, width, label='DFT')

plt.bar(x_axis + width * 2, dwt_dtw_dis, width, label='DWT')

plt.bar(x_axis + width * 3, one_d_sax_dtw_dis, width, label='OneD_SAX')

plt.bar(x_axis + width * 4, paa_dtw_dis, width, label='PAA')

plt.bar(x_axis + width * 5, pla_dtw_dis, width, label='PLA')

plt.bar(x_axis + width * 6, svd_dtw_dis, width, label='SVD')

plt.yscale('log')
plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Dynamic Time Warping Distances of Different Algorithms')
plt.xlabel('Datasets')
plt.ylabel('Distance')
plt.legend()
plt.show()
