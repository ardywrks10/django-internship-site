FROM python:3.11-slim AS production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirements/prod.txt ./requirements/prod.txt
RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir -r ./requirements/prod.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY internship_website ./internship_website

EXPOSE 8000

FROM production AS development

COPY requirements/dev.txt ./requirements/dev.txt
RUN python -m pip install --no-cache-dir -r requirements/dev.txt

COPY . .