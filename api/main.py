# FastAPI app for model serving
from fastapi import FastAPI
app = FastAPI()
@app.get('/')
def read_root():
    return {'message': 'Model is ready'}