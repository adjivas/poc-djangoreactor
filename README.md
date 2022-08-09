# Reactor Example
### how to build
```
pipenv install
docker-compose build

docker-compose exec navi2 python manage.py migrate
docker-compose exec navi2 bash
root:/app# cd ./src/djangoreactor
root:/app# npm install
root:/app# node esbuild.conf.js
```

### how to run
```
docker-compose up
curl http://127.0.0.1:8080
```
