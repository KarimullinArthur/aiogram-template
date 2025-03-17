FROM python:3.13-alpine

RUN addgroup -g 1001 app && \
    adduser -S -s /bin/sh -u 1001 -G app app && \
    apk add poetry

USER app

WORKDIR /app

COPY --chown=app:app . .

RUN poetry install --no-root

WORKDIR /app/src/bot

CMD ["poetry", "run", "python", "main.py"]
