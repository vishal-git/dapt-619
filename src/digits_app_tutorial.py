import gradio as gr
import joblib
import numpy as np
from PIL import ImageOps

model = joblib.load("models/digit_model.pkl")


def predict_digit(drawing):
    if drawing is None or drawing["composite"] is None:
        return "Please draw a digit first!"
    # make the drawing look like the training data (8x8, white digit on black, 0-16 scale)
    img = ImageOps.invert(drawing["composite"])          # white digit on black, like the training images
    img = img.crop(img.getbbox())                        # zoom in on the digit
    img = ImageOps.pad(img, (max(img.size),) * 2)        # make it square
    pixels = np.array(img.resize((8, 8))) / 255 * 16     # 8x8 on a 0-16 scale, like load_digits()
    return int(model.predict(pixels.reshape(1, -1))[0])  # the model's guess for this one drawing


# step 1: create a gr.Interface with
#         fn=predict_digit,
#         inputs=gr.Sketchpad(type="pil", image_mode="L",
#                             brush=gr.Brush(default_size=30, colors=["#000000"], color_mode="fixed")),
#         outputs="text", and a title
# --

if __name__ == "__main__":
    # step 2: launch the app
    # --
    pass  # replace this line with your code
