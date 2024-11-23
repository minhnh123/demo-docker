# Base image
FROM python:3.12

# Set work directory
WORKDIR /app

# Copy application files
COPY app.py /app
COPY requirements.txt /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
