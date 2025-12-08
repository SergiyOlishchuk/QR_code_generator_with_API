import uvicorn
from fastapi import FastAPI

from routing import router as main_router
from settings import settings

app = FastAPI(
    title="QR Code Generator API",
    description="Simple QR Code Generator",
    version="1.0",
    redoc_url=None,
)

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=settings.APP_PORT)
