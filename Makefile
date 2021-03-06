
.PHONY: help
help :
	@echo "up:\t\tup container"
	@echo "down:\t\tdown container"
	@echo "format:\t\tformat code where possible."

.PHONY: up 
up:
	@docker-compose up -d

.PHONY:
down: up
	@docker-compose down

.PHONY: format
format: up 
	@docker-compose exec trender isort .
	@docker-compose exec trender black .

.PHONY: shell
shell: up
	@docker-compose exec trender bash

.PHONY: build
build:
	@docker-compose build trender

.PHONY: logs
logs:
	@docker-compose logs trender

.PHONY: dshell
dshell: up
	@docker-compose exec trender python manage.py shell

.PHONY: test
test: up
	@docker-compose exec trender pytest scraper
