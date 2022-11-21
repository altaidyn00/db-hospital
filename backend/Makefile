clean:
	find . -name __pycache__ -type d -exec rm -r {} +

run:
	python3 -m uvicorn app.main:app --reload

dependencies:
	pip3 install -r requirements.txt