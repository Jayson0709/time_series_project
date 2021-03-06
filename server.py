from flask import Flask, render_template, request, flash
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line
from static.Python import apca
from static.Python import dft
from static.Python import dwt
from static.Python import paa
from static.Python import pla
from static.Python import svd
from static.Python import one_d_sax
from static.Python import constant_values
import re
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from dtaidistance import dtw_visualisation as dtw_vis
import numpy as np

# Get the demo data from the datasets
file_path = r"./datasets/Beef_TRAIN"
data = pd.read_csv(file_path, header=None).to_numpy()


# Initiate the app
app = Flask(__name__)


def denoise_data_using_fft(series):
    f_hat = np.fft.rfft(series)
    threshold = 1e8  # the threshold to filter the noise
    frequencies = np.fft.rfftfreq(len(series), d=20e-3/len(series))
    f_hat[frequencies > threshold] = 0
    return np.fft.irfft(f_hat)


def validate_input_segments(string):
    if string == constant_values.EMPTY_STRING:
        raise ValueError('Segments field is required.')
    string = string.strip()
    return int(string)


def validate_input_data(string):
    if string == constant_values.EMPTY_STRING:
        raise ValueError('Input data is empty.')
    string = string.strip()
    if string[-1] == constant_values.COMMA:
        raise ValueError('Input data cannot end with comma.')
    string = string.replace(constant_values.SPACE, constant_values.EMPTY_STRING)
    tokens = string.replace(constant_values.DOT, constant_values.EMPTY_STRING)
    tokens = tokens.split(constant_values.COMMA)
    for token in tokens:
        token = token.replace(constant_values.NEW_LINE, constant_values.EMPTY_STRING)
        if not re.match(r'^[\d,\-]*$', token):
            raise ValueError('Input data can only contain space, comma, and numbers.')
    results = string.split(constant_values.COMMA)
    for i in range(len(results)):
        if constant_values.NEW_LINE in results[i]:
            results[i] = results[i].replace(constant_values.NEW_LINE, constant_values.EMPTY_STRING)
    return results


def draw_euclidean_matching_graph(series1, series2, path):
    dtw_vis.plot_warping(series1, series2, path, filename="./static/images/euclidean_matching.png")


def draw_dtw_matching_graph(series1, series2, path):
    dtw_vis.plot_warping(series1, series2, path, filename="./static/images/dtw_warp.png")


# Calculate the accuracy based on the Euclidean distance
def graph_accuracy_based_on_ed(raw_dataset, transformed_dataset):
    euclidean_distance = 0.0
    temp = transformed_dataset
    if len(raw_dataset) != len(transformed_dataset):
        gap = len(raw_dataset) - len(transformed_dataset)
        for _ in range(gap):
            temp.append(transformed_dataset[-1])
    for i in range(len(raw_dataset)):
        euclidean_distance += abs(raw_dataset[i] - temp[i])
    return euclidean_distance


# Calculate the accuracy based on the Dynamic Time Warping distance
def graph_accuracy_based_on_dtw(raw_dataset, transformed_dataset):
    return fastdtw(raw_dataset, transformed_dataset, dist=euclidean)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/summary")
def summary():
    return render_template("summary.html")


@app.route("/readme")
def readme():
    return render_template("README.html")


@app.route("/visualization")
def visualization():
    return render_template("visualization.html")


