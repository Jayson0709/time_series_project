from flask.json import jsonify
from flask import Flask, render_template
from flask import request
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line

n = r"./datasets/Beef_TRAIN"
data = pd.read_csv(n)
print(data)

app = Flask(__name__, static_folder=r"./templates")


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


if __name__ == "__main__":
    app.run()
