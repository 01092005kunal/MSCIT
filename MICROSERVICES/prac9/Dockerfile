FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY process_data.py .
COPY main.py .
COPY bank.csv .
COPY requirements.txt .

# Install required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Process CSV when building the image
RUN python process_data.py

# FastAPI port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]