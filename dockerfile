# Use official Python image
FROM python:3.10.12

# Set working directory inside the container
WORKDIR /app

# Copy project files into container
COPY . /app

# Install dependencies
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt

# Expose port Django runs on
EXPOSE 8000

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
