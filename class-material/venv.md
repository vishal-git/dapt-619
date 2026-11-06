# Python Virtual Environment (venv)

1. Check which Python: `which python` or `where python`
2. Create  a new test script: `touch hello.py`
3. Add simple Python code to it: `echo 'from art import tprint; tprint("hello", font="random")' > hello.py`
4. Try to run it: `python hello.py`. Won’t run because we won’t have `art`.
5. Check `pip show art`. It would say `art` is not found.
6. Create a new virtual environment: `python -m venv venv`
7. Check the content of the new folder `ls -l venv`
    1. Basic packages in `bin/site_packages`.
8. Activate it: `venv\Scripts\activate`, or `source venv/bin/activate` on bash
9. Check `which python`. Now it refers to a local Python inside the virtual environment.
10. Install `art`: `pip install art`.
11. Try `pip show art` again, it will show the version number now.
12. Reinspect the content of the `venv` directory. New package `art` shows up in `site_packages`.
13. Run the script: `python hello.py`. It will run without any errors now. Run it multiple times, just for fun.
14. List what is installed in this environment, with exact versions: `pip freeze`. You will see one line, something like `art==6.5`.
    1. `pip freeze` prints every package in the active environment in the `package==version` format that `pip install` understands. That `==` is the point: it *pins* the exact version, so anyone who installs from this list gets the same `art` you have, not whatever is newest next month.
    2. Compare with `pip list`, which shows the same packages in a table meant for humans, not for `pip`.
15. Save that list to a file: `pip freeze > requirements.txt`. This is the conventional name, and most tools (and your teammates) will look for it.
16. Inspect it: `cat requirements.txt`. It is a plain text file, one package per line. Commit it to Git along with your code; do **not** commit the `venv/` folder itself (add `venv/` to `.gitignore`).
17. This is how someone else, or future you on a new laptop, rebuilds the exact same environment: create and activate a fresh venv (steps 6 and 8), then `pip install -r requirements.txt`. One command installs everything in the file at the pinned versions.
    1. Whenever you install or upgrade a package, run `pip freeze > requirements.txt` again so the file stays in sync with the environment.
18. Deactivate the environment: `deactivate`.
19. Check the content of site packages. Still intact.
20. But the script won’t run any more: `python hello.py`. Also check `pip show art` and `which python`.
21. ~~Remove the content of the virtual environment directory: `rm -rf venv/`~~. We will need this for the next exercise.
