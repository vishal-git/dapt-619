from fastapi import FastAPI, File, UploadFile
import uvicorn

from utils import load_model, preprocess_image, predict_image, CIFAR10_CLASSES

load_model()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "CIFAR-10 Image Classification API", "classes": CIFAR10_CLASSES}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image_tensor = preprocess_image(image_bytes)
    predicted_class, confidence = predict_image(image_tensor)
    return {
        "prediction": predicted_class,
        "confidence": f"{confidence:.2f}%"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # test the API with the following command:
    # curl -X POST "http://localhost:8000/predict" -F "file=@./my_image.png"