@app.route("/visualization/APCA", methods=['GET', 'POST'])
def apca_visualization():
    x_data = []
    y_data = []
    denoised_data = []
    apca_dataset = []
    reduced_data = []
    segments = None
    show_demo_message = True
    if request.method == 'GET':
        segments = 30
        APCA = apca.AdaptivePiecewiseConstantApproximation(segments)
        y_data = data[1][1:]
        x_data = [i for i in range(len(y_data))]
        denoised_data = denoise_data_using_fft(y_data)
        apca_dataset, reduced_data = APCA.transform(denoised_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            segments = validate_input_segments(request.form.get(constant_values.STRING_SEGMENTS))
            APCA = apca.AdaptivePiecewiseConstantApproximation(segments)
            denoised_data = denoise_data_using_fft(y_data)
            apca_dataset, reduced_data = APCA.transform(denoised_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)

    euclidean_distance = graph_accuracy_based_on_ed(y_data, apca_dataset)
    euclidean_match_path = [(x, x) for x in range(len(y_data))]
    draw_euclidean_matching_graph(y_data, apca_dataset, euclidean_match_path)
    dtw_distance, dtw_warp_path = graph_accuracy_based_on_dtw(y_data, apca_dataset)
    draw_dtw_matching_graph(y_data, apca_dataset, dtw_warp_path)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name=constant_values.STRING_ORIGINAL_DATA,
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name=constant_values.STRING_REDUCED_DATA,
                       y_axis=apca_dataset,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_step=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.APCA_TITLE))
    )
    return render_template("apca.html", line_options=line.dump_options(), original_data=y_data, denoised_data=denoised_data,
                           reduced_data=reduced_data, segments=segments, euclidean_distance=euclidean_distance,
                           dtw_distance=dtw_distance, warp_path=dtw_warp_path, boolean_message=show_demo_message)


@app.route("/visualization/DFT", methods=['GET', 'POST'])
def dft_visualization():
    x_data = []
    y_data = []
    denoised_data = []
    reduced_data = []
    show_demo_message = True
    n_coefficients = None
    if request.method == 'GET':
        n_coefficients = 30
        DFT = dft.DiscreteFourierTransformation(n_coefficients)
        y_data = data[2][1:]
        x_data = [i for i in range(len(y_data))]
        denoised_data = denoise_data_using_fft(y_data)
        reduced_data = DFT.transform(denoised_data)
    elif request.method == 'POST':
        try:
            n_coefficients = int(request.form.get(constant_values.STRING_N_COEFFICIENTS))
            DFT = dft.DiscreteFourierTransformation(n_coefficients)
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            denoised_data = denoise_data_using_fft(y_data)
            reduced_data = DFT.transform(denoised_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)

    euclidean_distance = graph_accuracy_based_on_ed(y_data, reduced_data)
    euclidean_match_path = [(x, x) for x in range(len(y_data))]
    draw_euclidean_matching_graph(y_data, reduced_data, euclidean_match_path)
    dtw_distance, dtw_warp_path = graph_accuracy_based_on_dtw(y_data, reduced_data)
    draw_dtw_matching_graph(y_data, reduced_data, dtw_warp_path)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name=constant_values.STRING_ORIGINAL_DATA,
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name=constant_values.STRING_REDUCED_DATA,
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_step=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.DFT_TITLE))
    )
    return render_template("dft.html", line_options=line.dump_options(), original_data=y_data, denoised_data=denoised_data,
                           reduced_data=reduced_data, euclidean_distance=euclidean_distance, dtw_distance=dtw_distance,
                           warp_path=dtw_warp_path, n_coefficients=n_coefficients, boolean_message=show_demo_message)


@app.route("/visualization/DWT", methods=['GET', 'POST'])
def dwt_visualization():
    DWT = dwt.DiscreteHaarWaveletTransformation()
    x_data = []
    y_data = []
    dwt_dataset = []
    denoised_data = []
    reduced_data = []
    coefficients = []
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[3][1:]
        x_data = [i for i in range(len(y_data))]
        denoised_data = denoise_data_using_fft(y_data)
        dwt_dataset, reduced_data, coefficients = DWT.haar_transformation(denoised_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            denoised_data = denoise_data_using_fft(y_data)
            dwt_dataset, reduced_data, coefficients = DWT.haar_transformation(denoised_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)

    euclidean_distance = graph_accuracy_based_on_ed(y_data, dwt_dataset)
    euclidean_match_path = [(x, x) for x in range(len(y_data))]
    draw_euclidean_matching_graph(y_data, dwt_dataset, euclidean_match_path)
    dtw_distance, dtw_warp_path = graph_accuracy_based_on_dtw(y_data, dwt_dataset)
    draw_dtw_matching_graph(y_data, dwt_dataset, dtw_warp_path)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name=constant_values.STRING_ORIGINAL_DATA,
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name=constant_values.STRING_REDUCED_DATA,
                       y_axis=dwt_dataset,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_step=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.DWT_TITLE))
    )
    return render_template("dwt.html", line_options=line.dump_options(), original_data=y_data, denoised_data=denoised_data,
                           reduced_data=reduced_data, coefficients=coefficients, euclidean_distance=euclidean_distance,
                           dtw_distance=dtw_distance, warp_path=dtw_warp_path, boolean_message=show_demo_message)


