#!/bin/bash
# entrypoint.sh

set -e

echo "Menunggu database siap di $POSTGRES_HOST:$POSTGRES_PORT ..."

# Loop tunggu sampai database ready
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  echo "Database belum siap - menunggu 1 detik..."
  sleep 1
done

echo "Database sudah siap!"

# Migrate
echo "Menjalankan migrate..."
python manage.py migrate --noinput

# Collect static files
echo "Mengumpulkan static files..."
python manage.py collectstatic --noinput --clear

# Jalanin gunicorn (yang dari CMD)
echo "Menjalankan aplikasi..."
exec "$@"
