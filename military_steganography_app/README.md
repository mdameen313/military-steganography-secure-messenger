# Military Steganography Secure Messenger

A Streamlit web application that allows secure communication by hiding encrypted text messages inside image pixels. Ideal for sensitive or classified messaging scenarios like military communication.

---

## 🚀 Features

- 🔐 AES Encryption using strong auto-generated keys.
- 🖼️ Embeds encrypted text inside an image using LSB (Least Significant Bit) technique.
- 📤 Sender shares the stego image + secure key.
- 📥 Receiver uploads stego image + key to reveal original message.

---

## 📦 Requirements

Install dependencies using pip:

```bash
pip install streamlit pillow cryptography
```

---

## 🧠 How it Works

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

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## 💻 Upload to GitHub

1. Create a new repository on [GitHub](https://github.com/new)
2. Clone it:
    ```bash
    git clone https://github.com/your-username/military-steganography-app.git
    cd military-steganography-app
    ```
3. Add project files:
    ```bash
    cp path/to/app.py .
    echo "streamlit\npillow\ncryptography" > requirements.txt
    ```
4. Commit and push:
    ```bash
    git add .
    git commit -m "Initial commit"
    git push origin main
    ```

---

## 🌐 Deploy Online (Streamlit Cloud)

1. Go to [Streamlit Cloud](https://streamlit.io/cloud)
2. Click **New App**
3. Select your GitHub repo
4. Set `app.py` as the main file
5. Deploy and share the app link ✅

---

## 📜 License
MIT License

---

## 🤝 Credits
Developed by [Your Name] for Cybersecurity Project, 2025.
