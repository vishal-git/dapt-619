# run from the repo root:  python src/percent_app.py
import gradio as gr
from metrics import percent_change


def describe_change(old, new):
    try:
        pct = percent_change(old, new)
    except ValueError:
        raise gr.Error("Old value cannot be zero.")
    direction = "up" if pct > 0 else "down" if pct < 0 else "flat"
    return f"{pct:.1f}% ({direction})"


demo = gr.Interface(
    fn=describe_change,
    inputs=[gr.Number(label="Old value"), gr.Number(label="New value")],
    outputs=gr.Textbox(label="Change"),
    title="Percent change calculator",
)

if __name__ == "__main__":
    demo.launch()  # use demo.launch(share=True) for a public link
