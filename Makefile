start:
	docker-compose up --build
restart:
	docker-compose up
kill:
	docker-compose kill
logs:
	docker-compose logs
ps:
	docker-compose ps
bash:
	docker-compose exec flask ash
setup:
	docker-compose exec flask python setup.py