# ---------- Stage 1: Build dependencies ----------
    FROM python:3.10-slim as build

    WORKDIR /app
    
    # Install build dependencies
    RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential gcc \
        && rm -rf /var/lib/apt/lists/*
    
    COPY requirements.txt .
    
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy application code
    COPY . .
    
    # ---------- Stage 2: Final image ----------
    FROM python:3.10-slim
    
    # Create a non-root user
    RUN adduser --disabled-password --gecos '' appuser
    
    WORKDIR /app
    
    # Copy only the needed files from build
    COPY --from=build /app /app
    
    # Use non-root user
    USER appuser
    
    # Expose app port
    EXPOSE 5000
    
    # Default command
    ENTRYPOINT ["python"]
    CMD ["app.py"]
    