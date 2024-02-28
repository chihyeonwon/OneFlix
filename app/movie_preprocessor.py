import pandas as pd
import requests
import sys
from tqdm import tqdm
import time


def add_url(row):
    return f"http://www.imdb.com/title/tt{row}/"


def add_rating(df):
    ratings_df = pd.read_csv('data/ratings.csv')
    ratings_df['movieId'] = ratings_df['movieId'].astype(str)
    agg_df = ratings_df.groupby('movieId').agg(
        rating_count=('rating', 'count'),
        rating_avg=('rating', 'mean')
    ).reset_index()

    rating_added_df = df.merge(agg_df, on='movieId')
    return rating_added_df


def add_poster(df):
    for i, row in tqdm(df.iterrows(), total=df.shape[0]):
        tmdb_id = row["tmdbId"]
        tmdb_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key=29ab09fff1761c162de4a759b1248e93&language=en-US"
        result = requests.get(tmdb_url)
        # final url : https://image.tmdb.org/t/p/original/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg
        try:
            df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original" + \
                result.json()['poster_path']
            time.sleep(0.1)  # 0.1초 시간 간격을 만들어 준다.
        except (TypeError, KeyError) as e:
            # toy story poster as default
            df.at[i, "poster_path"] = "https://image.tmdb.org/t/p/original/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg"

    return df


if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    # id 를 문자로 인식하도록 type을 변경한다.
    movies_df['movieId'] = movies_df['movieId'].astype(str)
    links_df = pd.read_csv('data/links.csv', dtype=str)
    merged_df = movies_df.merge(
        links_df, on='movieId', how='left')  # movies_df를 기준으로 merge
    merged_df['url'] = merged_df['imdbId'].apply(lambda x: add_url(x))
    result_df = add_rating(merged_df)
    result_df['poster_path'] = None
    reesult_df = add_poster(result_df)

    result_df.to_csv("data/movies_final.csv", index=None)
