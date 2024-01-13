run:
	poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload --ssl-keyfile ./ssl/key.pem --ssl-certfile ./ssl/cert.pem
