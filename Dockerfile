# Use official Python 3.9 image
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy specific files and folders into the container
COPY app.py /app/
COPY requirements.txt /app/
COPY schema.py /app/

# Fetch model and scaler from GitHub releases
RUN mkdir -p /app/models /app/scaling
RUN curl -L -o /app/models/model.pkl https://github.com/username/repo/releases/download/v1.0/model.pkl
RUN curl -L -o /app/scaling/scaler.pkl https://github.com/username/repo/releases/download/v1.0/scaler.pkl


# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (matching uvicorn command below)
EXPOSE 8080

# Run the FastAPI app with uvicorn on all interfaces and port 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
