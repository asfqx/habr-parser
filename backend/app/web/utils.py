from typing import Optional

from fastapi.responses import JSONResponse


def json_response(data: dict | list, status_code: int = 200):
    return JSONResponse(content={"status": "ok", "data": data}, status_code=status_code)


def error_response(
    message: str, status_code: int = 400, data: Optional[dict] = None
) -> JSONResponse:
    return JSONResponse(
        content={"status": "error", "message": message, "data": data},
        status_code=status_code,
    )
