
FROM python:3.10-slim


WORKDIR /app


RUN apt-get update && apt-get install -y build-essential libatlas-base-dev libpq-dev


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  # Telepítjük a Python csomagokat


COPY . .


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
