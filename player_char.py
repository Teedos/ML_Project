import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

players = 'nfl-big-data-bowl-2022/players.csv'
players_df = pd.read_csv(players)
players_df['birthDate'] = pd.to_datetime(players_df['birthDate'], infer_datetime_format = True) 
players_df['birthDate'] = np.round((pd.Timestamp.now() - players_df['birthDate']).dt.days/365)
players_df = players_df.rename(columns={'birthDate': 'age'})


position= "SS"
plot_title_height = "Height of "+ position
plot_title_weight = "Weight of "+ position
filtered_df = players_df.loc[players_df['Position']== position]
print(filtered_df)
fig = px.bar(filtered_df, x = filtered_df['displayName'], y = filtered_df['height'], title = plot_title_height)
fig.show()
fig = px.bar(filtered_df, x = filtered_df['displayName'], y = filtered_df['weight'], title = plot_title_weight)
fig.show()