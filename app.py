from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
inventory = {}

@app.get('/')
def root():
    return {'data': 'some json data'}

@app.get('/ip')
def api():
    return {'status-code': 200, 'ip': None}

@app.get('/ip/get')
def api(req: Request):
    return {'status-code': 200, 'ip': req.client.host}

