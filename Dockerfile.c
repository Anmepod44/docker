# vulnerable-app3/Dockerfile

FROM python:3

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "main.py"]
