import pandas as pd

data = [7,2,5,8,9,4]

# series
series = pd.Series(data)
index = []
print(series)

# data frame
df = pd.DataFrame([1,2,3],[6,7,8],[3,6,5])
print(df)

