# run from the repo root:  python src/heart_app.py
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/heart.csv")
NUMERIC = ["Age", "RestingBP", "Cholesterol", "MaxHR", "Oldpeak"]


def plot_column(col):
    fig, ax = plt.subplots(figsize=(8, 4))
    for label, grp in df.groupby("HeartDisease"):
        ax.hist(grp[col], bins=30, alpha=0.6, label=f"HeartDisease={label}")
    ax.set_xlabel(col)
    ax.legend()
    return fig


with gr.Blocks(title="Heart data explorer") as demo:
    gr.Markdown("# Heart data explorer")
    with gr.Row():
        col = gr.Dropdown(NUMERIC, value="Age", label="Column")
        btn = gr.Button("Plot", variant="primary")
    plot = gr.Plot()
    btn.click(fn=plot_column, inputs=col, outputs=plot)

if __name__ == "__main__":
    demo.launch(share=True)  # share=True: also prints a public link (https://....gradio.live), valid for 1 week
