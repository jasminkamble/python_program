import pandas as pd
a = [1,2,3]
var = pd.Series(a)
print(var)
print("\nprinting specific index :",var[0])

print("\nWith the index argument, you can name your own labels. ")

print(pd.Series(a,index = ["one","two","three"]))

var1 = pd.Series(a,index = ["one","two","three"])
print("\nprinting the specific element with help of lable",var1["one"])


calories = {"day1": 420, "day2": 380, "day3": 390}
print(pd.Series(calories))