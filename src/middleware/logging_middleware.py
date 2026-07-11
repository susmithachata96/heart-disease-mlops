import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/api.log"),
        logging.StreamHandler()
    ],
)

logger = logging.getLogger("api_logger")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        response = await call_next(request)

        process_time = time.time() - start_time

        logger.info(
            "%s %s | Status: %s | Time: %.4fs | Client: %s",
            request.method,
            request.url.path,
            response.status_code,
            process_time,
            request.client.host,
        )

        return response