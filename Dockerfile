FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the working directory
COPY . .

# Install git
RUN apt-get update && apt-get install -y git

# Install git
RUN pip install git+https://github.com/suno-ai/bark.git

# Expose the port that the API will listen on
EXPOSE 8000

# Start the API server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
