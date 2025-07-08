from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load the model
model = tf.keras.models.load_model('trojan_detector_model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        img = Image.open(file)
        img = img.resize((224, 224))  # Resize to match model input
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        
        prediction = model.predict(img_array)
        result = "Trojan" if prediction[0][0] > 0.5 else "Not Trojan"
        return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run(debug=True)