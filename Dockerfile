FROM python:3.11-slim-bookworm

RUN useradd wagtail

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=8000

EXPOSE ${PORT}

WORKDIR /app

RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
  curl \
  libjpeg62-turbo-dev \
  zlib1g-dev \
  libwebp-dev \
  && rm -rf /var/lib/apt/lists/*

RUN curl -sLO https://github.com/tailwindlabs/tailwindcss/releases/latest/download/tailwindcss-linux-x64 && \
  mv tailwindcss-linux-x64 tailwindcss && \
  chmod +x tailwindcss

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN chown wagtail:wagtail /app

# COPY --chown=wagtail:wagtail . .

# USER wagtail

CMD set -xe; python manage.py collectstatic --noinput --clear; python manage.py migrate --noinput; gunicorn songbird.wsgi:application
