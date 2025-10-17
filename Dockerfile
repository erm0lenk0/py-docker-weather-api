FROM python:3.11

LABEL maintainer="f1nd6r@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py", "runserver", "0.0.0.0:8000"]
