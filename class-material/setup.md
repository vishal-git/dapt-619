# Lecture 2 setup: conda environment

This lecture uses one conda environment, `dapt619`, with every package listed in the course repo's `requirements.txt`. The install includes PyTorch (used by `tabicl`), so it takes a few minutes.

Everything below runs in **Git Bash**, except step 1.

## Steps

1. In **Anaconda Prompt** (Mac: Terminal), find where conda is installed: `where conda` (Mac: `which conda`). Of the lines it prints, copy the one ending in `Scripts\conda.exe`, for example `C:\Users\ana\anaconda3\Scripts\conda.exe`.
2. Switch to **Git Bash** and go to the folder where you keep your course work: `cd <your folder>`
3. Get the course repo.
   - First time: `git clone https://github.com/vishal-git/dapt-619.git`
   - Already cloned: `cd dapt-619`, then `git pull`
4. Set up conda for Git Bash (once per computer; Mac users can skip this step).
   - Convert the Windows path from step 1 to a Unix-style path. Keep the single quotes so the backslashes survive:

     ```bash
     cygpath -u 'C:\Users\ana\anaconda3\Scripts\conda.exe'
     # /c/Users/ana/anaconda3/Scripts/conda.exe
     ```

   - Run conda's setup for Git Bash with that path:

     ```bash
     /c/Users/ana/anaconda3/Scripts/conda.exe init bash
     ```

   - Close Git Bash, open it again, and `cd` back to your course folder.
5. Move into the repo: `cd dapt-619`
6. Create the environment with Python 3.12: `conda create -n dapt619 python=3.12`
   - conda lists what it will install and asks `Proceed ([y]/n)?`. Type `y`. If it asks you to accept Anaconda's terms of service first, accept them.
   - In lecture 1 we used `python -m venv`. A conda environment is the same idea (an isolated set of packages), and conda also lets us choose the Python version.
7. See all your environments: `conda env list`. `dapt619` is now in the list; `*` marks the active one.
8. Activate it: `conda activate dapt619`. The prompt now shows `(dapt619)`.
9. Check which Python will run:
   - `python --version` prints `Python 3.12.x`.
   - `which python` points inside `.../envs/dapt619`.
10. Install the course packages: `pip install -r requirements.txt`
    - `requirements.txt` lists every package and its version, so everyone gets the same setup.
11. Spot-check the install. Each command prints the package's name, version, and location:

    ```bash
    pip show pandas
    pip show tabicl
    ```

## Troubleshooting

| Symptom | Fix |
|---|---|
| `conda: command not found` in Git Bash | Step 4 hasn't run yet, or Git Bash wasn't reopened afterward. |
| `ERROR: No matching distribution found for numpy==2.5.4` (or similar) | The environment isn't active, or isn't Python 3.12. Run `conda activate dapt619` and check `python --version`. |
| The prompt shows `(base)` instead of `(dapt619)` | Run `conda activate dapt619` again. |
| `pip show tabicl` prints `WARNING: Package(s) not found` | The install didn't finish, or ran outside the environment. Activate `dapt619` and rerun step 10. |
| The install takes several minutes | Expected: PyTorch alone is about 200 MB. |

## Using the environment

- Every new terminal window starts outside the environment. Run `conda activate dapt619` before any `python` or `pytest` command.
- Start Jupyter from the activated environment with `jupyter lab`. The JupyterLab button in Anaconda Navigator opens the `base` environment, which doesn't have the course packages.
- Run commands from the repo root (`dapt-619/`), for example `pytest -v src/heart.py` or `python src/percent_app.py`.

## Using Git Bash in VS Code

VS Code finds Git Bash automatically when Git for Windows is installed.

**Open a Git Bash terminal**

1. **Terminal → New Terminal** (or `` Ctrl+` ``).
2. In the terminal panel, click the **⌄** arrow next to the **+** and pick **Git Bash**.

**Make Git Bash the default terminal**

1. Either way works:
   - `Ctrl+Shift+P` → **Terminal: Select Default Profile** → **Git Bash**, or
   - in the terminal panel, click the **⌄** next to the **+** → **Select Default Profile** → **Git Bash**.
2. Close the open terminal and open a new one (`` Ctrl+` ``). Every new terminal now opens in Git Bash.

**If Git Bash isn't in the list**, add it to your settings: `Ctrl+Shift+P` → **Preferences: Open User Settings (JSON)**, then add these lines inside the outer `{ }`:

```json
"terminal.integrated.profiles.windows": {
  "Git Bash": {
    "path": "C:\\Program Files\\Git\\bin\\bash.exe",
    "args": ["--login", "-i"]
  }
},
"terminal.integrated.defaultProfile.windows": "Git Bash"
```

Save the file, close the open terminal, and open a new one. (If Git is installed somewhere else, use that folder's `bin\bash.exe` in `"path"`.)

**Two checks in the new terminal**

- `conda activate dapt619` works. If it prints `conda: command not found`, the Git Bash profile is missing `"--login"`; use the JSON above.
- VS Code's editor uses the same Python: `Ctrl+Shift+P` → **Python: Select Interpreter** → pick the one in `envs\dapt619`.
