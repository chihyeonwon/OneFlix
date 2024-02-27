import pandas as pd
import requests

if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    # id 를 문자로 인식하도록 type을 변경한다.
    movies_df['movieId'] = movies_df['movieId'].astype(str)
    links_df = pd.read_csv('data/links.csv', dtype=str)
    merged_df = movies_df.merge(
        links_df, on='movieId', how='left')  # movies_df를 기준으로 merge
    print(merged_df)
    print(merged_df.columns)
