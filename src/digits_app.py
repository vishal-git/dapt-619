import gradio as gr
from digits_utils import predict_digit, white_canvas

def process_image(image):
    if image is None:
        return "Please draw a digit first!"
    return predict_digit(image)

demo = gr.Interface(
    fn=process_image,
    inputs=gr.Paint(
        type="pil",
        image_mode="L",
        height=400,
        value=white_canvas(),
        brush={"color": "black", "size": 15}
    ),
    outputs="text",
    title="Handwritten Digit Recognition",
    description="Draw a digit (0–9) below and see the prediction!"
)

if __name__ == "__main__":
    demo.launch()
