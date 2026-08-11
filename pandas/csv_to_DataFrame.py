import pandas as pd

data = {
    "flower" :["rose","sunflower","tulip"],
    "image" :["🌹","🌻","🌷"]
    }

show = pd.DataFrame(data)
print(show)

print("\nprinting specific index :",show.loc[1])
print("\nprinting specific index :",show.loc[2])

print("\nprinting key and value at a time :",show.loc[1,2])

