# Black76's REST API

This API was built using:

- Python 3.11
- FastAPI
- SQLite 3

Steps to run the API:
- Create a virtual env locally: ```python3 -m venv venv```
- Activate the virtual env: ```source venv/bin/activate```
- Install the dependencies: ```pip3 install -r requirements.txt```
- Set up the test database: ```python3 db/load.py```
- Run the API: ```uvicorn app.api:black76```
- Go to http://127.0.0.1:8000/redoc to test the API

To unit test the API:
- Run ```pytest``` from root directory