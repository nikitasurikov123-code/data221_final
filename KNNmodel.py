import pandas
import numpy
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

data_frame = pandas.read_csv("car details v4.csv")

rupee_to_cad = 0.01525
data_frame["Price"] = data_frame["Price"] * rupee_to_cad

data_frame = data_frame.drop(columns = ["Color", "Length", "Width", "Height", "Max Power", "Max Torque"])

cleaned_engine = []
