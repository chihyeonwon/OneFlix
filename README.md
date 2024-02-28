## 기술 스택
- FastAPI, Implicit 라이브러리 (데이터 전처리)
- AWS EC2, Route53
- React.js
- Docker
- Visual Studio Code
- Python 3.11.8

## 파이썬 가상 환경 생성하기
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/c5fafd5a-db32-4144-bbba-0c88a41e080f)
```
가상 환경을 생성하고 관리하는 파이썬 패키지인 venv를 사용한다.
fullstack-api 작업폴더를 생성하고 다음 명령어를 사용하여 파이썬 가상 환경을 구축한다.
```
#### venv가 포함된 Python interpreter 선택
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/2b0fd9ba-78ee-466a-9c9f-e9c7a1f81784)
```
뷰 메뉴의 명령 팔레트에서 venv가 포함된 Python interpreter를 선택한다.
```

## GitLab repo 생성 및 연결하기
#### Gitlab project 생성
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/a74bef00-1905-47b6-a7c3-95be4547d12a)
```
백엔드 CI 자동화를 위해서 gitlab-runner를 AWS EC2에 설치해서 사용, 프론트엔드(React) 배포를 위해 GitHub Pages를 사용한다.

gitlab-runner 대신 GitHub Action을 GitHub Pages 대신 Cloudflare Pages를 사용할 수도 있다.
```
#### Access Token 생성
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/3b22e3fb-bf7d-4a2f-a3a1-dd78a76f7769)
```
Gitlab 인증을 위한 토큰을 생성한다.. 생성한 토큰을 이용하여 Gitlab repo를 인증할 수 있다.
```

## 데이터 전처리하기

#### 데이터셋 다운로드
[무비렌즈 데이터셋 다운로드](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip)
```
추천 시스템 연습에 많이 활용되는 무비렌즈 데이터셋을 활용한다.
사이즈에 따라 다양한 버전이 제공되는데, 추천 시스템을 구축해보는 것이 목적이기 때문에
가장 작은 small 버전의 데이터셋을 활용한다.
```
#### 데이터셋 훑어보기
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/f8ac4913-3d21-4090-829b-54ed16d68f9a)
```
다운로드한 파일의 압축을 풀어보면 5개의 파일로 이루어진 폴더가 있다.
```
- README.txt : 데이터셋에 대한 설명, 저작권 등의 정보가 있는 파일, 분석에는 사용하지 않으나 각 파일의 구성정보 확인 가능

- tags.csv : 각 유저가 영화에 대해 한 단어 혹은 한 문장으로 표현한 태그를 모아놓은 데이터

- ratings.csv : 유저 ID와 영화 ID, 5점 만점의 평점, 그리고 평점을 준 시점(timestamp)로 이루어진 데이터로
  이 파일을 이용하여 추천 엔진에 학습을 시키고 추천 결과를 도출할 수 있도록 한다.

#### ratings.csv 파일 일부
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/3539ac1d-933b-439e-b353-bf5399713c41)

#### links.csv 파일 일부
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/aedbc508-e9a2-4f01-9fd9-b808be7c9639)

```
movies.csv 파일과 links.csv 파일을 이용하여 oneflex에 보여줄 영화 정보 데이터프레임을 만든다.
웹 사이트 형태에서 보여주기 위해서는 영화의 제목, 영화 포스터 등의 정보가 필요하다.
무비렌즈 데이터셋에서 사용하고 있는 IMDB, TMDB 사이트의 API를 사용해서 이 과정을 자동화한다.
```
#### 데이터셋과 전처리 코드
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/77571c0f-aae2-453b-9d12-315aabc41148)
```
app 폴더 밑에 data 폴더를 만들고 다운로드한 데이터셋 파일 중 필요한 데이터파일(links.csv, movies.csv, ratings.csv)을
넣는다.

또 전처리 코드인 movie_preprocessor.py 파일을 생성하여 app 폴더의 하단에 추가한다.
```
#### pandas 패키지 설치
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/9f6020a6-e82d-498d-aa41-3ab435350276)
```
파이썬에서 데이터를 다룰 때 사용하는 padas 패키지를 다음 명령어로 설치한다.
```
#### request 패키지 설치
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/137f92d2-15c6-44c7-895c-4e29173106ff)
```
HTTP 통신을 위한 패키지인 requests 패키지를 다음 명령어로 설치한다.
```

#### movie_preprocessor.py 
```python
import pandas as pd
import requests

if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    print(movies_df)
```
이렇게 코드를 작성한 후에 movie_preprosessor.py 파일이 위치한 곳으로 이동해 작성한 스크립트를 실행한다.
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/b2d497bd-2092-4639-9faa-70a4adad15e8)
```
movies.csv 파일의 모습이 출력되는 것을 알 수 있다.
movieid, title, genres의 3개의 속성에 9742개의 데이터행이 출력된다.
```
#### movie_preprocessor.py 수정 (파일 merge(), imdbId, tmdbId 컬럼 추가)
```python
if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    # id 를 문자로 인식하도록 type을 변경한다.
    movies_df['movieId'] = movies_df['movieId'].astype(str)
    links_df = pd.read_csv('data/links.csv', dtype=str)
    merged_df = movies_df.merge(
        links_df, on='movieId', how='left')  # movies_df를 기준으로 merge
    print(merged_df)
    print(merged_df.columns)
```
```
movies.csv와 links.csv를 결합하는 작업을 수행한다.
공통된 key인 movieId를 이용해서 서로 다른 두 개의 데이터프레임을 병합하는 함수인 merge를 사용하였다.
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/3eae34a9-5e7d-4fb9-aec4-35574f9ae8e8)
```
기존에 출력된 값에서 imdbId, tmbdId 컬럼이 추가된 것을 확인할 수 있다.
```
#### movie_preprocessor.py 수정 (add_url(), apply(), url 컬럼 추가)
```python
def add_url(row):
    return f"http://www.imdb.com/title/tt{row}/"


