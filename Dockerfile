# Base image
FROM python:3.10-slim-buster

# Set work directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Ensure the script is executable
RUN chmod +x ./run.sh

# Set entrypoint
ENTRYPOINT ["bash", "./run.sh"]
