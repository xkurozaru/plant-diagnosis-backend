run:
	poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

up:
	sudo docker compose up --build
