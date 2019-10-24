import pandas as pd
import numpy as np
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# /Users/Caner/Desktop/plotly/dash-sample-apps/apps/dash-uber-rasterizer/data/plasma.csv
# plasma = pd.read_csv("/Users/Caner/Desktop/plotly/dash-sample-apps/apps/dash-uber-rasterizer/data/plasma.csv")
# viridis = pd.read_csv("/Users/Caner/Desktop/plotly/dash-sample-apps/apps/dash-uber-rasterizer/data/viridis.csv")
# fire = pd.read_csv("/Users/Caner/Desktop/plotly/dash-sample-apps/apps/dash-uber-rasterizer/data/fire.csv")

plasma = pd.read_csv(DATA_PATH.joinpath("plasma.csv"))
viridis = pd.read_csv(DATA_PATH.joinpath("viridis.csv"))
fire = pd.read_csv(DATA_PATH.joinpath("fire.csv"))

def format_colorscale(df):
    values = np.linspace(0, 1, len(df))
    colorscale = [[values[i], df["x"][i]] for i in range(len(df))]
    return(colorscale)

plasma_cs = format_colorscale(plasma)
viridis_cs = format_colorscale(viridis)
fire_cs = format_colorscale(fire)
blues_cs = [[0, "lightblue"], [1, "darkblue"]]

colorscales = {"plasma": plasma_cs,
               "viridis": viridis_cs,
               "fire": fire_cs,
               "blue": blues_cs}


