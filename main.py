# uvicorn main:app --reload --host 192.168.31.67 --port 8001

import asyncio
import router_menu
import router_cooking
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI(
    title="FreshFamilyMeal",
    description="This is a detailed description of FreshFamilyMeal API.",
    version="1.0.0",
)

# Create an async lock
lock = asyncio.Lock()


class AsyncLockMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Acquire the lock before processing the request
        async with lock:
            response = await call_next(request)
        # The lock is released automatically when the request is done
        return response


# Add the middleware to the FastAPI app
app.add_middleware(AsyncLockMiddleware)

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")


# Route to serve favicon.ico
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return RedirectResponse(url="/static/favicon.ico")


@app.get("/", tags=["Home"])
async def root(req: Request):
    client_ip = req.client.host
    return {"client_ip": client_ip, "message": "Hello, World!!!"}


app.include_router(router_menu.router)
app.include_router(router_cooking.router)
