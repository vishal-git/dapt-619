1. Check which Python: `which python` or `where python`
2. Create  a new test script: `touch hello.py`
3. Add simple Python code to it: `echo from art import tprint; tprint("hello", font="random") > test.py` 
4. Try to run it: `python hello.py`. Won’t run because we won’t have `art`.
5. Check `pip show art`. It would say `art` is not found. 
6. Create a new virtual environment: `python -m venv venv` 
7. Check the content of the new folder `ls -l venv`
    1. Basic packages in `bin/site_packages`.
8. Activate it: `venv\Scripts\activate`, or `source venv/bin/activate` on bash
10. Check `which python`. Now it refers to a local Python inside the virtual environment. 
11. Install `art`: `pip install art`.
12. Try `pip show art` again, it will show the version number now. 
13. Reinspect the content of the `venv` directory. New package `art` shows up in `site_packages`.
14. Run the script: `python hello.py`. It will run without any errors now. Run it multiple times, just for fun.
15. Deactivate the environment: `deactivate`.
16. Check the content of site packages. Still intact. 
17. But the script won’t run any more: `python test.py`. Also check `pip show art` and `which python`. 
18. ~~Remove the content of the virtual environment directory: `rm -rf venv/`~~. We will need this for the next exercise.
