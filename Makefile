.PHONY: build
build:
	docker build . -t flask

.PHONY: run 
run:
	docker run -v $(CURDIR)/src:/app -p 5000:5000 -it flask

.PHONY: start
start:
	make build && make run

.PHONY: prune
prune:
	docker system prune --force