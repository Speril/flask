# 가져올 이미지
FROM python:3.7-alpine

# bash를 사용하기 위해 설치
RUN apk update && \
        apk add --no-cache \
        bash

# python 기본 패키지
RUN apk add --update build-base python3-dev py-pip

# 환경변수
ENV LIBRARY_PATH=/lib:/usr/lib

# 호스트와 연결할 포트 ( 이렇게 빌드하는 이유는 추후 jwilder/nginx-proxy 를 위해서 입니다 )
EXPOSE 3000

# 기본 디렉토리
WORKDIR /var/www/html
COPY . /var/www/html/

# flask 설치
RUN pip install flask

# 실행 명령어
CMD ["python", "app.py"]