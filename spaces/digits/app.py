import gradio as gr
import joblib
import numpy as np
import spaces
from PIL import ImageOps

model = joblib.load("digit_model.pkl")


@spaces.GPU  # required by Hugging Face's free ZeroGPU hardware; does nothing anywhere else
def predict_digit(drawing):
    if drawing is None or drawing["composite"] is None:
        return "Please draw a digit first!"
    img = ImageOps.invert(drawing["composite"])          # white digit on black, like the training images
    img = img.crop(img.getbbox())                        # zoom in on the digit
    img = ImageOps.pad(img, (max(img.size),) * 2)        # make it square
    pixels = np.array(img.resize((8, 8))) / 255 * 16     # 8x8 on a 0-16 scale, like load_digits()
    return int(model.predict(pixels.reshape(1, -1))[0])


demo = gr.Interface(
    fn=predict_digit,
    inputs=gr.Sketchpad(type="pil", image_mode="L",
                        brush=gr.Brush(default_size=30, colors=["#000000"], color_mode="fixed")),
    outputs="text",
    title="Handwritten Digit Recognition",
    description="Click the brush icon, draw a digit (0-9), and press Submit.",
)

if __name__ == "__main__":
    demo.launch()
