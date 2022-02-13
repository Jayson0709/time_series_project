from flask.json import jsonify
from flask import Flask, render_template
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


@app.route("/visualization/APCA")
def apca_visualization():
    x_data = [i for i in range(len(data[3]))]
    y_data = data[3]
    APCA = apca.AdaptivePiecewiseConstantApproximation(12)
    reduced_data = APCA.transform(y_data)
    title_name = 'APCA'
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
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("apca.html", line_options=line.dump_options())


@app.route("/visualization/DFT")
def dft_visualization():
    x_data = [i for i in range(len(data[3]))]
    y_data = data[3]
    DFT = dft.DiscreteFourierTransformation()
    reduced_data = DFT.transform(y_data)
    title_name = 'DFT'
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
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("dft.html", line_options=line.dump_options())


@app.route("/visualization/DWT")
def dwt_visualization():
    x_data = [i for i in range(len(data[3]))]
    y_data = data[3]
    DWT = dwt.DiscreteHaarWaveletTransformation()
    reduced_data = DWT.haar_transformation(y_data)
    title_name = 'DWT'
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
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("dft.html", line_options=line.dump_options())


@app.route("/visualization/PAA")
def paa_visualization():
    x_data = [i for i in range(len(data[3]))]
    y_data = data[3]
    PAA = paa.PiecewiseAggregateApproximation(4)
    reduced_data = PAA.transform(y_data)
    title_name = 'PAA'
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
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("paa.html", line_options=line.dump_options())


@app.route("/visualization/PLA")
def pla_visualization():
    x_data = [i for i in range(len(data[3]))]
    y_data = data[3]
    PLA = pla.PiecewiseLinearAggregateApproximation(10)
    reduced_data = PLA.transform(y_data)
    title_name = 'PLA'
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
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("pla.html", line_options=line.dump_options())


@app.route("/visualization/SVD")
def svd_visualization():
    x_data = [i for i in range(len(data[3]))]
    y_data = data[3]
    SVD = svd.SingularValueDecomposition()
    reduced_data = SVD.transform(y_data, 5)
    title_name = 'SVD'
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
            .set_global_opts(title_opts=opts.TitleOpts(title=title_name))
    )
    return render_template("svd.html", line_options=line.dump_options())


if __name__ == "__main__":
    app.run()
