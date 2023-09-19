# Use an official Python runtime as a parent image
FROM python:3.9

# Create and set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the Django application code into the container
COPY . /app/

# Run database migrations (apply changes to the database schema)
RUN python manage.py migrate

# Collect static files (for serving static assets)
RUN python manage.py collectstatic --noinput

# Expose the port your Django app runs on
EXPOSE 8000

# Start your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
