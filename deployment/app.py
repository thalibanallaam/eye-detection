import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load model
model_path = "model_new.keras" 
model = load_model(model_path)

# Prediction Function
def predict_eye_state(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    img = cv2.resize(img, (64, 64))  # Resize the image
    img = np.expand_dims(img, axis=0)  # Batch dimension
    img = np.expand_dims(img, axis=-1)  # Channel dimension
    img = img / .255  # Normalize pixel values

    prediction = model.predict(img)

    if prediction > 0.5:
        return 'Open Eyes'
    else:
        return 'Closed Eyes'

# Streamlit app

# Title
st.title("Eye Detection App")

# File Input
file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if file is not None:
    # Load uploaded file
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), 1)

    # Image preview
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Make prediction
    predicted_state = predict_eye_state(image)

    # Display the prediction
    st.write(f"**Predicted eye state:** {predicted_state}")