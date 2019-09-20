# SODASITE
소프트웨어 공개 소프트웨어 소모임 SODA 공식 홈페이지



### 도커 이미지

코드를 고치고 이미지를 만들 경우 다음의 과정을 수행한다.

root디렉터리에 Dockerfile : 도커 이미지

> 다음 명령들은 root레벨에서 수행

1. Dockerfile로 sodasite라는 도커 이미지를 생성한다.

   **태그는 v1, v2와 같은 식으로 버전을 명시한다.**

```
$ sudo docker image build -t sodasite/sodasite:v? .
```

2. 도커 이미지 run

```
$ sudo docker run --rm -it -p 80:8000 sodasite/sodasite:v?
```

3. ```localhost```에서 실행중임을 확인할 수 있다.

4. 이미지가 잘 동작함을 확인했으므로 만든 이미지를 도커 허브에 올린다. 

   **태그를 꼭 명시해준다.**

```
$ sudo docker login
$ sudo docker push sodasite/sodasite:v?
```



### 배포

위에서 만든 도커 이미지를 AWS에 배포해본다.

이미지는 Docker hub에 ```sodasite/sodasite```라는 이름으로 올라가있다.

AWS에 ubuntu 인스턴스를 생성하고 ssh key를 받는다.



그러면 local에서 아까 받은 key를 통해 ssh접속을 할 수 있다.

```
$ chmod 400 <key.pem>
$ ssh -i "<key.pem>" ubuntu@<public DNS>
```



접속이 되었으면 docker를 설치한다. unable to locate에러가 뜨면 ```apt-get update```를 수행한다.

```
$ sudo apt-get install docker.io
$ sudo docker login
$ sudo docker pull sodasite/sodasite:v?
$ sudo docker run --rm -it -p 80:8000 sodasite/sodasite:v?
```



그럼 public IP로 웹에서 확인이 가능하다.