25.03.05
![image](https://github.com/user-attachments/assets/98e2dd74-3841-46fd-a46d-3a5bf315dbf3)
AWS Routing 계약 기간 종료로 서비스 종료 되었습니다~

## 기술 스택
- FastAPI, Implicit 라이브러리 (데이터 전처리)
- AWS EC2, Route53
- React.js
- Docker
- Visual Studio Code
- Python 3.11.8

[무중단 배포](https://youtu.be/8FN3aHDimTE?si=hFc-pKTmY7ItkSKD)

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
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/23634fe4-b85f-42ab-b3ba-1126e1c7aa68)
```
코드를 실행하려면 시간이 오래 걸리기 때문에 진행 상황을 알려주는 패키지인 tqdm 패키지를 설치한다.

실제로 전처리한 데이 9724개를 csv파일로 만드는 데 50분 이상이 걸렸다.
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
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/74b649d7-ce9f-48a6-941c-75c5f6017236)
```
기존 movieId, title, genres 컬럼에 데이터 전처리 작업을 통해서 얻은
imdbId, tmdbId, url, rating_count, rating_avg, poster_path 컬럼이 모두 잘 추가되어 들어가 있는 것을 확인할 수 있다.

이제 추천 시스템이 탑재된 백엔드를 구현한다.
```
## 백엔드 목록 조회하기

#### FastAPI 세팅
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/be294c28-14c1-486c-ae32-753f0a1d1a98)
```
FastAPI는 파이썬 기반의 가장 빠른 웹 프레임워크 중 하나이다. FastAPI 패키지를 다음 명령어로 설치한다.
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/9ececb11-794f-4409-9183-f8214e0b7a86)
```
 다음 명령어로  웹 서버 구동을 위한 uvicorn 패키지도 설치한다.
```
#### main.py
```python
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/all/")
async def all_movies():
    return {"message": "All movies"}


@app.get("/generes/{genre}")
async def genre_movies(genre: str):
    return {"message": f"genre: {genre}"}


@app.get("/user-based/")
async def user_based(params: Optional[List[str]] = Query(None)):
    return {"message": "user based"}


@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    return {"message": f"item ased: {item_id}"}
```
```
실제로 활용할 4개의 엔드포인트를 미리 생성하였다.("/", "/all", "/genres/{genre}", "/user-based/", "/item-based/{item_id}")
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/262c6029-c92f-4cfa-9914-18eb9d12d980)
```
FastAPI 서버를 다음 명령어로 동작시킨다.
```
#### 엔드포인트 작동 테스팅
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/8440dce1-9a7f-467f-868b-3829721eb76f)
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/364b8746-e979-47c8-9d73-3d8a85a46fe8)
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/8639d4e9-9cf0-4c53-82db-1f270c5d4d43)
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/09297fee-2434-4181-af8d-6a34a6d66d62)
```
지정한 4개의 엔드포인트가 잘 작동하는지 확인하였다. 4개의 엔드포인트에서 원하는 데이터가 나올 수 있도록 구현한다.
```
## /all 엔드포인트
```
/all 엔드포인트에서는 랜덤한 10개의 영화 데이터를 반환하도록 한다.
```
#### resolver.py
```python
import pandas as pd

item_fname = 'data/movies_final.csv'


def random_items():
    movies_df = pd.read_csv(item_fname)
    movies_df = movies_df.fillna('')  # 공백을 채워준다
    result_items = movies_df.sample(n=10).to_dict("records")
    return result_items
```
#### main.py
```python
@app.get("/all/")
async def all_movies():
    result = random_items()
    return {"result": result}
