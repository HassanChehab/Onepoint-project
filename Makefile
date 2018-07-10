.SILENT:
.PHONY: build

# Alias
CONSOLE=php app/console
COMPOSER=composer

## Colors
COLOR_RESET   = \033[0m
COLOR_INFO    = \033[32m
COLOR_COMMENT = \033[33m

## Help command
help:
	printf "${COLOR_COMMENT}Usage:${COLOR_RESET}\n"
	printf " make [target]\n\n"
	printf "${COLOR_COMMENT}Available targets:${COLOR_RESET}\n"
	awk '/^[a-zA-Z\-\_0-9\.@]+:/ { \
		helpMessage = match(lastLine, /^## (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")); \
			helpMessage = substr(lastLine, RSTART + 3, RLENGTH); \
			printf " ${COLOR_INFO}%-16s${COLOR_RESET} %s\n", helpCommand, helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

setup:
	docker-compose build

## Start docker containers
start:
	make setup
	docker-compose up

start@d:
	make setup
	docker-compose up -d

## Stop docker containers
stop:
	docker-compose stop

CONTAINERS=$(shell docker ps -a -q)
VOLUMES=$(shell docker volume ls -qf dangling=true)

## Remove docker containers
destroy:
	make stop
	# rm ./.dockers/apache/certs/*
	docker rm $(CONTAINERS) 2>/dev/null; true
	docker volume rm $(VOLUMES) 2>/dev/null; true

###########
# Install #
###########
## Install project dependencies
install:
	pip install -r web/requirements.txt

## Install dependencies on Docker host
install@docker:
	docker exec web pip install -r web/requirements.txt
