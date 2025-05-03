# vulnerable-app4/Dockerfile

FROM python:3.6

WORKDIR /code
COPY . .

RUN pip install Flask==1.0.2

EXPOSE 8080
CMD ["python", "app.py"]
