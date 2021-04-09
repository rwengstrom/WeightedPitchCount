
import pandas as pd

# Load in Necessary Datasets
pitches = pd.read_csv('data/pitches.csv')
leverage = pd.read_csv('data/leverage.csv')

# Merge and Clean Data
df = pd.merge(pitches,leverage)
df = df.drop(['code','type','event_num','on_1b','on_2b','on_3b'], axis = 1)
print(df.columns)


#Create a smaller dataset
ball = df[['pitch_type',
       'ab_id', 'b_count', 's_count', 'outs', 'pitch_num', 'pitcher_id',
       '(b_score-p_score)', 'top', 'inning', 'pitch_leverage']]

#Create groupby function and DataFrame
pitcher = ball.groupby('pitcher_id')
ave_lev_pitch = pd.DataFrame((pitcher.sum()['pitch_leverage'])/(pitcher.count()['pitch_leverage']))

games = pd.read_csv('data/2019_atbats.csv') #These are 2019 games

ball.sort_values(by = 'ab_id') #These are pitches from 2015-2018