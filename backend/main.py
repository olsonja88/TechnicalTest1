import logging, uuid, datetime
from dateutil.relativedelta import relativedelta
from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse

app = FastAPI()

logging.basicConfig(level=logging.INFO)

@app.get("/")
def get_data():
    unique_uuid = str(uuid.uuid4())
    current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    expires_at = (current_time + relativedelta(months=1)).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return {"uuid" : unique_uuid,
            "document_name": "Super Top Secret Halloween Costume Ideas",
            "current_time": current_time,
            "description": "A list of the best halloween costumes.",
            "expires_at": expires_at}

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request, exc):
    error_response = JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )
    logging.error("Exception handler response: %s", error_response.json())
    return error_response
