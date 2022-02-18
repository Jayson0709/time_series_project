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
    title_name = 'APCA'
    x_data = []
    y_data = []
    reduced_data = []
    if request.method == 'POST':
        x_data = []
        y_data = request.form.get('data')
        APCA = apca.AdaptivePiecewiseConstantApproximation(request.form.get('segments'))
        reduced_data = APCA.transform(y_data)
    else:
        APCA = apca.AdaptivePiecewiseConstantApproximation(12)
        x_data = []
        y_data = [float(i) for i in request.form.get('data').replace(" ", "").split(',')]
        reduced_data = APCA.transform(y_data)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name="Original Data",
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name="Reduced Data",
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("apca.html", line_options=line.dump_options())


@app.route("/visualization/DFT", methods=['GET', 'POST'])
def dft_visualization():
    title_name = 'DFT'
    DFT = dft.DiscreteFourierTransformation()
    x_data = []
    y_data = []
    reduced_data = []
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3]
        reduced_data = DFT.transform(y_data)
    elif request.method == 'POST':
        x_data = []
        y_data = [float(i) for i in request.form.get('data').replace(" ", "").split(',')]
        reduced_data = DFT.transform(y_data)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name="Original Data",
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name="Reduced Data",
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("dft.html", line_options=line.dump_options())


@app.route("/visualization/DWT", methods=['GET', 'POST'])
def dwt_visualization():
    DWT = dwt.DiscreteHaarWaveletTransformation()
    title_name = 'DWT'
    x_data = []
    y_data = []
    reduced_data = []
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3]
        reduced_data = DWT.haar_transformation(y_data)
    elif request.method == 'POST':
        x_data = []
        y_data = [float(i) for i in request.form.get('data').replace(" ", "").split(',')]
        reduced_data = DWT.haar_transformation(y_data)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name="Original Data",
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name="Reduced Data",
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("dft.html", line_options=line.dump_options())


@app.route("/visualization/PAA", methods=['GET', 'POST'])
def paa_visualization():
    title_name = 'PAA'
    x_data = []
    y_data = []
    reduced_data = []
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3]
        PAA = paa.PiecewiseAggregateApproximation(4)
        reduced_data = PAA.transform(y_data)
    elif request.method == 'POST':
        y_data = [float(i) for i in request.form.get('data').replace(" ", "").split(',')]
        x_data = [i for i in range(len(y_data))]
        PAA = paa.PiecewiseAggregateApproximation(int(request.form.get('segments')))
        reduced_data = PAA.transform(y_data)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name="Original Data",
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name="Reduced Data",
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("paa.html", line_options=line.dump_options())


@app.route("/visualization/PLA", methods=['GET', 'POST'])
def pla_visualization():
    title_name = 'PLA'
    x_data = []
    y_data = []
    reduced_data = []
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3][1:]
        PLA = pla.PiecewiseLinearAggregateApproximation(10)
        reduced_data = PLA.transform(y_data)
    elif request.method == 'POST':
        x_data = []
        y_data = [float(i) for i in request.form.get('data').replace(" ", "").split(',')]
        PLA = pla.PiecewiseLinearAggregateApproximation(request.form.get('segments'))
        reduced_data = PLA.transform(y_data)
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name="Original Data",
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name="Reduced Data",
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("pla.html", line_options=line.dump_options())


@app.route("/visualization/SVD", methods=['GET', 'POST'])
def svd_visualization():
    title_name = 'SVD'
    SVD = svd.SingularValueDecomposition()
    x_data = []
    y_data = []
    reduced_data = []
    if request.method == 'GET':
        x_data = [i for i in range(len(data[3]))]
        y_data = data[3]
        reduced_data = SVD.transform(y_data, 5)
    elif request.method == 'POST':
        x_data = []
        y_data = [float(i) for i in request.form.get('data').replace(" ", "").split(',')]
        reduced_data = SVD.transform(y_data, int(request.form.get('n_elements')))
    line = (
        Line()
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(series_name="Original Data",
                       y_axis=y_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .add_yaxis(series_name="Reduced Data",
                       y_axis=reduced_data,
                       symbol="emptyCircle",
                       is_symbol_show=True,
                       is_smooth=True,
                       label_opts=opts.LabelOpts(is_show=False),
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("svd.html", line_options=line.dump_options())


if __name__ == "__main__":
    app.run()
