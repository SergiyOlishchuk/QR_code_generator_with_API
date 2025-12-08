from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Query
from fastapi.responses import StreamingResponse

from generator import QRCodeGenerator
from schemas import QRRequest, DefaultAnswer

router = APIRouter()


async def process_get_qr_code(data: QRRequest):
    img_buf = QRCodeGenerator(data=data).run()
    return StreamingResponse(img_buf, media_type="image/png")


@router.get("/qr")
async def qr_get(data: Annotated[QRRequest, Query()]) -> StreamingResponse:
    return await process_get_qr_code(data)


@router.post("/qr")
async def qr_post(data: QRRequest) -> StreamingResponse:
    return await process_get_qr_code(data)


@router.get("/")
async def root() -> DefaultAnswer:
    return DefaultAnswer(message="QR Code Generator", info="Docs: /docs")
