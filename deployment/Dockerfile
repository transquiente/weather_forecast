FROM python:3.10-alpine AS base
ENV PYTHONUNBUFFERED 1

FROM base AS builder
ENV POETRY_VERSION=1.8.2
RUN apk update
RUN apk add --no-cache postgresql-dev build-base gcc musl-dev openssl-dev libffi-dev cargo freetype freetype-dev
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv
COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin --no-deps

FROM base AS app-base
RUN addgroup -S nonroot && adduser -S nonroot -G nonroot
WORKDIR /app
COPY pyproject.toml alembic.ini /app/
COPY migrations /app/migrations
COPY tools /app/tools
COPY app /app/app

FROM app-base AS deploy-app
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"
USER nonroot
CMD alembic upgrade head
CMD uvicorn --factory tools.start_web:create_app --host 0.0.0.0 --port 8000 --proxy-headers --forwarded-allow-ips "*"

FROM app-base AS test
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"
COPY tests /app/tests
USER nonroot
ENTRYPOINT ["pytest"]
CMD ["tests"]
