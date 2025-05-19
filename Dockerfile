# Gunakan base image Python yang ringan
FROM python:3.9-slim

# Cegah file pyc dan buffer stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Buat user non-root
RUN adduser --disabled-password --no-create-home --gecos '' django

# Siapkan direktori kerja
WORKDIR /app

# Copy requirements.txt terlebih dahulu
COPY requirements.txt .

# Install library sistem yang diperlukan
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy entrypoint.sh dan pastikan executable
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Copy semua source code ke dalam image
COPY . .


# Ubah ownership folder ke user django
RUN chown -R django:django /app

# Gunakan user non-root
USER django

# Jalankan entrypoint
ENTRYPOINT ["bash","./entrypoint.sh"]

# Command default setelah entrypoint jalan
CMD ["gunicorn", "--bind", "0.0.0.0:5005", "core.wsgi:application"]