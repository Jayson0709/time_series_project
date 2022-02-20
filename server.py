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
from static.Python import constant_values

# Get the demo data from the datasets
file_path = r"./datasets/Beef_TRAIN"
data = pd.read_csv(file_path, header=None).to_numpy()


# Initiate the app
app = Flask(__name__)


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
    reduced_data = []
    show_demo_message = True
    segments = None
    if request.method == 'GET':
        segments = 12
        APCA = apca.AdaptivePiecewiseConstantApproximation(segments)
        x_data = []
        y_data = data[3]
        reduced_data = APCA.transform(y_data)
    elif request.method == 'POST':
        try:
            x_data = []
            y_data = [float(i) for i in request.form.get(constant_values.STRING_DATA).replace(constant_values.SPACE, constant_values.EMPTY_STRING).split(constant_values.COMMA)]
            segments = int(request.form.get(constant_values.STRING_SEGMENTS))
            APCA = apca.AdaptivePiecewiseConstantApproximation(segments)
            reduced_data = APCA.transform(y_data)
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
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.APCA_TITLE))
    )
    return render_template("apca.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, segments=segments, boolean_message=show_demo_message)


@app.route("/visualization/DFT", methods=['GET', 'POST'])
def dft_visualization():
    DFT = dft.DiscreteFourierTransformation()
    x_data = []
    y_data = []
    reduced_data = []
    show_demo_message = True
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3]
        reduced_data = DFT.transform(y_data)
    elif request.method == 'POST':
        try:
            x_data = []
            y_data = [float(i) for i in request.form.get(constant_values.STRING_DATA).replace(constant_values.SPACE, constant_values.EMPTY_STRING).split(constant_values.COMMA)]
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
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.DFT_TITLE))
    )
    return render_template("dft.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, boolean_message=show_demo_message)


@app.route("/visualization/DWT", methods=['GET', 'POST'])
def dwt_visualization():
    DWT = dwt.DiscreteHaarWaveletTransformation()
    x_data = []
    y_data = []
    reduced_data = []
    show_demo_message = True
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3]
        reduced_data = DWT.haar_transformation(y_data)
    elif request.method == 'POST':
        try:
            x_data = []
            y_data = [float(i) for i in request.form.get(constant_values.STRING_DATA).replace(constant_values.SPACE, constant_values.EMPTY_STRING).split(constant_values.COMMA)]
            reduced_data = DWT.haar_transformation(y_data)
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
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.DWT_TITLE))
    )
    return render_template("dwt.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, boolean_message=show_demo_message)


@app.route("/visualization/PAA", methods=['GET', 'POST'])
def paa_visualization():
    x_data = []
    y_data = []
    reduced_data = []
    segments = None
    show_demo_message = True
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3]
        segments = 4
        PAA = paa.PiecewiseAggregateApproximation(segments)
        reduced_data = PAA.transform(y_data)
    elif request.method == 'POST':
        try:
            y_data = [float(i) for i in request.form.get(constant_values.STRING_DATA).replace(constant_values.SPACE, constant_values.EMPTY_STRING).split(constant_values.COMMA)]
            x_data = [i for i in range(len(y_data))]
            segments = int(request.form.get(constant_values.STRING_SEGMENTS))
            PAA = paa.PiecewiseAggregateApproximation(segments)
            reduced_data = PAA.transform(y_data)
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
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.PAA_TITLE))
    )
    return render_template("paa.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, segments=segments, boolean_message=show_demo_message)


@app.route("/visualization/PLA", methods=['GET', 'POST'])
def pla_visualization():
    x_data = []
    y_data = []
    reduced_data = []
    segments = 10
    show_demo_message = True
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3][1:]
        PLA = pla.PiecewiseLinearAggregateApproximation(segments)
        reduced_data = PLA.transform(y_data)
    elif request.method == 'POST':
        try:
            x_data = []
            y_data = [float(i) for i in request.form.get(constant_values.STRING_DATA).replace(constant_values.SPACE, constant_values.EMPTY_STRING).split(constant_values.COMMA)]
            segments = int(request.form.get(constant_values.STRING_SEGMENTS))
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
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
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
    n_elements = 5
    show_demo_message = True
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3]
        reduced_data = SVD.transform(y_data, n_elements)
    elif request.method == 'POST':
        try:
            x_data = []
            y_data = [float(i) for i in request.form.get(constant_values.STRING_DATA).replace(constant_values.SPACE, constant_values.EMPTY_STRING).split(constant_values.COMMA)]
            n_elements = int(request.form.get(constant_values.STRING_N_ELEMENTS))
            reduced_data = SVD.transform(y_data, n_elements)
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
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=constant_values.SVD_TITLE))
    )
    return render_template("svd.html", line_options=line.dump_options(), original_data=y_data, reduced_data=reduced_data, n_elements=n_elements, boolean_message=show_demo_message)


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
