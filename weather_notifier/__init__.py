import pandas as pd

data = pd.read_csv('/home/hardcode/PycharmProjects/weather-notifier/data/users.csv')

for index, row in data.iterrows():
    if type(row['user']).__name__ == 'str':
        print(row['user'], row['email'], row['locations'])
