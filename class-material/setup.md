# Lecture 2 setup: conda environment

This lecture uses one conda environment, `dapt619`, with every package listed in the course repo's `requirements.txt`. The install includes PyTorch (used by `tabicl`), so it takes a few minutes.

## Steps (Anaconda Prompt on Windows, Terminal on Mac)

1. Go to the folder where you keep your course work: `cd <your folder>`
2. Get the course repo.
   - First time: `git clone https://github.com/vishal-git/dapt-619.git`
   - Already cloned: `cd dapt-619`, then `git pull`
3. Move into the repo: `cd dapt-619`
4. Create the environment with Python 3.12: `conda create -n dapt619 python=3.12 -y`
   - In lecture 1 we used `python -m venv`. A conda environment is the same idea (an isolated set of packages), and conda also lets us choose the Python version.
5. Activate it: `conda activate dapt619`. The prompt now starts with `(dapt619)`.
6. Check which Python will run:
   - `python --version` prints `Python 3.12.x`.
   - `where python` (Anaconda Prompt) or `which python` (Mac): the first line points inside `...\envs\dapt619`.
7. Install the course packages: `pip install -r requirements.txt`
   - `requirements.txt` lists every package and its version, so everyone gets the same setup.
8. Check that the key packages import:

   ```
   python -c "import pandas, polars, pytest, gradio, sklearn, tabicl; print('all good')"
   ```

## Using conda in Git Bash

Git Bash doesn't know about conda until conda sets it up. This takes one command, run once:

1. In **Anaconda Prompt**, find where conda is installed: `where conda`. Of the lines it prints, copy the one ending in `Scripts\conda.exe`, for example `C:\Users\ana\anaconda3\Scripts\conda.exe`.
2. Switch to **Git Bash**.
3. Convert that Windows path to a Unix-style path with `cygpath -u`. Keep the single quotes so the backslashes survive:

   ```bash
   cygpath -u 'C:\Users\ana\anaconda3\Scripts\conda.exe'
   # /c/Users/ana/anaconda3/Scripts/conda.exe
   ```

4. Run conda's setup for Git Bash, using the path from step 3:

   ```bash
   /c/Users/ana/anaconda3/Scripts/conda.exe init bash
   ```

5. Close Git Bash and open it again. `conda activate dapt619` now works in every new Git Bash window.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `conda: command not found` in Git Bash | Use Anaconda Prompt, or follow "Using conda in Git Bash" above. |
| `git: command not found` in Anaconda Prompt | Do steps 1–3 in Git Bash, then switch to Anaconda Prompt for step 4. |
| `ERROR: No matching distribution found for numpy==2.5.4` (or similar) | The environment isn't active, or isn't Python 3.12. Run `conda activate dapt619` and check `python --version`. |
| The prompt shows `(base)` instead of `(dapt619)` | Run `conda activate dapt619` again. |
| The install takes several minutes | Expected: PyTorch alone is about 200 MB. |

## Using the environment

- Every new terminal window starts outside the environment. Run `conda activate dapt619` before any `python` or `pytest` command.
- Start Jupyter from the activated environment with `jupyter lab`. The JupyterLab button in Anaconda Navigator opens the `base` environment, which doesn't have the course packages.
- Run commands from the repo root (`dapt-619/`), for example `pytest -v src/heart.py` or `python src/percent_app.py`.