```
```
resolver.py는 pandas에서 제공하는 sample 함수를 이용하여 랜덤하게 10개의 데이터를 반환하도록 한다.
main.py의 "/all"엔드 포인트의 코드를 result로 random_items()으로 반환되는 10개의 데이터를 출력하도록 수정한다.
```
#### /all 엔드포인트 테스팅 (랜덤한 10개의 데이터 출력)
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/9392545c-42fc-4869-85fd-b6208da7de68)

## /genres 엔드포인트
```
같은 장르 genre의 영화만 보여주도록 /genres 엔드포인트를 구현한다. 랜덤하게 아이템을 반환하는 데에서 /all과 같이
sample 함수를 이용하지만 그 전에 genres 컬럼에 있는 이름을 이용해서 영화 데이터를 필터링 한 후에 반환한다.
```
#### resolver.py 
```python
def random_genres_items(genre):
    movies_df = pd.read_csv(item_fname)
    genre_df = movies_df[movies_df['genres'].apply(
        lambda x: genre in x.lower())]
    genre_df = genre_df.fillna('')  # 공백을 채워준다
    result_items = genre_df.sample(n=10).to_dict("records")
    return result_items
```
#### main.py
```python
@app.get("/genres/{genre}")
async def genre_movies(genre: str):
    result = random_genres_items(genre)
    return {"result": result}
```
```
resolver.py의 random_genres_items 함수에서 genre_df pandas 객체를 생성할 때의 람다 함수를 보면
매개변수로 받은 genre가 genres 컬럼 안에 포함 되는지 안 되는지를 판별한다.(in 함수)

genres 컬럼을 보면 adventure | animation | children | comedy | fantasty 같은 방식으로 장르가 구분되어 있고
이를 |를 기준으로 일일이 검색할 수도 있지만 str 자료형은 비교가 가능하므로 in 함수를 이용하여 글자가 포함되는 지
여부를 판별해주어 원하는 장르별 영화를 반환할 수 있다.
```
#### /geres 엔드포인트 테스팅
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/3c09316c-b9db-4504-a64a-e98c8229d0a2)
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/0e6d5a6f-9120-40ff-8149-dc1eeac81b03)
```
/genres/comedy, /genres/action에 접근했을 때 해당하는 장르의 영화가 잘 출력하는 것을 알 수 있고 sample 함수를
사용했기 때문에 새로고침 할 때마다 다른 영화들이 보여지게 된다.
```
## 추천 목록 조회하기

#### implicit 패키지 설치
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/3d0604df-7466-4795-99e6-5e4173f2954b)
```
implicit 패키지는 다양한 머신러닝 기법을 이용해서 추천 엔진을 만들 수 있게 해주는 파이썬 패키지이다.
딥러닝을 이용하지는 않지만, 추천 시스템의 기본 원리를 이해하고 간단한 수준의 추천 시스템을 만드는 데 충분하다.

다음 명령어로 implicit 패키지를 설치한다.
```

#### 추천 엔진 학습시키기
```
추천 엔진을 학습시키고 그 결과를 /item-based(영화별 추천), /user-based(유저별 추천) 엔드포인트로 보내주기 위해서
recommender.py 파일을 만든다. 또한 model이 저장될 수 있또록 model이라는 폴더도 함께 만든다.
```
#### recommender.py
```python
def model_train():
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["movieId"] = ratings_df["movieId"].astype("category")

    # create a sparse matrix of all the users/repos
    rating_matrix = coo_matrix(
        (
            ratings_df["rating"].astype(np.float32),
            (
                ratings_df["movieId"].cat.codes.copy(),
                ratings_df["userId"].cat.codes.copy(),
            ),
        )
    )

    als_model = AlternatingLeastSquares(
        factors=50, regularization=0.01, dtype=np.float64, iterations=50
    )

    als_model.fit(weight * rating_matrix)

    pickle.dump(als_model, open(saved_model_fname, "wb"))
    return als_model


if __name__ == "__main__":
    model = model_train()
```
```
model_train() 함수는 ratings 데이터를 이용해서 추천 엔진(=model)을 학습시키는 함수이다.
userId와 movieId를 category 데이터 형태로 바꿔준다.
어떤 유저가 어떤 영화에 얼마의 평점을 주었는 지를 행렬 형태로 표현해주는 함수인 coo_matrix함수를 사용한다.
als_model을 생성하는 부분을 보면 factors, regularization, dtype, iteration의 변수를 조정할 수 있다.

