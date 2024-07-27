include deployment/docker.env
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

lint:
	@poetry run mypy .
# Lint all files in the current directory.
	@poetry run ruff check .
# Exit with a non-zero status code upon detecting any unformatted files.
	@poetry run ruff format --check .

format:
# Sorting imports
	@poetry run ruff check --select I --fix .
# Lint all files in the current directory, and fix any fixable errors.
	@poetry run ruff check --fix .
# Format all files in the current directory.
	@poetry run ruff format .
