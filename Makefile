build:
	docker build . -t flask
run:
	docker run -v $(CURDIR)/src:/app -p 5000:5000 -it flask
start:
	make build && make run
prune:
	docker system prune --force