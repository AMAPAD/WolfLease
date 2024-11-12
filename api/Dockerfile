# Use Python 3.11 slim as the base image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files and to ensure output is flushed
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy requirements file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project into the container
COPY . /app

# Expose the port Django will run on
EXPOSE 8000

# Run migrations and then start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]