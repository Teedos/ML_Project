from os import chdir
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

"""games = 'nfl-big-data-bowl-2022/games.csv'
games_df = pd.read_csv(games)
partial = games_df.head(10)
print(partial.fillna(0))

home = partial.homeTeamAbbr.tolist()

home_points = []
home_team = []
for x in home:
    str = x.split("-")
    home_team.append(str[0])
    home_points.append(str[1])  
print(home_points)

visitor = partial.visitorTeamAbbr.tolist()
visitor_points = []
visitor_team = []
for x in visitor:
    str = x.split("-")
    visitor_team.append(str[0])
    visitor_points.append(str[1])  
print(visitor_points)"""

tracking_2018= 'nfl-big-data-bowl-2022/tracking2018.csv'
tracking_df = pd.read_csv(tracking_2018)
#partial = tracking_df.head(20)
#print(partial.fillna(0))

players = 'nfl-big-data-bowl-2022/players.csv'
players_df = pd.read_csv(players)
players_df['birthDate'] = pd.to_datetime(players_df['birthDate'], infer_datetime_format = True) 
players_df['birthDate'] = np.round((pd.Timestamp.now() - players_df['birthDate']).dt.days/365)
players_df = players_df.rename(columns={'birthDate': 'age'})


###Difference between SS#####

pos= players_df.query('Position == "SS"')
filtered_df = tracking_df.loc[tracking_df['nflId'].isin(pos['nflId'])]
filtered_df = filtered_df[["nflId","playId"]]
df_temp = filtered_df.groupby(['nflId','playId'])
df_unique = df_temp['nflId'].count()
print(df_unique)
filtered_df = filtered_df.rename({'playId' : 'nUniquePlays'}, axis = 1)
df_unique = filtered_df.groupby('nflId').nunique()

print(df_unique)
y_axis = df_unique.reset_index()['nUniquePlays'].tolist()
x_axis = df_unique.reset_index()['nflId'].tolist()

fig = px.bar(x = x_axis,y = y_axis,
    labels ={
        "x": "NFL ID",
        "y": "Number of unique plays"
    }, title = "Number of unique plays by SS in 2018 season")
fig.update_xaxes(type='category')
fig.show()

del players_df
del df_temp
del df_unique
del tracking_df