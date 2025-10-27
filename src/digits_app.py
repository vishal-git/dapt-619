import gradio as gr
from PIL import Image
import joblib
import numpy as np

import numpy as np
from PIL import Image, ImageOps, ImageFilter
import joblib

clf = joblib.load("models/digit_model.pkl")

def _to_pil_from_paint(payload):
    if isinstance(payload, Image.Image):
        return payload
    if isinstance(payload, dict):
        for k in ("composite", "image", "background"):
            v = payload.get(k)
            if isinstance(v, Image.Image):
                return v
            if v is not None:
                arr = np.asarray(v)
                if arr.ndim in (2, 3):
                    return Image.fromarray(arr.astype("uint8"))
    return Image.fromarray(np.asarray(payload).astype("uint8"))

def preprocess_for_sklearn_digits(paint_payload):
    # 1) get grayscale PIL
    img = _to_pil_from_paint(paint_payload).convert("L")

    # 2) invert to white ink on black (sklearn digits look like this)
    img = ImageOps.invert(img)

    # 3) crop to bounding box of the digit
    arr = np.array(img)
    mask = arr > 10  # low threshold to catch faint strokes
    if mask.any():
        ys, xs = np.where(mask)
        x0, x1, y0, y1 = xs.min(), xs.max(), ys.min(), ys.max()
        img = img.crop((x0, y0, x1 + 1, y1 + 1))

    # 4) pad to square & center
    w, h = img.size
    m = max(w, h)
    canvas = Image.new("L", (m, m), color=0)
    canvas.paste(img, ((m - w) // 2, (m - h) // 2))

    # 5) soften a bit to mimic dataset
    canvas = canvas.filter(ImageFilter.GaussianBlur(radius=1))

    # 6) resize to 8x8 (digits dataset size)
    small = canvas.resize((8, 8), Image.LANCZOS)

    # 7) scale to 0..16 like load_digits()
    arr8 = np.asarray(small).astype(np.float32)
    arr8 = (arr8 / 255.0) * 16.0

    return arr8.reshape(1, -1)

def predict_digit(paint_payload):
    X = preprocess_for_sklearn_digits(paint_payload)
    return int(clf.predict(X)[0])

def white_canvas(w=400, h=400):
    return Image.new("L", (w, h), color=255)  # 255 = white in grayscale

with gr.Blocks() as demo:
    gr.Markdown("# Handwritten Digit Recognition")
    gr.Markdown("Draw a digit (0–9) below and click Submit.")

    with gr.Row():
        img_input = gr.Paint(
            label="Draw your digit here",
            type="pil",
            image_mode="L",
            height=400,
            value=white_canvas(),            # initial white background
            brush={"color": "black", "size": 15}
        )
        output = gr.Textbox(label="Prediction")

    submit_btn = gr.Button("Submit")
    clear_btn = gr.Button("Clear")

    def process_image(image):
        if image is None:
            return "Please draw a digit first!"
        return predict_digit(image)

    def clear_input():
        return white_canvas()

    submit_btn.click(process_image, inputs=img_input, outputs=output)
    clear_btn.click(clear_input, outputs=img_input)

if __name__ == "__main__":
    demo.launch()
