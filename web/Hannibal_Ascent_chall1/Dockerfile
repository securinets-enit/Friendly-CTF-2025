FROM python:3.11-slim

# Don't cache pip installs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY app.py .
COPY templates/ templates/

# Expose only the challenge port
EXPOSE 4523

# Run securely using python (not flask CLI)
CMD ["python", "app.py"]
