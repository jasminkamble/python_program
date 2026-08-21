import pandas as pd

var = pd.read_csv("pandas/csv/csv_corr.csv")
print(var.corr())