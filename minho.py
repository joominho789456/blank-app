import streamlit as st
import qrcode
from PIL import Image
import io

# Streamlit 앱의 제목
st.title('URL to QR Code Generator')

# URL 입력을 위한 텍스트 박스
url = st.text_input('Enter URL:')

# URL이 입력되었을 때 QR 코드 생성
if url:
    # QR 코드 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    # 이미지 생성
    img = qr.make_image(fill='black', back_color='white')
    
    # 이미지 객체를 BytesIO로 변환
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()
    
    # 이미지 표시
    st.image(img_bytes, caption='Generated QR Code', use_column_width=True)
