from io import BytesIO
from typing import Callable

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import (
    RoundedModuleDrawer,
    CircleModuleDrawer,
    GappedSquareModuleDrawer,
    HorizontalBarsDrawer,
    SquareModuleDrawer,
    VerticalBarsDrawer,
)

from schemas import QRRequest


def parse_quality(quality: str) -> int:
    parse_dict = {
        "low": 1,
        "medium": 0,
        "quartile": 3,
        "high": 2,
    }
    return parse_dict.get(quality, 0)


def parse_drawer(drawer: str) -> Callable:
    parse_dict = {
        "CircleModuleDrawer": CircleModuleDrawer,
        "GappedSquareModuleDrawer": GappedSquareModuleDrawer,
        "HorizontalBarsDrawer": HorizontalBarsDrawer,
        "RoundedModuleDrawer": RoundedModuleDrawer,
        "SquareModuleDrawer": SquareModuleDrawer,
        "VerticalBarsDrawer": VerticalBarsDrawer,
    }
    return parse_dict.get(drawer, 0)


class QRCodeGenerator:
    def __init__(self, data: QRRequest):
        self.data = data

    def make_qr_code_image(self):
        qr = qrcode.main.QRCode(
            version=self.data.size,
            error_correction=parse_quality(self.data.quality),
            box_size=self.data.box_size,
            border=self.data.border,
        )

        qr.add_data(self.data.data)
        qr.make(fit=(self.data.size is None))

        return qr.make_image(
            fill_color=self.data.fill_color.as_hex(),
            back_color=self.data.back_color.as_hex(),
            image_factory=StyledPilImage,
            module_drawer=parse_drawer(self.data.drawer_type)(),
        )

    def run(self):
        img = self.make_qr_code_image()
        buf = BytesIO()
        img.save(buf, format="PNG")
        buf.seek(0)
        return buf
