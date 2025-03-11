import streamlit as st
import qrcode
from PIL import Image
import io

st.title('Gerador de QrCode')
url = st.text_input('Cole sua URL aqui', placeholder='https://exemplo.com')

if url:

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_collor="black", back_collor="white")

    pill_img = img.get_image()

    st.image(pill_img, caption="QrCode gerado", use_container_width=True)

    buf = io.BytesIO()
    pill_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label= "Baixar QrCode",
        data= byte_im,
        file_name= "qrcode.png",
        mime= "image/png"
    )