# Gunakan base image yang lebih ringan
FROM python:3.9-slim

# Cegah pembuatan file pyc dan gunakan log stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Buat user non-root untuk menjalankan aplikasi
RUN adduser --disabled-password --no-create-home --gecos '' django

# Siapkan direktori kerja
WORKDIR /app

# Copy file requirements dulu (agar layer cache bisa digunakan)
COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*
    
# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Salin seluruh source code
COPY . .

# # Jalankan collectstatic (biasanya dilakukan di entrypoint/start script, tapi bisa di sini)
# RUN python manage.py collectstatic --noinput

# Ubah ownership folder ke user django (non-root)
RUN chown -R django:django /app

# Gunakan user non-root
USER django

ENTRYPOINT ["./entrypoint.sh"]
# Jalankan aplikasi menggunakan gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
