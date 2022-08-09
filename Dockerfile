FROM python:3.10-slim AS builder

WORKDIR /app

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential
RUN apt-get install -y git
RUN apt-get install -y npm nodejs

COPY Pipfile Pipfile.lock ./

RUN pip install --upgrade pip pipenv
RUN pipenv install --dev --deploy --system

COPY . .

EXPOSE 80

ENTRYPOINT ["./manage.py", "runserver", "0.0.0.0:80"]
