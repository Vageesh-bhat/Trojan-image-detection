import os
import numpy as np
import cv2
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model

# Load model
MODEL_PATH = "malware_detection_resnet50.h5"
model = load_model(MODEL_PATH)

# Categories (must match your training order)
categories = ["benign", "malware"]

# Image size (same as training)
IMG_SIZE = 128

app = Flask(__name__)

# Preprocess uploaded image
def prepare_image(file_path):
    img = cv2.imread(file_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)  # shape: (1,128,128,3)
    return img

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check for uploaded file
        if "file" not in request.files:
            return "No file uploaded"
        file = request.files["file"]
        if file.filename == "":
            return "No file selected"
        
        # Save uploaded file into static folder
        filepath = os.path.join("static", file.filename)
        file.save(filepath)

        # Run prediction
        img = prepare_image(filepath)
        pred = model.predict(img)[0]
        label = categories[np.argmax(pred)]
        confidence = round(100 * np.max(pred), 2)

        # Convert label to True/False
        is_malware = True if label == "malware" else False

        return render_template("result.html", 
                               filename=file.filename,
                               label=is_malware,
                               confidence=confidence)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
