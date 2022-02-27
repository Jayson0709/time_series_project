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

# Get the demo data from the datasets
file_path = r"./datasets/Beef_TRAIN"
data = pd.read_csv(file_path, header=None).to_numpy()


# Initiate the app
app = Flask(__name__)


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
    if not re.match(r'^[0-9,]*$', string):
        raise ValueError('Input data can only contain space, comma, and numbers.')
    return string.split(constant_values.COMMA)


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
    apca_dataset = []
    reduced_data = []
    show_demo_message = True
    segments = None
    if request.method == 'GET':
        segments = 30
        APCA = apca.AdaptivePiecewiseConstantApproximation(segments)
        y_data = data[3]
        x_data = [i for i in range(len(y_data))]
        apca_dataset, reduced_data = APCA.transform(y_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            segments = validate_input_segments(request.form.get(constant_values.STRING_SEGMENTS))
            APCA = apca.AdaptivePiecewiseConstantApproximation(segments)
            apca_dataset, reduced_data = APCA.transform(y_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)
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
    return render_template("apca.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, segments=segments, boolean_message=show_demo_message)


@app.route("/visualization/DFT", methods=['GET', 'POST'])
def dft_visualization():
    x_data = []
    y_data = []
    reduced_data = []
    show_demo_message = True
    n_coefficients = None
    if request.method == 'GET':
        n_coefficients = 30
        DFT = dft.DiscreteFourierTransformation(n_coefficients)
        y_data = data[3]
        x_data = [i for i in range(len(y_data))]
        reduced_data = DFT.transform(y_data)
    elif request.method == 'POST':
        try:
            n_coefficients = int(request.form.get(constant_values.STRING_N_COEFFICIENTS))
            DFT = dft.DiscreteFourierTransformation(n_coefficients)
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            reduced_data = DFT.transform(y_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)
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
    return render_template("dft.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, n_coefficients=n_coefficients,boolean_message=show_demo_message)


@app.route("/visualization/DWT", methods=['GET', 'POST'])
def dwt_visualization():
    DWT = dwt.DiscreteHaarWaveletTransformation()
    x_data = []
    y_data = []
    dwt_dataset = []
    reduced_data = []
    coefficients = None
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[3]
        x_data = [i for i in range(len(y_data))]
        dwt_dataset, reduced_data, coefficients = DWT.haar_transformation(y_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            dwt_dataset, reduced_data, coefficients = DWT.haar_transformation(y_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)
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
    return render_template("dwt.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, coefficients=coefficients, boolean_message=show_demo_message)


@app.route("/visualization/PAA", methods=['GET', 'POST'])
def paa_visualization():
    x_data = []
    y_data = []
    reduced_data = []
    paa_dataset = []
    segments = None
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[3]
        x_data = [i for i in range(len(y_data))]
        segments = 20
        PAA = paa.PiecewiseAggregateApproximation(segments)
        paa_dataset, reduced_data = PAA.transform(y_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            segments = validate_input_segments(request.form.get(constant_values.STRING_SEGMENTS))
            PAA = paa.PiecewiseAggregateApproximation(segments)
            paa_dataset, reduced_data = PAA.transform(y_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)
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
    return render_template("paa.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, segments=segments, boolean_message=show_demo_message)


@app.route("/visualization/PLA", methods=['GET', 'POST'])
#TODO visualizate the dataset
def pla_visualization():
    x_data = []
    y_data = []
    reduced_data = []
    pla_dataset = []
    segments = 10
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[3][1:]
        x_data = [i for i in range(len(y_data))]
        PLA = pla.PiecewiseLinearAggregateApproximation(segments)
        reduced_data = PLA.transform(y_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            segments = validate_input_segments(request.form.get(constant_values.STRING_SEGMENTS))
            PLA = pla.PiecewiseLinearAggregateApproximation(segments)
            reduced_data = PLA.transform(y_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)
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
    return render_template("pla.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, segments=segments, boolean_message=show_demo_message)


@app.route("/visualization/SVD", methods=['GET', 'POST'])
def svd_visualization():
    SVD = svd.SingularValueDecomposition()
    x_data = []
    y_data = []
    reduced_data = []
    svd_dataset = []
    n_components = 0
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[3]
        x_data = [i for i in range(len(y_data))]
        n_components = 30
        svd_dataset, reduced_data = SVD.transform(y_data, n_components)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            n_components = int(request.form.get(constant_values.STRING_N_ELEMENTS))
            svd_dataset, reduced_data = SVD.transform(y_data, n_components)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)
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
    return render_template("svd.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, n_components=n_components, boolean_message=show_demo_message)


@app.route("/visualization/ONE_D_SAX", methods=['GET', 'POST'])
def one_d_sax_visualization():
    x_data = []
    y_data = []
    reduced_data = []
    segments = None
    n_sax_symbols_avg = None
    n_sax_symbols_slope = None
    show_demo_message = True
    if request.method == 'GET':
        y_data = data[3]
        x_data = [i for i in range(len(y_data))]
        segments = 10
        n_sax_symbols_avg = 8
        n_sax_symbols_slope = 8
        ONE_D_SAX = one_d_sax.OneDSymbolicAggregateApproximation(segments, n_sax_symbols_avg, n_sax_symbols_slope)
        reduced_data = ONE_D_SAX.transform(y_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in validate_input_data(request.form.get(constant_values.STRING_DATA))]
            x_data = [i for i in range(len(y_data))]
            segments = int(request.form.get(constant_values.STRING_SEGMENTS))
            n_sax_symbols_avg = int(request.form.get(constant_values.STRING_N_SAX_SYMBOLS_AVG))
            n_sax_symbols_slope = int(request.form.get(constant_values.STRING_N_SAX_SYMBOLS_SLOPE))
            ONE_D_SAX = one_d_sax.OneDSymbolicAggregateApproximation(segments, n_sax_symbols_avg, n_sax_symbols_slope)
            reduced_data = ONE_D_SAX.transform(y_data)
            show_demo_message = False
        except Exception as e:
            flash(str(e), category=constant_values.STRING_CATEGORY_ERROR)
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
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.SAX_TITLE))
    )
    return render_template("one_d_sax.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, segments=segments, n_sax_symbols_avg=n_sax_symbols_avg, n_sax_symbols_slope=n_sax_symbols_slope, boolean_message=show_demo_message)


if __name__ == "__main__":
    app.secret_key = constant_values.SECRET_KEY
    app.debug = True
    app.run()
