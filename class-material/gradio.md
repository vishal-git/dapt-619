# Gradio app (digits)

1. Clone the course repo: `git clone https://github.com/vishal-git/dapt-619.git`
2. Check the content of the cloned repo. `ls dapt-619`
3. Create a new directory: `mkdir digits`
4. Make a subdirectory: `mkdir digits/src`
5. Move into the new project folder: `cd digits`
6. Check where you are and what's there: `pwd`, then `ls`.
7. Create an empty file `touch src/train_digits_model.py`.
8. Type in all content from `train_digits_model.py` into this file.
9. Now we are going to run this code. We already created the `dapt619` conda environment at the start of class (slide 3), and it has everything we need: scikit-learn, Gradio, and the rest of `requirements.txt`.
10. Activate it: `conda activate dapt619`. You will notice “(dapt619)” before your prompt.
    - In Git Bash, `conda activate` only works after running `conda init bash` once in Anaconda Prompt and reopening Git Bash.
11. Confirm which Python will run: `where python` (Anaconda Prompt) or `which python` (Git Bash). The first result should be inside `…\envs\dapt619`.
12. (VS Code might ask which interpreter to use; pick the one in `envs\dapt619`.)
13. Nothing to install: `pip install -r requirements.txt` already did it. (Without that file, it would be `pip install scikit-learn gradio`.)
14. Make a new folder to store the trained model: `mkdir models`.
15. Run the script from command line: `python src/train_digits_model.py`.
16. Check is a new model is saved in the `models` folder: `ls models`.
17. Now, let’s build a Gradio app. Our goal is to hand-draw a digit and use the model to determine the digit.
18. Create a new file to write code for this app: `touch src/digits_app.py`.
19. Open it in VS Code and write the code from `dapt-619/src/digits_app.py` (or start from `dapt-619/src/digits_app_tutorial.py`, which fills in the pre-processing so we can focus on Gradio). Walk through the four pre-processing lines: the drawing has to *look like the training data*, so we invert it (white digit on black), crop to the digit, pad it to a square, and shrink it to 8×8 pixels on a 0–16 scale, the same as `load_digits()`.
20. Gradio is already installed in `dapt619` (it's in `requirements.txt`).
21. Run the app: `python src/digits_app.py`. This will print a local URL. Click on it to open it in a browser and interact with the app.
    - Click the **brush icon** first; the canvas won't draw until a tool is selected.
    - Draw the digit large and centered, then press **Submit**.
    - Use the canvas's **trash-can icon** to wipe the drawing. The Interface's **Clear** button does not reliably clear the canvas.
    - Expect some mistakes: the model was trained on tiny 8×8 scans, not mouse drawings. Good moment to ask: "How would you make it more accurate?"
22. Press Ctrl + C to exit and get back to the command line.
23. Deactivate the virtual environment: `deactivate`.

## Hosting on Hugging Face Spaces (instructor demo)

Everything the Space needs is in `spaces/digits/`: `app.py`, `requirements.txt`, `digit_model.pkl`, and `README.md` (the YAML header sets `sdk: gradio`, `sdk_version`, `app_file`).

24. Go to `huggingface.co/new-space`. Name the Space, pick the **Gradio** SDK, choose the hardware, and keep it public.
   - Gradio Spaces on CPU hardware need a paid (PRO) plan. Free accounts that are **30+ days old with a verified email** can host up to 2 Spaces on **ZeroGPU**.
   - ZeroGPU refuses to start unless one function is decorated with `@spaces.GPU`, which is why `spaces/digits/app.py` has it. The decorator does nothing outside ZeroGPU.
25. Open the **Files** tab → **Add file** → **Upload files**. Drag in the four files from `spaces/digits/` and click **Commit**.
26. Watch the status go from "Building" to "Running". If the build fails, open **Logs**; it's usually a missing or mismatched package in `requirements.txt`.
27. Share `huggingface.co/spaces/<user>/<space>`. Open it on a phone to show it runs without your laptop.

Talking points:

- **Rebuild on every change:** each upload or push makes a fresh machine run `pip install -r requirements.txt` and then `python app.py`. This is the venv lesson again.
- **Pin the version:** `scikit-learn==1.9.1` matches the version that pickled the model.
- **Public code:** a public Space means public code. API keys go in **Settings → Secrets**.
- **Sleeping Spaces:** free Spaces sleep when idle; the first visit wakes them up.
- **Terminal alternatives:** `git clone` the Space repo and `git push`, or run `gradio deploy` inside the folder.

