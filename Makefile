
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
