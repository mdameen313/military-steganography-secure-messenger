# Military Steganography Secure Messenger

A Streamlit web application that allows secure communication by hiding encrypted text messages inside image pixels. Ideal for sensitive or classified messaging scenarios like military communication.

---

## Features

-  AES Encryption using strong auto-generated keys.
-  Embeds encrypted text inside an image using LSB (Least Significant Bit) technique.
-  Sender shares the stego image + secure key.
-  Receiver uploads stego image + key to reveal original message.

---

##  Requirements

Install dependencies using pip:

```bash
pip install streamlit pillow cryptography
```

---

##  How it Works

1. **Send Message**
    - Upload any image.
    - Enter the secret message.
    - System encrypts the message and hides it in the image.
    - Download the stego image and share it with the key.

2. **Receive Message**
    - Upload the stego image.
    - Enter the key shared by sender.
    - System extracts and decrypts the message.

---

## ▶ Run Locally

```bash
streamlit run app.py
```

---


## 🤝 Credits
Developed by Mohammed Ameen for Cybersecurity Project, 2025.
