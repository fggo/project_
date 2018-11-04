# Overview
1. 네이버 smartstore에 등록된 판매자들의 상품을 대상으로 했습니다.
2. 판매자(seller) 아이디는 미리 정해놓고 테스트를 진행했습니다. [ex] seller='naemall'<br>
    따라서, server.py에 seller는 부득이 하게 hardcoding 했습니다.
3. '할인가'을 return하도록 구현했습니다.


# Development Set up

## Create and Activate virtual environment
tested on Fedora 29
```commandline
cd $HOME/project_ && ls
    requirements.txt
    
cat requirements.txt
    scrapy==1.4.0
    Flask==1.0.2
    
pipenv install -r requirements.txt --python=/usr/bin/python3.6
pipenv shell  # activate virtual environment
```

## Scrapy project set up
```commandline
(project_)cd $HOME/project_
(project_)scrapy startproject get_price .
(project_)cd $HOME/project_/get_price/spiders/

(project_)touch priceSpider.py
```

## Flask server set up
```commandline
(project_)pwd
    $HOME/project_
(project_)touch server.py

# run flask server
(project_)env FLASK_APP=server.py flask run
```


# Docker implementation
virtual env대신, docker를 이용한 flask서버 구동 방법을 찾아보고 있습니다.

## Create Dockerfile
```dockerfile
FROM ubuntu:16.04
MAINTAINER jnuho "jnuho@outlook.com"
RUN apt update -y && \
    apt install -y python-pip python-dev
    
   
# install all dependencies (flask, scrapy)
COPY ./requirements.txt /app/requirements.txt



WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT ["python"]

CMD ["server.py"]
```

## Build the image
```commandline
docker build -t project_:latest .
docker run -d -p 5000:5000 project_
```


# How my API works?
1. flask를 이용한 server.py 에서 spider정보를 가지고 커맨드라인 scrapy crawl [spider_name] -o [output.json] -a param1=val1 -a param2=val2 을 subprocess를 이용하여 실행시켰습니다.
2. priceSpider.py는 이 subprocess를 통해 scraping작업을 하고 결과물을 yield를 통해 json에 저장합니다.
3. 다시 server.py에서 해당 데이터를 read하여 flask server running 되고 있는 상태에서 http://localhost:5000/product_id를 통해 할인가를 확인할 수 있습니다.