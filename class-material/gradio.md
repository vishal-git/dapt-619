# Gradio apps

Two demos, two common uses of Gradio:

1. **Give a model an interface:** the digits app below (tutorial: you fill in the blanks).
2. **Explore your data:** the heart data explorer (see [Demo 2](#demo-2-heart-data-explorer-just-run-it); the code is complete, so you only run it).

## Demo 1: Draw a digit

Complete versions: `src/train_digits_model.py` and `src/digits_app.py`. Tutorial versions (fill in the blanks): `src/train_digits_model_tutorial.py` and `src/digits_app_tutorial.py`.

The goal: hand-draw a digit in a browser and let a model trained on scikit-learn's `load_digits()` guess it.

### Set up a project folder

1. In Git Bash, activate the course environment: `conda activate dapt619`. It already has scikit-learn and Gradio (see `setup.md`).
2. Make a project folder next to the `dapt-619` repo (not inside it) and move into it:

   ```bash
   cd ..              # from dapt-619/ up to your course folder
   mkdir digits
   cd digits
   mkdir src models
   ```

3. Copy the two tutorial files into `src/`, without the `_tutorial` in their names:

   ```bash
   cp ../dapt-619/src/train_digits_model_tutorial.py src/train_digits_model.py
   cp ../dapt-619/src/digits_app_tutorial.py src/digits_app.py
   ```

4. Check where you are and what's there: `pwd`, then `ls src`.
5. Open the `digits` folder in VS Code (**File → Open Folder**).

### Train the model

6. Fill in the four steps in `src/train_digits_model.py`: split the data, fit an SVC, print the test accuracy, and save the model to `models/digit_model.pkl`.
7. Run it from the `digits` folder: `python src/train_digits_model.py`. It prints `Test accuracy: 99.56%`.
8. Check that the model was saved: `ls models` shows `digit_model.pkl`.

### Build the app

9. Open `src/digits_app.py`. The function `predict_digit()` is already filled in. Its four pre-processing lines make the drawing *look like the training data*: they invert it (white digit on black), crop to the digit, pad it to a square, and shrink it to 8×8 pixels on a 0–16 scale, the same as `load_digits()`. Then it returns the model's guess.
10. Fill in the two steps. Step 1, below `predict_digit()`, creates the interface:

    ```python
    demo = gr.Interface(
        fn=predict_digit,
        inputs=gr.Sketchpad(type="pil", image_mode="L",
                            brush=gr.Brush(default_size=30, colors=["#000000"], color_mode="fixed")),
        outputs="text",
        title="Handwritten Digit Recognition",
    )
    ```

    Step 2, inside `if __name__ == "__main__":`, replaces `pass`. This "main guard" runs its block only when the file itself is run (`python src/digits_app.py`), not when another file imports it:

    ```python
        demo.launch()
    ```
11. Run the app from the `digits` folder: `python src/digits_app.py`. It prints a local URL (`http://127.0.0.1:7860`); open it in a browser.
    - Click the **brush icon** first; the canvas doesn't draw until a tool is selected.
    - Draw the digit large and centered, then press **Submit**.
    - Use the canvas's **trash-can icon** to wipe the drawing. The **Clear** button below doesn't reliably clear the canvas.
    - Expect some mistakes: the model was trained on tiny 8×8 scans, not mouse drawings. How would you make it more accurate?
12. Press `Ctrl + C` in the terminal to stop the app.

### Troubleshooting

| Symptom | Fix |
|---|---|
| Submit shows an error, and the terminal ends with `UnidentifiedImageError: cannot identify image file '...\layer_0.png'` | A Windows timing issue: Gradio read the drawing before it was fully saved. Wait a second and press **Submit** again. |
| That error keeps coming back | Switch to the Gradio version used last year, then restart the app: `pip install gradio==5.49.1`. The course code works the same on it. |
| **Clear** doesn't wipe the drawing | Use the canvas's **trash-can icon** instead. |

## Demo 2: Heart data explorer (just run it)

`src/heart_app.py` uses `gr.Blocks` instead of `gr.Interface`: a dropdown and a **Plot** button side by side (`gr.Row`), a plot below, and `btn.click(...)` wiring the button to `plot_column()`.

1. From the repo root (`dapt-619/`), with `dapt619` active: `python src/heart_app.py`. It reads `data/heart.csv`, so run it from the repo root, not from `src/`.
2. The terminal prints two URLs:
   - a local URL (`http://127.0.0.1:7860`), which only works on your computer;
   - a public link (`https://….gradio.live`), because the app calls `demo.launch(share=True)`. Anyone with the link can use the app for a week, but it still runs on your laptop: stop the app and the link stops working.
3. Pick a column, press **Plot**, and compare the histograms for `HeartDisease=0` and `HeartDisease=1`.
4. Press `Ctrl + C` to stop the app.

If no public link appears, the terminal says why. Gradio downloads a small tunnel program the first time, and antivirus software or a network firewall can block it. The local URL still works.

## Showing an error message

When the input doesn't make sense, stop the function with `gr.Error`. The app shows your message instead of crashing:

```python
def predict(monthly_charges):
    if monthly_charges <= 0:
        raise gr.Error("Monthly charges must be a positive number.")
    ...
```

The homework app needs this.

## Hosting on Hugging Face Spaces

Everything the Space needs is in `spaces/digits/`: `app.py`, `requirements.txt`, `digit_model.pkl`, and `README.md` (the YAML header sets `sdk: gradio`, `sdk_version`, `app_file`).

1. Go to `huggingface.co/new-space`. Name the Space, pick the **Gradio** SDK, choose the hardware, and keep it public.
   - Gradio Spaces on CPU hardware need a paid (PRO) plan. Free accounts that are **30+ days old with a verified email** can host up to 2 Spaces on **ZeroGPU**.
   - ZeroGPU refuses to start unless one function is decorated with `@spaces.GPU`, which is why `spaces/digits/app.py` has it. The decorator does nothing outside ZeroGPU.
2. Open the **Files** tab → **Add file** → **Upload files**. Drag in the four files from `spaces/digits/` and click **Commit**.
3. Watch the status go from "Building" to "Running". If the build fails, open **Logs**; it's usually a missing or mismatched package in `requirements.txt`.
4. Share `huggingface.co/spaces/<user>/<space>`. The app runs on Hugging Face, so it works on a phone even when your laptop is off.

Good to know:

- **Rebuild on every change:** each upload or push makes a fresh machine run `pip install -r requirements.txt` and then `python app.py`. This is the venv lesson again.
- **Pin the version:** `scikit-learn==1.9.1` matches the version that pickled the model.
- **Public code:** a public Space means public code. API keys go in **Settings → Secrets**.
- **Sleeping Spaces:** free Spaces sleep when idle; the first visit wakes them up.
- **Terminal alternatives:** `git clone` the Space repo and `git push`, or run `gradio deploy` inside the folder.