@app.route("/visualization/PAA", methods=['GET', 'POST'])
def paa_visualization():
    x_data = []
    y_data = []
    denoised_data = []
    reduced_data = []
    paa_dataset = []
    segments = None
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[4][1:]
        x_data = [i for i in range(len(y_data))]
        segments = 20
        PAA = paa.PiecewiseAggregateApproximation(segments)
        denoised_data = denoise_data_using_fft(y_data)
        paa_dataset, reduced_data = PAA.transform(denoised_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            segments = validate_input_segments(request.form.get(constant_values.STRING_SEGMENTS))
            PAA = paa.PiecewiseAggregateApproximation(segments)
            denoised_data = denoise_data_using_fft(y_data)
            paa_dataset, reduced_data = PAA.transform(denoised_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)

    euclidean_distance = graph_accuracy_based_on_ed(y_data, paa_dataset)
    euclidean_match_path = [(x, x) for x in range(len(y_data))]
    draw_euclidean_matching_graph(y_data, paa_dataset, euclidean_match_path)
    dtw_distance, dtw_warp_path = graph_accuracy_based_on_dtw(y_data, paa_dataset)
    draw_dtw_matching_graph(y_data, paa_dataset, dtw_warp_path)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name=constant_values.STRING_ORIGINAL_DATA,
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name=constant_values.STRING_REDUCED_DATA,
                       y_axis=paa_dataset,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_step=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.PAA_TITLE))
    )
    return render_template("paa.html", line_options=line.dump_options(), original_data=y_data, denoised_data=denoised_data,
                           reduced_data=reduced_data, segments=segments, euclidean_distance=euclidean_distance,
                           dtw_distance=dtw_distance, warp_path=dtw_warp_path, boolean_message=show_demo_message)


@app.route("/visualization/PLA", methods=['GET', 'POST'])
def pla_visualization():
    x_data = []
    y_data = []
    denoised_data = []
    reduced_data = []
    pla_dataset = []
    segments = None
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[10][1:]
        x_data = [i for i in range(len(y_data))]
        segments = 10
        PLA = pla.PiecewiseLinearAggregateApproximation(segments)
        denoised_data = denoise_data_using_fft(y_data)
        pla_dataset, reduced_data = PLA.transform(denoised_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            segments = validate_input_segments(request.form.get(constant_values.STRING_SEGMENTS))
            PLA = pla.PiecewiseLinearAggregateApproximation(segments)
            denoised_data = denoise_data_using_fft(y_data)
            pla_dataset, reduced_data = PLA.transform(denoised_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)

    euclidean_distance = graph_accuracy_based_on_ed(y_data, pla_dataset)
    euclidean_match_path = [(x, x) for x in range(len(y_data))]
    draw_euclidean_matching_graph(y_data, pla_dataset, euclidean_match_path)
    dtw_distance, dtw_warp_path = graph_accuracy_based_on_dtw(y_data, pla_dataset)
    draw_dtw_matching_graph(y_data, pla_dataset, dtw_warp_path)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name=constant_values.STRING_ORIGINAL_DATA,
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name=constant_values.STRING_REDUCED_DATA,
                       y_axis=pla_dataset,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_step=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.PLA_TITLE))
    )
    return render_template("pla.html", line_options=line.dump_options(), original_data=y_data, denoised_data=denoised_data,
                           reduced_data=reduced_data, segments=segments, euclidean_distance=euclidean_distance,
                           dtw_distance=dtw_distance, warp_path=dtw_warp_path, boolean_message=show_demo_message)


