import pandas as pd
import requests

if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    print(movies_df)