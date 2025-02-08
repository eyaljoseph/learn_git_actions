# Use an official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on (adjust this if your app uses a different port)
EXPOSE 8080

# Set the command to run your app (adjust this based on your app's entry point)
CMD ["python", "main.py"]
