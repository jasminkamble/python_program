import pandas as pd

var = pd.read_json('pandas/cleaning_data/json_file.json')

new_var = var.dropna()

print(new_var.to_string())