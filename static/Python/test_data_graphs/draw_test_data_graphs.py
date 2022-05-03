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
plt.bar(x_axis, list1_ed, width, label='N=20', hatch=patterns[0])
plt.bar(x_axis + width, list2_ed, width, label='N=40', hatch=patterns[1])
plt.bar(x_axis + width * 2, list3_ed, width, label='N=60', hatch=patterns[2])
plt.bar(x_axis + width * 3, list4_ed, width, label='N=80', hatch=patterns[3])
plt.bar(x_axis + width * 4, list5_ed, width, label='N=100', hatch=patterns[4])
plt.bar(x_axis + width * 5, list6_ed, width, label='N=120', hatch=patterns[5])
plt.bar(x_axis + width * 6, list7_ed, width, label='N=140', hatch=patterns[6])

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Euclidean Distances of DFT with Different n_coefficients (N)')
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
plt.bar(x_axis, list1_dtw, width, label='N=20', hatch=patterns[0])
plt.bar(x_axis + width, list2_dtw, width, label='N=40', hatch=patterns[1])
plt.bar(x_axis + width * 2, list3_dtw, width, label='N=60', hatch=patterns[2])
plt.bar(x_axis + width * 3, list4_dtw, width, label='N=80', hatch=patterns[3])
plt.bar(x_axis + width * 4, list5_dtw, width, label='N=100', hatch=patterns[4])
plt.bar(x_axis + width * 5, list6_dtw, width, label='N=120', hatch=patterns[5])
plt.bar(x_axis + width * 6, list7_dtw, width, label='N=140', hatch=patterns[6])

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Dynamic Time Warping Distances of DFT with Different n_coefficients (N)')
plt.xlabel('Datasets')
plt.ylabel('Dynamic Time Warping Distance')
plt.legend()
plt.show()

########################################################################################
# Euclidean and dynamic time warping distances for APCA with different segment size.
# Euclidean distance data
list1_ed = [114.30216564135038, 128.87753786356691, 301.7009037235459, 43.92926100536797, 74.63850814164154]
list2_ed = [50.334325606547594, 107.83068626356699, 280.41750887542264, 43.92926100536797, 74.63850814164154]
list3_ed = [36.69634247619049, 107.61148631006003, 275.5755933870319, 43.92926100536797, 74.63850814164154]
list4_ed = [29.942066492857155, 107.3993403581866, 264.5300267752992, 43.92926100536797, 74.63850814164154]
list5_ed = [25.941021564285737, 107.21283465795332, 264.12059263719243, 43.92926100536797, 74.63850814164154]
list6_ed = [23.82810214166666, 93.59959110644256, 257.67587393225404, 39.18456588822512, 67.4439069362147]
list7_ed = [22.463992100000024, 106.76169840247198, 262.21922737835814, 43.92926100536797, 74.63850814164154]

plt.subplot(1, 2, 1)
plt.bar(x_axis, list1_ed, width, label='segment_size=10', hatch=patterns[0])
plt.bar(x_axis + width, list2_ed, width, label='segment_size=20', hatch=patterns[1])
plt.bar(x_axis + width * 2, list3_ed, width, label='segment_size=30', hatch=patterns[2])
plt.bar(x_axis + width * 3, list4_ed, width, label='segment_size=40', hatch=patterns[3])
plt.bar(x_axis + width * 4, list5_ed, width, label='segment_size=50', hatch=patterns[4])
plt.bar(x_axis + width * 5, list6_ed, width, label='segment_size=60', hatch=patterns[5])
plt.bar(x_axis + width * 6, list7_ed, width, label='segment_size=70', hatch=patterns[6])

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Euclidean Distances of APCA with Different Segment Size')
plt.xlabel('Datasets')
plt.ylabel('Euclidean Distance')
plt.legend()


# Dynamic time warping distance data
list1_dtw = [73.09677197993668, 114.70506880642404, 308.28328420169146, 39.18456588822512, 67.4439069362147]
list2_dtw = [46.284366124404684, 92.90768762864634, 273.6250586585054, 39.18456588822512, 67.4439069362147]
list3_dtw = [35.32409874404763, 93.43220825291716, 270.13641167275415, 39.18456588822512, 67.4439069362147]
list4_dtw = [29.20605112182542, 93.67482158186576, 257.34219118669085, 39.18456588822512, 67.4439069362147]
list5_dtw = [25.464557415476197, 93.4209467781154, 257.1374741176378, 39.18456588822512, 67.4439069362147]
list6_dtw = [23.82810214166666, 93.59959110644256, 257.67587393225404, 39.18456588822512, 67.4439069362147]
list7_dtw = [22.26243451666669, 92.78575202471839, 255.99270270604416, 39.18456588822512, 67.4439069362147]

