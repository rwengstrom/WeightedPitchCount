
import pandas as pd

# Load in Necessary Datasets
pitches = pd.read_csv('pitches.csv')
leverage = pd.read_csv('leverage.csv')

# Merge and Clean Data
df = pd.merge(pitches,leverage)
df = df.drop(['code','type','event_num','on_1b','on_2b','on_3b'], axis = 1)
print(df.columns)
