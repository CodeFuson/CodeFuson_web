# Use official Python image from Docker Hub
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django app
COPY . /app/

# Expose port 8000 for the Django app
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
