FROM python:3.9-slim

RUN mkdir -p /app
WORKDIR /app

# python settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install dependencies
COPY resume/requirements.txt . 
COPY resume/migrate.sh . 
RUN python -m pip install --no-cache-dir -r requirements.txt
RUN chmod +x migrate.sh

# copy the django app
COPY resume .

# django port
EXPOSE 8000

# collect static into single folder
RUN python manage.py collectstatic --noinput

# serving django with gunicorn on port 8000 (timeout 60 seconds)
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-t", "60", "core.wsgi"]