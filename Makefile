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
