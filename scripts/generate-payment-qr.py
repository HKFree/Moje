#!/usr/bin/env python3
"""Regenerate the static demo QR with: python3 -m pip install 'qrcode[pil]'"""
from pathlib import Path
from urllib.parse import quote

import qrcode

# Demo values must match public/index.html. Never use these for a real payment.
bank, prefix, account = '2010', '000000', '0123456789'
bban = bank + prefix + account
checksum = 98 - int(bban + '123500') % 97  # CZ00 moved behind BBAN; C=12, Z=35.
iban = f'CZ{checksum:02d}{bban}'
message = quote('Jan Novák · 12345', safe=' ')
payload = (
    f'SPD*1.0*ACC:{iban}*AM:290.00*CC:CZK'
    f'*DT:20261125*MSG:{message}*X-VS:12345'
)
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=4)
qr.add_data(payload)
qr.make(fit=True)
output = Path(__file__).resolve().parents[1] / 'public/assets/payment-qr.png'
qr.make_image(fill_color='black', back_color='white').save(output)
print(payload)
