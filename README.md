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


