.PHONY: install
install:
	poetry install

.PHONY: update
update:
	poetry update
	pre-commit autoupdate

.PHONY: lint
lint:
	ruff check .

.PHONY: format
format:
	black .

.PHONY: clean
clean:
	rm -rf .ruff_cache media static tailwindcss
	rm -rf ./home/__pycache__
	rm -rf ./songbird/__pycache__

.PHONY: run
run:
	python manage.py runserver

.PHONY: compose-up
compose-up:
	docker-compose up -d --build

.PHONY: compose-down
compose-down:
	docker-compose down

.PHONY: compose-prod-up
compose-prod-up:
	docker-compose -f docker-compose.prod.yaml up -d --build

.PHONY: compose-prod-down
compose-prod-down:
	docker-compose -f docker-compose.prod.yaml down

.PHONY: flush
db-flush:
	docker-compose exec web python manage.py flush --no-input

.PHONY: migrate
migrate:
	docker-compose exec web python manage.py migrate

.PHONY: tailwind-compose-watch
tailwind-compose-watch:
	docker-compose exec web ./tailwindcss -i ./theme/*.css -o ./songbird/static/css/style.css --watch

.PHONY: tailwind-compose-build
tailwind-compose-build:
	docker-compose exec web ./tailwindcss -i ./theme/*.css -o ./songbird/static/css/style.css --minify

.PHONY: start
start: compose-down compose-up migrate tailwind-compose-watch

.PHONY: start-prod
start-prod: compose-prod-down compose-prod-up migrate tailwind-compose-build
