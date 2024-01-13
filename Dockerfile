FROM python:3.10 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes


FROM python:3.10

WORKDIR /app

COPY --from=requirements-stage /tmp/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY .env /app/.env
COPY ./src /app/src
COPY ./ssl /app/ssl

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--ssl-keyfile", "./ssl/key.pem", "--ssl-certfile", "./ssl/cert.pem"]
