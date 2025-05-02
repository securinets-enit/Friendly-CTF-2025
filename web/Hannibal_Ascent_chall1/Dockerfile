# Use a slim Python image
FROM python:3.11-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    iputils-ping \
 && rm -rf /var/lib/apt/lists/*

# Create a user to avoid running as root
RUN useradd -m ctfuser

# Set working directory
WORKDIR /app

# Copy app files
COPY . /app

# Install Flask
RUN pip install --no-cache-dir flask

# Ensure proper permissions
RUN chown -R ctfuser:ctfuser /app

# Switch to non-root user
USER ctfuser

# Expose the app port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
