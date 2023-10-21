import logging
from typing import Union
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def read_root():
    return {"Hello" : "World"}

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    error_response = JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
    logging.error("Exception handler response: %s", error_response.json())
    return error_response