factors: latent factor의 개수로 숫자가 클수록 기준의 개수가 많아지고 이는 다양한 사람들의 취향을 반영할 수 있다는 뜻이다
단점으로는 오버피팅이라고하는 과적합이 발생할 가능성이 높아진다. 과적합이 일어날 경우 학습한 데이터에서는 아주 정확한 결과값이
학습하지 않은 데이터에서는 좋지 않은 결과값이 나온다.

regularization: 이러한 과적합 문제를 방지하기 위한 변수로 숫자가 클수록 과적합을 막을 수 있으나 너무 큰 값을 넣을 경우에는
추천의 정확도가 떨어질 확률이 높아진다.

dtype : rating의 데이터 형식이 float이기 때문에 np.float64를 사용한다.

iterations : 학습을 통해 parameter의 업데이트를 몇 번 할 것인지를 나타낸다. iteration의 횟수도 많을수록 과적합이 될 가능성이 높다

Collaborative Filtering 기반의 추천 시스템이므로 변수에 여러 값을 넣어서 실험해 볼 수 있다.
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/d71188ce-3b50-4f44-912b-36da77a5388a)
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/f5101ba3-027e-4600-b134-5fce5bd010b8)
```
recommender.py를 실행하면 model 폴더 밑에 finalized_model.sav라는 모델 파일이 생긴 것을 확인할 수 있다.
```
## /item-based 엔드포인트
```
implicit 패키지의 similar_items 함수는 Collaborative Filtering 기반, 즉 유저-아이템 간의 상호작용을 가지고
비슷한 아이템을 추천해주는 함수다. 
```
#### recommender.py 수정(calculate_item_based, item_based_recommendation)
```python
def model_train():
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["movieId"] = ratings_df["movieId"].astype("category")

    # create a sparse matrix of all the users/repos
    rating_matrix = coo_matrix(
        (
            ratings_df["rating"].astype(np.float32),
            (
                ratings_df["movieId"].cat.codes.copy(),
                ratings_df["userId"].cat.codes.copy(),
            ),
        )
    )

    als_model = AlternatingLeastSquares(
        factors=50, regularization=0.01, dtype=np.float64, iterations=50
    )

    als_model.fit(weight * rating_matrix)

    pickle.dump(als_model, open(saved_model_fname, "wb"))
    return als_model


def calculate_item_based(item_id, items):
    loaded_model = pickle.load(open(saved_model_fname, "rb"))
    recs = loaded_model.similar_items(itemid=int(item_id), N=11)
    return [str(items[r]) for r in recs[0]]

def item_based_recommendation(item_id):
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["movieId"] = ratings_df["movieId"].astype("category")
    movies_df = pd.read_csv(item_fname)

    items = dict(enumerate(ratings_df["movieId"].cat.categories))
    try:
        parsed_id = ratings_df["movieId"].cat.categories.get_loc(int(item_id))
        result = calculate_item_based(parsed_id, items)
    except KeyError as e:
        result = []
    result = [int(x) for x in result if x != item_id]
    result_items = movies_df[movies_df["movieId"].isin(result)].to_dict("records")
    return result_items
```
```
calculate_item_based 함수는 모델에 itemId를 입력하고, 가장 비슷한 11개의 영화를 결과로 반환하는 함수다.
11개로 한 이유는 자기 자신이 제일 높은 유사도로 나오기 때문에 첫 번째 결과를 제외한 10개의 결과를 얻기 위함이다.

item_based_recommendation은 원하는 데이터 형태를 모두 받을 수 있돌고 변환해주는 함수다.
calculate_item_based 함수에서는 가장 비슷한 영화의 movieId만을 출력하기에 원하는 결과를 모두 표시하려면
movieId, title, genres 등 movies_final.csv 파일에 있는 정보를 함께 반환해준다.
```
#### main.py 수정 (/item-based)
```python
@app.get("/item-based/{item_id}")
async def item_based(item_id: str):
    result = item_based_recommendation(item_id)
    return {"result": result}
```
```
/item-based 엔드포인트를 다음과 같이 item_based_recommendation 함수의 결과를 출력하도록 수정한다.
```
#### /item-based/2 CF기반 영화 추천 테스팅
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/a3c71da3-b869-472d-8f92-bdae43f940c2)
```
2번 영화인 Jumanji와 비슷한 영화를 추천받기 위해 localhost:8000/item-based/2로 접속하면 Jumanji와 비슷한
영화 10개가 출력된다.
```
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/03613b2f-d4c5-4ecb-9fa2-e5ace2ff8707)
```
72번 영화인 Kicking and Screaming와 비슷한 영화로 Jumanji가 있다. 
```
## /user-based 엔드포인트
```
/user-based 엔드포인트에서는 유저의 평점을 기반으로 한 추천 결과를 보여준다.
```
#### recommender.py 수정 (calculate_user_based, build_matrix_input, user_based_recommendation)
```python
def calculate_user_based(user_items, items):
    loaded_model = pickle.load(open(saved_model_fname, "rb"))
    recs = loaded_model.recommend(
        userid=0, user_items=user_items, recalculate_user=True, N=10
    )
    return [str(items[r]) for r in recs[0]]


def build_matrix_input(input_rating_dict, items):
    model = pickle.load(open(saved_model_fname, "rb"))
    # input rating list : {1: 4.0, 2: 3.5, 3: 5.0}

    item_ids = {r: i for i, r in items.items()}
    mapped_idx = [item_ids[s]
                  for s in input_rating_dict.keys() if s in item_ids]
    data = [weight * float(x) for x in input_rating_dict.values()]
    # print('mapped index', mapped_idx)
    # print('weight data', data)
    rows = [0 for _ in mapped_idx]
    shape = (1, model.item_factors.shape[0])
    return coo_matrix((data, (rows, mapped_idx)), shape=shape).tocsr()


def user_based_recommendation(input_ratings):
    ratings_df = pd.read_csv(data_fname)
    ratings_df["userId"] = ratings_df["userId"].astype("category")
    ratings_df["movieId"] = ratings_df["movieId"].astype("category")
    movies_df = pd.read_csv(item_fname)

    items = dict(enumerate(ratings_df["movieId"].cat.categories))
    input_matrix = build_matrix_input(input_ratings, items)
    result = calculate_user_based(input_matrix, items)
    result = [int(x) for x in result]
    result_items = movies_df[movies_df["movieId"].isin(
        result)].to_dict("records")
    return result_items
```
```
calculate_user_based에서는 recommend 함수를 사용하여 유저 기반의 추천을 한다.
build_matrix_input 함수를 이용해서 user input을 정의해주어야 한다.
input으로 받는 형태는 {1: 4.5, 2: 4.0}과 같이 python dictionary 형태로 받게 되는데
recommend 함수에서 필요한 데이터 형태가 user-item 간의 coo_matrix이기 때문이다.
```
#### main.py 수정 (/user-based 엔드포인트)
```python
@app.get("/user-based/")
async def user_based(params: Optional[List[str]] = Query(None)):
    input_ratings_dict = dict(
        (int(x.split(":")[0]), float(x.split(":")[1])) for x in params
    )
    result = user_based_recommendation(input_ratings_dict)
    return {"result": result}
```
```
FastAPI에서 url parmeter를 사용하기 위한 기본적인 형태로 input의 형태가 Optional[List[str]] 형태다.
input_rating_dict 변수는 localhost:8000/user-based/?params=1:4.5&params=2:5 url로 접근했을 때
FastAPI에서 params를 ["1:4.5", "2:5"]라는 리스트의 형태를 user_based_recommendation 함수에서 다루기
쉽도록 변환한 것이다.
```
#### /user-based 추천 테스팅
![image](https://github.com/chihyeonwon/OneFlix/assets/58906858/d11e9543-6a78-442d-8c0e-e750265fe959)
```
600번과 609번에 대해 평점 5점을 주고 어떤 결과가 나오는 지 확인하였다.
비슷한 시기에 적당히 흥행했던 작품들이 나온다.
```

