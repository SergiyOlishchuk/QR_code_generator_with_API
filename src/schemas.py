from enum import StrEnum

from pydantic import BaseModel, Field
from pydantic_extra_types.color import Color


class DefaultAnswer(BaseModel):
    success: bool = True
    message: str
    info: str | None


class ErrorCorrect(StrEnum):
    low = "low"
    medium = "medium"
    quartile = "quartile"
    high = "high"


class DrawerType(StrEnum):
    CircleModuleDrawer = "CircleModuleDrawer"
    GappedSquareModuleDrawer = "GappedSquareModuleDrawer"
    HorizontalBarsDrawer = "HorizontalBarsDrawer"
    RoundedModuleDrawer = "RoundedModuleDrawer"
    SquareModuleDrawer = "SquareModuleDrawer"
    VerticalBarsDrawer = "VerticalBarsDrawer"


class QRRequest(BaseModel):
    data: str = Field(description="Text, URL or any other data for QR Code.")
    size: int | None = Field(
        None,
        description="The size parameter is an integer from 1 to 40 that controls the size of the QR Code "
        "(the smallest, version 1, is a 21x21 matrix). Don't set this parameter o determine this "
        "automatically.",
        ge=1,
        le=40,
    )
    quality: ErrorCorrect = Field(
        ErrorCorrect.medium,
        description="The quality parameter controls the error correction used for the QR Code. Can be low, medium, quartile or high",
    )
    box_size: int = Field(
        10,
        description='The box_size parameter controls how many pixels each “box" of the QR code is.',
    )
    border: int = Field(
        4,
        ge=0,
        le=10,
        description="The border parameter controls how many boxes thick the border should be (the default is 4, which "
        "is the minimum according to the specs).",
    )
    fill_color: Color = Field(
        Color("black"),
        description="fill_color can change the painting color of QR",
    )
    back_color: Color = Field(
        Color("white"),
        description="fill_color can change the painting color of QR",
    )
    drawer_type: DrawerType = Field(
        DrawerType.SquareModuleDrawer,
        description="The drawer_type parameter controls the shape of QR Code",
    )
