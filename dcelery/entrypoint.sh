#!/bin/ash

echo "Applying database migrations..."

# Apply Django migrations
python manage.py migrate

# Execute the CMD from docker-compose
exec "$@"