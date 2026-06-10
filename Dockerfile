FROM python:3.11-slim

WORKDIR /app

COPY word_game.py .

CMD ["python", "-u", "word_game.py"]