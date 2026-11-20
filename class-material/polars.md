# Polars notebooks

Two notebooks in `notebooks/`, both complete. Run them cell by cell and read the code and output as you go.

| Notebook | What it covers |
|---|---|
| `01_polars_wrangle.ipynb` | Six core Polars moves (read, `select` / `with_columns`, `group_by`, `filter`, chaining, `join`) on the Olist orders data, each next to its pandas equivalent |
| `02_lazy_evaluation.ipynb` | Eager (`read_csv`) vs lazy (`scan_csv`): reading a query plan with `.explain()`, running it with `.collect()`, and timing both |

Both read their data from `data/` with paths like `../data/olist_orders.csv.gz`, so keep them in `notebooks/` inside the repo.

## Option A: JupyterLab from Git Bash

1. Open Git Bash and go to the repo:

   ```bash
   cd ~/path/to/dapt-619      # wherever you cloned it
   git pull                   # get the latest notebooks
   ```

2. Activate the course environment. It has Polars, matplotlib, and JupyterLab (see `setup.md`):

   ```bash
   conda activate dapt619
   ```

   The prompt should now start with `(dapt619)`.

3. Start JupyterLab **from the repo root** (`dapt-619/`):

   ```bash
   jupyter lab
   ```

   A browser tab opens. If it doesn't, copy the `http://localhost:8888/lab?token=…` link that the terminal prints and paste it into a browser. JupyterLab only shows the folder you started it in and the folders below it, which is why you start it from the repo root.

4. In the file browser on the left, open `notebooks/` → `01_polars_wrangle.ipynb`.
5. Run cells one at a time with `Shift + Enter`, or run everything with **Run → Run All Cells**.
6. When you're done, use **File → Shut Down** in JupyterLab, or press `Ctrl + C` in Git Bash and answer `y`. Leave the Git Bash window open while you work: closing it stops JupyterLab.

> Don't use the **JupyterLab** button in Anaconda Navigator unless you switch Navigator to the `dapt619` environment first. By default it opens the `base` environment, which doesn't have Polars.

## Option B: VS Code

1. **File → Open Folder** → `dapt-619`.
2. Open `notebooks/01_polars_wrangle.ipynb`. If VS Code offers to install the **Jupyter** and **Python** extensions, accept.
3. Click **Select Kernel** (top right) → **Python Environments** → `dapt619`.
4. Run cells with `Shift + Enter`, or click **Run All** at the top.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: No module named 'polars'` | The notebook is using the wrong Python. In JupyterLab: stop it, run `conda activate dapt619`, start `jupyter lab` again. In VS Code: **Select Kernel** → `dapt619`. |
| `bash: jupyter: command not found` | The environment isn't active (`conda activate dapt619`), or the packages aren't installed yet (`pip install -r requirements.txt` from the repo root). |
| `conda: command not found` in Git Bash | Conda hasn't been set up for Git Bash yet: follow step 4 in `setup.md`, then close and reopen Git Bash. |
| `FileNotFoundError: ../data/olist_orders.csv.gz` | The notebook was moved or copied out of `notebooks/`. Open the one inside the repo. |
| JupyterLab doesn't show the `notebooks/` folder | It was started from a different folder. Stop it, `cd` to `dapt-619/`, and run `jupyter lab` again. |
| Port 8888 already in use / a second link like `localhost:8889` | Another JupyterLab is still running. Use that one, or shut it down first. |
