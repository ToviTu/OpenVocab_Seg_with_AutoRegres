IMAGE_NAME=tovitu/coseg

build:
	docker build . -t ${IMAGE_NAME} 
push:
	docker push ${IMAGE_NAME}
clean: 
	docker system prune -af
