include deployment/local.env
export

# there should be tabs not white spaces - will be an error

run: postgres
	@uvicorn --factory tools.start_web:create_app --host 0.0.0.0 --port 8000 --proxy-headers --forwarded-allow-ips "*"

postgres:
	@docker compose up postgres -d

build:
	@docker compose -f docker-compose.yml build

up: build
	@docker compose -f docker-compose.yml up -d

down:
	@docker compose -f docker-compose.yml down

ps:
	@docker ps

migration: postgres
	@poetry run alembic revision --autogenerate -m "$(args)"

check: postgres
	@poetry run alembic check

migrate: postgres
	@poetry run alembic upgrade head

downgrade: postgres
	@poetry run alembic downgrade -1

lint:
	@poetry run mypy .
# Lint all files in the current directory.
	@poetry run ruff check .
# Exit with a non-zero status code upon detecting any unformatted files.
	@poetry run ruff format --check .

format:
# Sorting imports
	@poetry run ruff check --select I --fix .
# Format all files in the current directory.
	@poetry run ruff format .
# Lint all files in the current directory, and fix any fixable errors.
	@poetry run ruff check --fix .

test:
	@DB_DATABASE=postgres_test poetry run pytest -s $(args)
