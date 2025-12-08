FROM python:3.13.10-slim-trixie

WORKDIR /app

COPY requirements.txt requirements.txt
COPY pyproject.toml pyproject.toml

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src

CMD ["python3", "main.py"]