plt.subplot(1, 2, 2)
plt.bar(x_axis, list1_dtw, width, label='segment_size=10', hatch=patterns[0])
plt.bar(x_axis + width, list2_dtw, width, label='segment_size=20', hatch=patterns[1])
plt.bar(x_axis + width * 2, list3_dtw, width, label='segment_size=30', hatch=patterns[2])
plt.bar(x_axis + width * 3, list4_dtw, width, label='segment_size=40', hatch=patterns[3])
plt.bar(x_axis + width * 4, list5_dtw, width, label='segment_size=50', hatch=patterns[4])
plt.bar(x_axis + width * 5, list6_dtw, width, label='segment_size=60', hatch=patterns[5])
plt.bar(x_axis + width * 6, list7_dtw, width, label='segment_size=70', hatch=patterns[6])

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Dynamic Time Warping Distances of APCA with Different Segment Size')
plt.xlabel('Datasets')
plt.ylabel('Dynamic Time Warping Distance')
plt.legend()
plt.show()

########################################################################################
# Euclidean and dynamic time warping distances for PAA with different segment size.
# Euclidean distance data
list1_ed = [89.03159109999999, 211.75621020000014, 304.99461999999954, 43.61715720000001, 72.9420363]
list2_ed = [94.45988690000003, 175.50753020000016, 295.7156199999997, 43.61715720000001, 72.9420363]
list3_ed = [51.23511890000004, 150.4368502000002, 283.8576199999998, 43.61715720000001, 72.9420363]
list4_ed = [185.07555889999995, 125.10680980000006, 318.4676200000016, 43.61715720000001, 72.9420363]
list5_ed = [137.8170709, 195.4940497999999, 298.3686200000002, 43.61715720000001, 72.9420363]
list6_ed = [183.72449890000013, 113.32566999999996, 314.3943000000004, 43.61715720000001, 72.9420363]
list7_ed = [264.21475910000015, 192.07414980000016, 292.4786200000006, 43.61715720000001, 72.9420363]

plt.subplot(1, 2, 1)
plt.bar(x_axis, list1_ed, width, label='segment_size=10', hatch=patterns[0])
plt.bar(x_axis + width, list2_ed, width, label='segment_size=20', hatch=patterns[1])
plt.bar(x_axis + width * 2, list3_ed, width, label='segment_size=30', hatch=patterns[2])
plt.bar(x_axis + width * 3, list4_ed, width, label='segment_size=40', hatch=patterns[3])
plt.bar(x_axis + width * 4, list5_ed, width, label='segment_size=50', hatch=patterns[4])
plt.bar(x_axis + width * 5, list6_ed, width, label='segment_size=60', hatch=patterns[5])
plt.bar(x_axis + width * 6, list7_ed, width, label='segment_size=70', hatch=patterns[6])

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.xlabel('Datasets')
plt.title('Euclidean Distances of PAA with Different Segment Size')
plt.ylabel('Euclidean Distance')
plt.legend()


# Dynamic time warping distance data
list1_dtw = [69.12685309999996, 172.9248302000001, 304.8537199999994, 33.555297200000005, 66.1219023]
list2_dtw = [56.362988800000004, 143.80399019999993, 282.41400999999985, 33.555297200000005, 66.1219023]
list3_dtw = [46.14556690000005, 140.4633306000002, 283.5645900000001, 33.555297200000005, 66.1219023]
list4_dtw = [40.26489609999993, 118.14280950000007, 281.83908000000133, 33.555297200000005, 66.1219023]
list5_dtw = [36.43502210000003, 111.33529980000003, 265.1227400000008, 33.555297200000005, 66.1219023]
list6_dtw = [32.702722899999905, 101.95855979999993, 249.95213000000146, 33.555297200000005, 66.1219023]
list7_dtw = [28.953942899999948, 109.84621039999986, 225.74204000000083, 33.555297200000005, 66.1219023]


plt.subplot(1, 2, 2)
plt.bar(x_axis, list1_dtw, width, label='segment_size=10', hatch=patterns[0])
plt.bar(x_axis + width, list2_dtw, width, label='segment_size=20', hatch=patterns[1])
plt.bar(x_axis + width * 2, list3_dtw, width, label='segment_size=30', hatch=patterns[2])
plt.bar(x_axis + width * 3, list4_dtw, width, label='segment_size=40', hatch=patterns[3])
plt.bar(x_axis + width * 4, list5_dtw, width, label='segment_size=50', hatch=patterns[4])
plt.bar(x_axis + width * 5, list6_dtw, width, label='segment_size=60', hatch=patterns[5])
plt.bar(x_axis + width * 6, list7_dtw, width, label='segment_size=70', hatch=patterns[6])

plt.xticks(x_axis + width * 3, dataset_name_list)
plt.title('Dynamic Time Warping Distances of PAA with Different Segment Size')
plt.xlabel('Datasets')
plt.ylabel('Dynamic Time Warping Distance')
plt.legend()
plt.show()
