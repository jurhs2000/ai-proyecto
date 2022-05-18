# Universidad del Valle de Guatemala
# Inteligencia Artificial - CC3045
# Authors:
# Julio Herrera - 19402
# Juan Pablo Pineda - 19087
# Diego Crespo - 19541

import pandas as pd

# Dataset:
# games_of_all_time.csv - Games of All Time from Metacritic - https://www.kaggle.com/datasets/xcherry/games-of-all-time-from-metacritic?resource=download
# vgsales.csv - Video Game Sales - https://www.kaggle.com/datasets/gregorut/videogamesales

games_meta = pd.read_csv('games_of_all_time.csv')
games_sales = pd.read_csv('vgsales.csv')

print(games_meta.head())
print(games_sales.head())

print(games_meta.describe())
print(games_sales.describe())

# change the column names
games_meta.columns = ['name', 'meta_score', 'user_score', 'platforms', 'description', 'url', 'developer', 'genre', 'type', 'rating']
games_sales.columns = ['id', 'name', 'platform', 'year', 'genres', 'publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

print(games_meta.head())
print(games_sales.head())

# join the two datasets by name
games_meta_sales = pd.merge(games_meta, games_sales, on='name')

print('----------------------------')
print(games_meta_sales.head(20))
print(games_meta_sales.describe())
