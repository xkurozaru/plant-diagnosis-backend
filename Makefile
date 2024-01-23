run:
	poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

up:
	docker compose up --build -d

logs:
	docker compose logs -f
