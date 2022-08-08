FROM python:3.10

WORKDIR /app
COPY Pipfile Pipfile.lock ./

RUN pip install --upgrade pip pipenv \
    && pipenv install --dev --deploy --system

COPY . .

EXPOSE 80

ENTRYPOINT ["./manage.py", "runserver", "0.0.0.0:80"]
