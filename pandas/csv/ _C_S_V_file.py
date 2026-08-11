
print("printting data from csv")
import pandas as pd
var = pd.read_csv("pandas/simple.csv")
print(var)

print("\n")
print("\n")
print("\n")
print("\n")


import pandas as pd
var = pd.read_csv("pandas/simple.csv")
print(var.to_string())


import pandas as pd
pd.options.display.max_rows=50
var = pd.read_csv('pandas/simple.csv')
print(var)