if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    # id 를 문자로 인식하도록 type을 변경한다.
    movies_df['movieId'] = movies_df['movieId'].astype(str)
    links_df = pd.read_csv('data/links.csv', dtype=str)
    merged_df = movies_df.merge(
        links_df, on='movieId', how='left')  # movies_df를 기준으로 merge
    merged_df['url'] = merged_df['imdbId'].apply(lambda x: add_url(x))
    print(merged_df)
    print(merged_df.iloc[1, :])
```
```
URL 컬럼을 추가한다. URL은 imdb 웹사이트의 영화 상세 화면으로 이동하도록 한다.
imdb 영화 상세 화면 url 주소는 다음과 같다. http://www.imdb.com/title/tt0114709/
tt 뒤의 0114709는 imdbId 컬럼의 값에 해당하는 것으로 보아 http://www.imdb.com/title/tt에 imdbId를
붙여주면 된다는 것을 알 수 있다. 이를 코드로 표현하여 url이라는 컬럼을 추가했다.
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/97f7ef2d-927b-451d-932c-fea0b9d1f58a)
```
기존 컬럼의 마지막에 url 컬럼이 추가되는 것을 알 수 있다.
첫 번째 데이터인 Jumanji 영화의 정보를 출력하도록 하고 url 부분의 url로 이동하면 Jumanji의 영화 상세 화면으로
이동하는 것을 확인할 수 있다.
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/1657c4cc-0c89-4a74-92fc-58843f2de64f)

#### movie_preprocessor.py 수정 (add_rating(), agg(), rating_count, rating_avg 칼럼 추가)
```python
def add_rating(df):
    ratings_df = pd.read_csv('data/ratings.csv')
    ratings_df['movieId'] = ratings_df['movieId'].astype(str)
    agg_df = ratings_df.groupby('movieId').agg(
        rating_count=('rating', 'count'),
        rating_avg=('rating', 'mean')
    ).reset_index()

    rating_added_df = df.merge(agg_df, on='movieId')
    return rating_added_df

if __name__ == "__main__":
    movies_df = pd.read_csv('data/movies.csv')
    # id 를 문자로 인식하도록 type을 변경한다.
    movies_df['movieId'] = movies_df['movieId'].astype(str)
    links_df = pd.read_csv('data/links.csv', dtype=str)
    merged_df = movies_df.merge(
        links_df, on='movieId', how='left')  # movies_df를 기준으로 merge
    merged_df['url'] = merged_df['imdbId'].apply(lambda x: add_url(x))
    result_df = add_rating(merged_df)
    print(result_df)
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/de274e39-653c-42d2-85e2-663f7ff2e449)
```
add_rating 함수는 ratings.csv 파일을 읽고 rating 정보를 count, mean이라는 집계함수를 사용해서 컬럼에 추가해준다.
rating_count, rating_avg 칼럼이 추가된 것을 확인할 수 있다.
```

#### themoviedb 사이트에서 API 키 값 받아오기
[themoviedb 사이트](https://www.themoviedb.org/signup)
```
tmdb의 API를 이용해서 영화 포스터 데이터를 받아온다.
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/6fc914db-009b-4089-972d-6622d745384e)
```
회원가입 후 이메일 인증을 한 뒤에 프로필 부분의 설정 메뉴로 들어간다.
설정에서 API 메뉴를 선택한다.
Developer 키 타입 설정 및 API 사용 동의 후 신청 상세 화면을 작성한다. 바로 API 키가 발급된다.
```
#### 진행상황을 알려주는 tqdm 패키지 설치
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/1595a4e7-e631-4d49-b0d2-e91e4ea8f195)
```
코드를 실행하려면 시간이 오래 걸리기 때문에 진행 상황을 알려주는 패키지인 tqdm 패키지를 설치한다.
```
#### movie_preprocessor.py 수정 (add_poster(), to_csv(), poster_path 컬럼 추가)
```python

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
```
```
발급받은 API 키와 tmdbId를 조합해서 tmdb_url을 생성한다.
tmdb_url로 HTTP GET Request 요청을 보낸 결과를 result에 저장한다.
poster 경로는 result.json()을 https://image.tmdb.org/t/p/original 뒤에 붙인 url이 된다.
이 경로에서 poster_path를 받아온다. 포스터 경로

메인 함수에서 poster_path 컬럼을 None으로 선언한 후 add_poster함수에서 api를 통해서
poster_path 값을 받아서 컬럼 값에 저장한다.

최종적으로 만들어진 테이블을 data밑의 movies_final.csv 이름의 csv 형식의 파일로 저장한다.
```
#### 최종적으로 전처리 된 movies_final csv 데이터의 일부

```
기존 movieId, title, genres 컬럼에 데이터 전처리 작업을 통해서 얻은
imdbId, tmdbId, url, rating_count, rating_avg, poster_path 컬럼이 모두 잘 추가되어 들어가 있는 것을 확인할 수 있다.

이제 추천 시스템이 탑재된 백엔드를 구현한다.
```
## 백엔드 목록 조회하기

#### FastAPI 세팅

```
FastAPI는 파이썬 기반의 가장 빠른 웹 프레임워크 중 하나이다. FastAPI 패키지를 다음 명령어로 설치한다.
```

```
 다음 명령어로  웹 서버 구동을 위한 uvicorn 패키지도 설치한다.
```

