import pandas as pd


# corr()
df = pd.read_csv('data.csv')
print(df.corr())

#           Duration     Pulse  Maxpulse  Calories
# Duration  1.000000 -0.190684 -0.000611  0.924628
# Pulse    -0.190684  1.000000  0.791785  0.007563
# Maxpulse -0.000611  0.791785  1.000000  0.206282
# Calories  0.924628  0.007563  0.206282  1.000000

