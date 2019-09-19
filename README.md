# SODASITE
소프트웨어 공개 소프트웨어 소모임 SODA 공식 홈페이지



### 도커 이미지

root디렉터리에 Dockerfile : 도커 이미지

> 다음 명령들은 root레벨에서 수행

1. Dockerfile로 sodasite라는 도커 이미지 생성

```
$ sudo docker image build -t sodasite .
```

2. 도커 이미지 run

```
$ sudo docker run --rm -it -p 80:8000 sodasite
```

3. ```localhost:80```에서 실행중임을 확인할 수 있다.



### 배포

위에서 만든 도커 이미지를 클라우드에 배포해본다.