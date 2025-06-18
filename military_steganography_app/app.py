import streamlit as st
from PIL import Image
import io
import base64
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

# Key derivation

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# Encrypt message

def encrypt_message(message: str, password: str) -> bytes:
    salt = os.urandom(16)
    key = derive_key(password, salt)
    fernet = Fernet(key)
    encrypted = fernet.encrypt(message.encode())
    return salt + encrypted

# Decrypt message

def decrypt_message(encrypted_data: bytes, password: str) -> str:
    salt = encrypted_data[:16]
    encrypted = encrypted_data[16:]
    key = derive_key(password, salt)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted).decode()

# Embed into image

def embed_data_into_image(img: Image.Image, data_bytes: bytes) -> Image.Image:
    binary = ''.join(format(byte, '08b') for byte in data_bytes)
    binary += '1111111111111110'  # Delimiter

    if img.mode != 'RGB':
        img = img.convert('RGB')

    pixels = list(img.getdata())
    new_pixels = []
    binary_index = 0

    for pixel in pixels:
        r, g, b = pixel
        if binary_index < len(binary):
            r = (r & ~1) | int(binary[binary_index])
            binary_index += 1
        if binary_index < len(binary):
            g = (g & ~1) | int(binary[binary_index])
            binary_index += 1
        if binary_index < len(binary):
            b = (b & ~1) | int(binary[binary_index])
            binary_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    return img

# Extract from image

def extract_data_from_image(img: Image.Image) -> bytes:
    pixels = list(img.getdata())
    binary = ''

    for pixel in pixels:
        for color in pixel:
            binary += str(color & 1)

    all_bytes = [binary[i:i+8] for i in range(0, len(binary), 8)]
    data_bytes = bytearray()

    for byte in all_bytes:
        if byte == '11111110':
            break
        data_bytes.append(int(byte, 2))

    return bytes(data_bytes)

# Streamlit App
st.title("🔐 Military Steganography Secure Messenger")

mode = st.radio("Choose an action:", ["Send Message", "Receive Message"])

if mode == "Send Message":
    uploaded_image = st.file_uploader("Upload an image to hide the message in", type=["png", "jpg", "jpeg"])
    message = st.text_area("Enter the secret message to hide")

    if uploaded_image and message:
        image = Image.open(uploaded_image)
        password = Fernet.generate_key().decode()
        encrypted_data = encrypt_message(message, password)
        output_image = embed_data_into_image(image, encrypted_data)

        st.success("Message has been embedded into the image.")
        st.image(output_image, caption="Stego Image", use_container_width=True)

        buf = io.BytesIO()
        output_image.save(buf, format='PNG')
        byte_im = buf.getvalue()

        b64 = base64.b64encode(byte_im).decode()
        href = f'<a href="data:image/png;base64,{b64}" download="stego_image.png">📥 Download Stego Image</a>'
        st.markdown(href, unsafe_allow_html=True)

        st.text_input("🔑 Share this encryption key securely with the recipient:", value=password)

elif mode == "Receive Message":
    uploaded_stego = st.file_uploader("Upload the image with the hidden message", type=["png", "jpg", "jpeg"])
    password = st.text_input("Enter the key that was shared with you")

    if uploaded_stego and password:
        image = Image.open(uploaded_stego)
        try:
            encrypted_bytes = extract_data_from_image(image)
            decrypted_message = decrypt_message(encrypted_bytes, password)
            st.success("✅ Decrypted Message:")
            st.code(decrypted_message)
        except Exception as e:
            st.error("❌ Failed to decrypt message. Please check the image and key.")
