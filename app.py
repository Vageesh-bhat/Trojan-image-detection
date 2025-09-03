from flask import Flask, request, render_template
import tensorflow as tf
from PIL import Image
import numpy as np
import os

app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model('trojan_detector.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('result.html', result="No file uploaded", confidence=0, image_path=None)
    
    file = request.files['file']
    if file.filename == '':
        return render_template('result.html', result="No file selected", confidence=0, image_path=None)
    
    upload_folder = os.path.join('static', 'uploads')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    file_path = os.path.join(upload_folder, file.filename)
    file.save(file_path)
    
    # Preprocess image
    img = Image.open(file).convert('RGB')
    img = img.resize((128, 128))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Make prediction
    pred = model.predict(img_array)
    print(f"perd: {pred}")
    confidence = float(pred[0][0])
    print(f"conf: {confidence}")
    result = "Trojan" if confidence > 0.5 else "Not Trojan"
    image_path = file.filename 
    
    # Render result.html with prediction
    return render_template('result.html', result=result, confidence=confidence, image_path=image_path)
