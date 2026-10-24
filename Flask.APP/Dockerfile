
# 1. Base image
FROM python:3.12-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy dependency file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY app.py .

# 6. Expose application port
EXPOSE 5000

# 7. Start Flask application
CMD ["python", "./app.py"]
