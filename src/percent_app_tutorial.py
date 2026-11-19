# run from the repo root:  python src/percent_app_tutorial.py
import gradio as gr
from metrics import percent_change


def describe_change(old, new):
    # step 1: call percent_change; if it raises a ValueError, raise gr.Error("Old value cannot be zero.")
    # --

    # step 2: set direction to "up", "down", or "flat"
    # --

    # step 3: return a string such as "25.0% (up)"
    # --
    pass  # replace this line with your code


# step 4: create a gr.Interface with fn=describe_change,
#         two gr.Number inputs (Old value, New value) and a gr.Textbox output
# --

if __name__ == "__main__":
    # step 5: launch the app (try share=True for a public link)
    # --
    pass  # replace this line with your code
