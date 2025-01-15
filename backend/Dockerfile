FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml pdm.lock /app/
RUN pip install pdm && pdm install

COPY ./backend /app/backend

CMD ["pdm", "run", "flask", "--app", "app:create_app", "run"]
