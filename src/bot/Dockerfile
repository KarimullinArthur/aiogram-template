FROM python:3.13-alpine


RUN addgroup -g 1001 app && \
    adduser -S -s /bin/sh -u 1001 -G app app && 

USER app

WORKDIR /app

COPY --chown=app:app . .

RUN pip install 

WORKDIR /app/src/bot

CMD ["python", "main.py"]
