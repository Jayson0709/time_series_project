## Undergraduate Final Year Project

### Basic Objectives - Finished
*PAA*, *SVD*, *APCA*, *DWT*, *DFT*, *PLA*, and *OneD_SAX* implementation and Visualization
- Visualization similarity -> comparison
- Dynamic warping -> DP performance
- UCR dataset -> time series dataset

### Extensions - Finished
- de-noising - **Faster Fourier Transform**
- Accuracy measurement - **Dynamic Time Warping Distance**

### Criteria
- Performance -> computation time (CPU time and memory requirement)
- Accuracy -> Euclidean Distance, Dynamic Time Warping Distance

### Framework
Flask, Bootstrap

### Graph Library & Template Engine
pyecharts & Jinja

### To run the project
Install the dependencies and modules:
```
# Windows
pip -r install requirements.txt
# Mac & Linux
pip3 -r install requirements.txt
```

After install the dependencies and modules, simply run the following command:
```
# Windows
python server.py
# Mac & Linux
python3 server.py
```
The app should be on and running at: http://127.0.0.1:5000/

### To stop the project
It is really easy to stop the project on the terminal.
Simply use the following command on the terminal that you run
the project.
```
# Windows & Linux
Ctrl + C

# Mac 
control + C
```

### Code Structure
```
Project root:  
|
|--- datasets  
|       |--- Beef_TRAIN (Demo data, from UCR datasets)
|--- static
|       |--- css
|       |       |--- style.css (the CSS style sheet)
|       |--- images (demo images used for the project)
|       |       |--- APCA.png
|       |       |--- DFT.png
|       |       |--- dimensionality_reduction_graph.png
|       |       |--- dtw_warp.png (the changing dtw warping path image)
|       |       |--- DWT.png
|       |       |--- euclidean_matching.png (the changing Euclidean matching image)
|       |       |--- OneD_SAX.png
|       |       |--- PAA.png
|       |       |--- PLA.png
|       |       |--- SVD.png
|       |       |--- time_series_graph.png
|       |--- JavaScript
|       |       |--- echarts.min.js (echarts library for pyecharts)
|       |--- Python (Python scripts for algorithm implementation)
|       |       |--- test_data_graphs
|       |       |       |--- draw_test_data_graphs.py (code to draw test graphs)
|       |       |--- test_datasets (five UCR datasets for algorithms analysis)
|       |       |       |--- 50words_TEST
|       |       |       |--- Computers_TEST
|       |       |       |--- Earthquakes_TEST
|       |       |       |--- ECG5000_TEST
|       |       |       |--- Symbols_TEST
|       |       |--- apca.py
|       |       |--- apca_test.py
|       |       |--- constant_values.py
|       |       |--- dft.py
|       |       |--- dft_test.py
|       |       |--- dwt.py
|       |       |--- dwt_test.py
|       |       |--- one_d_sax.py
|       |       |--- one_d_sax_test.py
|       |       |--- paa.py
|       |       |--- paa_test.py
|       |       |--- pla.py
|       |       |--- pla_test.py
|       |       |--- svd.py
|       |       |--- svd_test.py
|--- templates (the folder contains all html files for each page) 
|       |--- apca.html 
|       |--- base.html 
|       |--- dft.html 
|       |--- dwt.html 
|       |--- index.html 
|       |--- one_d_sax.html 
|       |--- paa.html 
|       |--- pla.html 
|       |--- README.html 
|       |--- summary.html 
|       |--- svd.html 
|       |--- visualization.html 
|--- README.md (markdown file for the project)
|--- requirements.txt (required libraries and modules for the project)
|--- server.py (the backend code file that contains all the required APIs)
```
