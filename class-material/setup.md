# Lecture 2 setup: conda environment (slide 3)

Start this in the first minutes of class: `pip install` downloads PyTorch (for `tabicl`), which takes a while. Do the warm-up questions while it runs.

## Steps (Anaconda Prompt on Windows, Terminal on Mac)

1. Go to the folder where you keep course work: `cd <your folder>`
2. Get the course repo.
   - First time: `git clone https://github.com/vishal-git/dapt-619.git`
   - Already have it: `cd dapt-619`, then `git pull`
3. Move into the repo: `cd dapt-619`
4. Create the environment with Python 3.12: `conda create -n dapt619 python=3.12 -y`
   - Last lecture we used `python -m venv`. A conda environment is the same idea (an isolated set of packages), and conda also lets us choose the Python version.
5. Activate it: `conda activate dapt619`. The prompt now starts with `(dapt619)`.
6. Check which Python will run:
   - `python --version` should print `Python 3.12.x`.
   - `where python` (Anaconda Prompt) or `which python` (Mac): the first line should be inside `...\envs\dapt619`.
7. Install everything for the course: `pip install -r requirements.txt`
   - **Ask first:** "What does this file do?" (It lists every package and version, so everyone gets the same setup.)
8. When it finishes, check that the key packages import:

   ```
   python -c "import pandas, polars, pytest, gradio, sklearn, tabicl; print('all good')"
   ```

## If something goes wrong

| Symptom | Fix |
|---|---|
| `conda: command not found` in Git Bash | Use Anaconda Prompt. Or run `conda init bash` once in Anaconda Prompt, then close and reopen Git Bash. |
| `git: command not found` in Anaconda Prompt | Do steps 1–3 in Git Bash, then come back to Anaconda Prompt for step 4. |
| `ERROR: No matching distribution found for numpy==2.5.4` (or similar) | The environment isn't active, or isn't Python 3.12. Run `conda activate dapt619` and check `python --version`. |
| The prompt shows `(base)` instead of `(dapt619)` | Run `conda activate dapt619` again. |
| The install is very slow | Expected: PyTorch alone is ~200 MB. Let it run during the warm-up. |

## Later in class

- New terminal window? Run `conda activate dapt619` again before any `python` or `pytest` command.
- Jupyter: start it **from the activated environment** with `jupyter lab`. The JupyterLab button in Anaconda Navigator opens the `base` environment, which doesn't have our packages.
- Everything runs from the repo root (`dapt-619/`), e.g. `pytest -v src/heart.py`, `python src/percent_app.py`.
