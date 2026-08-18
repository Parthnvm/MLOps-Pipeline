# Using official pythong runtime as parent image
FROM python:3.9-slim

# Setting up working directory
WORKDIR /app

# Copyin requirement list and installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-die -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000


# Command to run the application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]