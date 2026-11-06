"""FastAPI application entrypoint for BusTrack GenAI service."""

import uuid
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from src.api.routes import router
from src.core.config import load_config


def create_app() -> FastAPI:
    """Create and configure the FastAPI application instance."""
    cfg = load_config()
    application = FastAPI(
        title="BusTrack GenAI Service",
        description="Servicio interno de recomendaciones explicables con grounding.",
        version=cfg.service_version,
    )

    @application.middleware("http")
    async def correlation_id_middleware(request: Request, call_next):
        correlation_id = request.headers.get("X-Correlation-ID", str(uuid.uuid4()))
        response = await call_next(request)
        response.headers["X-Correlation-ID"] = correlation_id
        return response

    @application.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        _request: Request, _exc: RequestValidationError
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Contexto de entrada invalido."},
        )

    @application.exception_handler(Exception)
    async def generic_exception_handler(
        _request: Request, _exc: Exception
    ) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "Error interno del servicio."},
        )

    application.include_router(router)
    return application


app = create_app()
