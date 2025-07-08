# 🛡️ Trojan Image Detection API

A Flask-based web API that uses a trained deep learning model to detect trojan-injected or maliciously tampered images. This backend accepts image uploads and returns predictions based on the model.

---

## 🚀 Features

- Detects trojan content in uploaded images
- Accepts POST requests with image files
- Returns JSON response with prediction (`Trojan` or `Not Trojan`)
- Easily integrable with frontend or other tools

---

## 📁 Project Structure
```
Trojan-Image-Detection/
├── static/
│ └── css/
│ └── style.css # Custom styles for the web UI
├── template/
│ └── index.html # HTML frontend for uploading images
├── app.py # Flask server handling UI and API
├── trojan_detection.ipynb # Model training/testing notebook
├── requirement.txt # Python dependencies
└── README.md # Project documentation
```

---

## ⚙️ Requirements

- Python 3.7 or higher
- TensorFlow
- Flask
- Pillow
- NumPy

## Create virtual environment
```bash
python -m venv .venv
```
## Activate virtual environment
```bash
.venv\Scripts\activate
```
## 🔧 Install Dependencies

```bash
pip install -r requirements.txt
```
