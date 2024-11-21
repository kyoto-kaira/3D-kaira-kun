build:
	docker build -t moving-kaira-kun .

run:
	docker run -it --rm -v ${PWD}:/app -p 8501:8501 --name moving-kaira-kun moving-kaira-kun
