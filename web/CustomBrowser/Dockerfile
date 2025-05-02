FROM python:3.11-slim

# Create a user for better security
RUN useradd -m ctfuser

WORKDIR /home/ctfuser/app

# Copy app code
COPY app.py .

# Install Flask
RUN pip install --no-cache-dir flask

# Drop privileges
USER ctfuser

EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
