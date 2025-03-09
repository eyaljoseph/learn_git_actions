# Use an official Python image as the base image
FROM python:3.10-slim

# Create non-root user
RUN useradd -m appuser

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Switch to non-root user
USER appuser

# Expose the port the app runs on (adjust this if your app uses a different port)
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Set the command to run your app (adjust this based on your app's entry point)
CMD ["python", "main.py"]
