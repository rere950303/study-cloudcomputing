# Docker hub ID
rere95

# 명령어 정리
```bash
sudo docker build -t rere95/ping:v1 .

sudo docker build -t rere95/pong:v1 .

sudo docker run -d -p 5000:5000/tcp --name ping {image id}

sudo docker run -d -p 5001:5001/tcp --name pong {image id}

sudo docker network create project1

sudo docker network connect project1 {container id}
```
- 그 외 `commit`, `tag`, `push`와 같은 기타 명령어들은 과제 ppt에 나와있는 내용을 참고했음

# app.py, Dockerfile
## ping
```python
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '[sender_ping] Hello stranger, I am ping container! nice to meet u!!!!!\n'

@app.route('/ping')
def ping():
    request = '---ping--->'
    response = requests.get('http://pong:5001/pong').text
    return '[sender_ping] ' + request + '[receiver_pong] ' + response + '\n'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
```

## pong
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '[receiver_pong] Hello, I am pong container! nice to meet you\n'

@app.route('/pong')
def pong():
    return 'Hi Hi Hi'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
```

## Dockerfile
```Dockerfile
FROM python:3.8-slim

COPY . /app

RUN pip3 install flask requests

WORKDIR /app

ENTRYPOINT [ "python", "app.py" ]
```

# 간략한 설명
## ping
- 포트 번호를 5000으로 해서 서버를 띄우고 requests를 이용하여 pong 컨테이너로 http 요청을 보낸다.

## pong
- 포트 번호를 5001로 해서 서버를 띄우고 각 URL 요청에 대응되는 값을 반환한다.

## Dockerfile
- 베이스 layer를 python으로 하고 Dockerfile이 존재하는 폴더를 /app 폴더로 복사하고 pip3 패키지 관리 툴을 이용하여 flask 등을 설치한다. 이후 ENTRYPOINT 명령어를 통해 이미지로 컨테이너 실행 시 app.py를 실행시킨다.

<br>

# network 캡쳐 화면
![스크린샷 2022-11-04 오후 12 41 04](https://user-images.githubusercontent.com/78265252/199880562-7172e974-7879-491d-a0b0-d6d0085c81f3.png)

<br><br><br><br><br><br>

# ping, pong 캡쳐 화면
![스크린샷 2022-11-04 오후 12 45 44](https://user-images.githubusercontent.com/78265252/199881140-7c23e6dd-fb62-4094-a7b7-74f24d9d585e.png)

# push 캡쳐 화면
## ping
![스크린샷 2022-11-04 오후 12 49 49](https://user-images.githubusercontent.com/78265252/199881607-2dac7d70-4ba1-4c3a-afcc-fe318ddd28b5.png)

<br><br>

## pong
![스크린샷 2022-11-04 오후 12 50 02](https://user-images.githubusercontent.com/78265252/199881646-8ebb6251-7d2d-42de-89d0-4f2db8bfebf0.png)
