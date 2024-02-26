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








