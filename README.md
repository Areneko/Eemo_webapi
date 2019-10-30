# Eemo api

## How to run

### Setup
```
$ git clone https://github.com/Areneko/Eemo_webapi.git
$ cd Eemo_webapi
```

### Run python

#### Use docker
```
$ cp .env.example .env (And rewirte to your values)
$ make start
```

#### Not use docker
```
$ pip install flask
$ python python/src/app.py
```