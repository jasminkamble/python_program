import pandas as pd

var = pd.read_json('pandas/cleaning_data/json_file.json')

new_var = var.dropna()

print(new_var.to_string())


#Notice in the result that some rows have been removed (row 17, 27 and 91).

#These rows had cells with empty values.


import pandas as pd

var = pd.read_json('pandas/cleaning_data/json_file.json')

var.dropna(inplace=True)

print(var.to_string())

