import uvicorn
from fastapi import FastAPI, HTTPException, Request
from starlette.responses import JSONResponse
from app.api import router as api_router
from app.web.utils import error_response

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    try:
        body = await request.json()
    except Exception as e:
        body = None
    return error_response(exc.detail, exc.status_code, body)


app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
