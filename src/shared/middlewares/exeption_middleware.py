from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import logging
from json.decoder import JSONDecodeError

from src.shared.utils.custom_exeption import CustomAppException

logger = logging.getLogger(__name__)

async def exception_middleware(request: Request, call_next):
    try:

        if request.headers.get("content-type") == "application/json":
            try:
                await request.json()
            except JSONDecodeError as json_error:
                logger.error(f"Error de decodificación JSON: {str(json_error)}")
                return JSONResponse(
                    content={
                        "code_error": 400,
                        "msg": "JSON inválido. Verifica la sintaxis de la solicitud."
                    },
                    status_code=400
                )

        response = await call_next(request)
        return response
    except RequestValidationError as validation_error:
        logger.error(f"Error de validación: {validation_error.errors()}")
        return JSONResponse(
            content={
                "code_error": 422,
                "msg": "Error de validación en la solicitud."
            },
            status_code=422
        )
    except CustomAppException as custom_exc:
        logger.error(f"CustomAppException detectada: {custom_exc.msg}")
        return JSONResponse(
            content={
                "code_error": custom_exc.code_error,
                "msg": custom_exc.msg
            },
            status_code=custom_exc.status_code
        )
    except Exception as e:
        logger.exception(f"Excepción no capturada: {str(e)}")
        return JSONResponse(
            content={
                "code_error": 500,
                "msg": "Ocurrió un error interno del servidor."
            },
            status_code=500
        )
