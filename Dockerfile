# Use a lightweight Python base image
FROM python:3.9-slim

# Install system dependencies (needed for evdev and Python C extensions)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libevdev-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Copy requirements file first for Docker cache efficiency
COPY requirements.txt .

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir Werkzeug==2.2.3

# Copy application code
COPY . .

# Expose the Flask port
EXPOSE 5000

# Run the app as a module inside the package
CMD ["python", "-m", "app.main"]