@app.route("/visualization/SVD", methods=['GET', 'POST'])
def svd_visualization():
    SVD = svd.SingularValueDecomposition()
    x_data = []
    y_data = []
    denoised_data = []
    reduced_data = []
    svd_dataset = []
    n_components = None
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[5][1:]
        x_data = [i for i in range(len(y_data))]
        n_components = 30
        denoised_data = denoise_data_using_fft(y_data)
        svd_dataset, reduced_data = SVD.transform(denoised_data, n_components)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            n_components = int(request.form.get(constant_values.STRING_N_ELEMENTS))
            denoised_data = denoise_data_using_fft(y_data)
            svd_dataset, reduced_data = SVD.transform(denoised_data, n_components)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)

    euclidean_distance = graph_accuracy_based_on_ed(y_data, svd_dataset)
    euclidean_match_path = [(x, x) for x in range(len(y_data))]
    draw_euclidean_matching_graph(y_data, svd_dataset, euclidean_match_path)
    dtw_distance, dtw_warp_path = graph_accuracy_based_on_dtw(y_data, svd_dataset)
    draw_dtw_matching_graph(y_data, svd_dataset, dtw_warp_path)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name=constant_values.STRING_ORIGINAL_DATA,
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name=constant_values.STRING_REDUCED_DATA,
                       y_axis=svd_dataset,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_step=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.SVD_TITLE))
    )
    return render_template("svd.html", line_options=line.dump_options(), original_data=y_data, denoised_data=denoised_data,
                           reduced_data=reduced_data, n_components=n_components, euclidean_distance=euclidean_distance,
                           dtw_distance=dtw_distance, warp_path=dtw_warp_path, boolean_message=show_demo_message)


@app.route("/visualization/ONE_D_SAX", methods=['GET', 'POST'])
def one_d_sax_visualization():
    x_data = []
    y_data = []
    denoised_data = []
    reduced_data = []
    segments = None
    n_sax_symbols_avg = None
    n_sax_symbols_slope = None
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[6][1:]
        x_data = [i for i in range(len(y_data))]
        segments = 10
        n_sax_symbols_avg = 8
        n_sax_symbols_slope = 8
        ONE_D_SAX = one_d_sax.OneDSymbolicAggregateApproximation(segments, n_sax_symbols_avg, n_sax_symbols_slope)
        denoised_data = denoise_data_using_fft(y_data)
        reduced_data = ONE_D_SAX.transform(denoised_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            segments = int(request.form.get(constant_values.STRING_SEGMENTS))
            n_sax_symbols_avg = int(request.form.get(constant_values.STRING_N_SAX_SYMBOLS_AVG))
            n_sax_symbols_slope = int(request.form.get(constant_values.STRING_N_SAX_SYMBOLS_SLOPE))
            ONE_D_SAX = one_d_sax.OneDSymbolicAggregateApproximation(segments, n_sax_symbols_avg, n_sax_symbols_slope)
            denoised_data = denoise_data_using_fft(y_data)
            reduced_data = ONE_D_SAX.transform(denoised_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)

    euclidean_distance = graph_accuracy_based_on_ed(y_data, reduced_data)
    euclidean_match_path = [(x, x) for x in range(len(y_data))]
    draw_euclidean_matching_graph(y_data, reduced_data, euclidean_match_path)
    dtw_distance, dtw_warp_path = graph_accuracy_based_on_dtw(y_data, reduced_data)
    draw_dtw_matching_graph(y_data, reduced_data, dtw_warp_path)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name=constant_values.STRING_ORIGINAL_DATA,
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name=constant_values.STRING_REDUCED_DATA,
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_step=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.ONE_D_SAX_TITLE))
    )
    return render_template("one_d_sax.html", line_options=line.dump_options(), original_data=y_data, denoised_data=denoised_data,
                           reduced_data=reduced_data, segments=segments, n_sax_symbols_avg=n_sax_symbols_avg,
                           n_sax_symbols_slope=n_sax_symbols_slope, euclidean_distance=euclidean_distance,
                           dtw_distance=dtw_distance, warp_path=dtw_warp_path, boolean_message=show_demo_message)


if __name__ == "__main__":
    app.secret_key = constant_values.SECRET_KEY
    app.debug = True
    app.run()
