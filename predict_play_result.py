from numpy.lib.type_check import nan_to_num
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

plays ='nfl-big-data-bowl-2022/plays.csv'
plays_df = pd.read_csv(plays)

x = np.array(plays_df[['playId','quarter', 'down', 'yardsToGo', 'kickerId', 'penaltyYards', 'preSnapHomeScore', 'kickLength', 'absoluteYardlineNumber']].values.tolist())
x = nan_to_num(x)
y = np.array(plays_df['playResult'].values.tolist())
del plays_df
x_train, x_test, y_train, y_test = train_test_split(x, y,test_size=0.66)
model = LinearRegression().fit(x,y)
predicted_y = model.predict(x_test)
print('intercept: ',model.intercept_, "\n")
print('slope: \n',model.coef_, "\n")
print(np.round(predicted_y))