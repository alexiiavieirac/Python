# Criando QR Code:

import qrcode
from qrcode.image.styledpil import StyledPilImage

# QR Code simples:
imagem = qrcode.make("https://www.youtube.com/@HashtagProgramacao")
imagem.save("qrcode.png")

# QR Code com imagem:
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("https://www.youtube.com/@HashtagProgramacao")

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embeded_image_path="logo.png"
)

imagem.save("qrcode_logo.png")

# Criando diversos QR Code ao mesmo tempo:
redes_sociais = {
    "Facebook": "https://www.facebook.com/@HashtagProgramacao",
    "Instagram": "https://www.instagram.com/hashtagprogramacao",
    "YouTube": "https://www.youtube.com/@HashtagProgramacao",
    "TikTok": "https://www.tiktok.com/@hashtagprogramacao"
}

# É uma tupla, onde está dentro de uma lista, tendo 2 valores, a rede social e a url:
print(redes_sociais.items())

for rede_social, url in redes_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path="logo.png"
    )

    imagem.save(f"sociais_{rede_social}.png")
