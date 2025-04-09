from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from tensorflow.image import resize
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

MODEL = tf.keras.models.load_model("C:/Users/grzeye/Downloads/plant disease CNN-20240818T180156Z-001/plant disease CNN/plant_disease_classification_model.keras")
CLASS_NAMES = ["Healthy", "Powdery", "Rust"]
app = FastAPI()

# Ajouter le middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Remplace par ton origine React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image

@app.get("/ping")
async def ping():
    return "Hello, I am alive"

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Lire et préparer l'image
    image = read_file_as_image(await file.read())
    image = resize(image, (150, 150))  # Redimensionner à 150x150
    image = image / 255.0  # Normalisation des pixels
    img_batch = np.expand_dims(image, axis=0)  # Ajouter la dimension batch

    # Faire la prédiction
    prediction = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(prediction[0])]
    confidence = np.max(prediction[0])

    # Retourner la prédiction sous forme de JSON
    return {"class": predicted_class, "confidence": float(confidence)}

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)
