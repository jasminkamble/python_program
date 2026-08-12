import pandas as pd

df = pd.read_json('pandas/cleaning_data/json_file.json')

df.loc[106,'Duration'] = 45

print(df.to_string())

