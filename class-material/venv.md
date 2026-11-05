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
14. Deactivate the environment: `deactivate`.
15. Check the content of site packages. Still intact.
16. But the script won’t run any more: `python hello.py`. Also check `pip show art` and `which python`.
17. ~~Remove the content of the virtual environment directory: `rm -rf venv/`~~. We will need this for the next exercise.
