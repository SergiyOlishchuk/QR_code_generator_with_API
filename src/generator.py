from io import BytesIO

import qrcode

from schemas import QRRequest


class QRCodeGenerator:
    def __init__(self, data: QRRequest):
        self.data = data

    def make_qr_code_image(self):
        qr = qrcode.main.QRCode(
            version=self.data.size,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=self.data.box_size,
            border=self.data.border,
        )

        qr.add_data(self.data.data)
        qr.make(fit=(self.data.size is None))

        return qr.make_image(
            fill_color=self.data.fill_color.as_hex(),
            back_color=self.data.back_color.as_hex(),
        )

    def run(self):
        img = self.make_qr_code_image()
        buf = BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        return buf
