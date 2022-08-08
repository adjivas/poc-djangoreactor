# navi2
This is a template for a project using Python Django.

## Usage

### Quick Dev Setup

First, configure your `.env` file following the [example.env](./example.env) file.

Run
```shell
docker-compose up -d --build
```

Quick readyness test
```
clafoutis@clafoutis-pro:~/Desktop/work/navi2 # curl localhost:8080/health
{"alive": true}
```

### Dockerless Setup

First, install [pipenv](https://github.com/pypa/pipenv) and [pyenv](https://github.com/pyenv/pyenv).

Run
```shell
pipenv install --dev
```

First, configure your `.env` file following the [example.env](./example.env) file.  
You'll need to have a local database too.

Then run
```shell
pipenv run ./manage.py runserver 0.0.0.0:8080
```

In another terminal, make your readyness test:
```
clafoutis@clafoutis-pro:~/Desktop/work/navi2 # curl localhost:8080/health
{"alive": true}
```
