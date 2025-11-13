1. Clone the course repo: `git clone https://github.com/vishal-git/dapt-619.git` 
2. Check the content of the cloned repo. `ls dapt-619`
3. Create a new directory: `mkdir digits`
4. Make a subdirectory: `mkdir digits/src`
5. Copy some utility functions from the repo into `digits/src`: `cp dapt-619/src/digits_utils.py digits/src/` 
6. Check the content of the `src` folder using `ls`.  
7. Create an empty file `touch src/train_digits_model.py`.
8. Type in all content from `train_digits_model.py` into this file. 
9. Now we are going to run this code. But first, let’s create a venv!
10. Even before we create a new environment, we need to set a proper path for Python.
11. Go to Anaconda command prompt and run the following to find the location of the Python executable file: `where python`. E.g. “C:\Users\visha\anaconda3\python.exe”. We need to copy this, remove python.exe from it, and replace all backward slashes with forward slashes. 
12. Run the following: `export PATH="/c/Users/visha/anaconda/:$PATH"`
13. Now create a new Python venv: `python -m venv .venv` (VSCode might ask to use this environment; click yes.)
14. Activate it: `source .venv/Scripts/activate`. You will notice “(.venv)” before your prompt. 
15. Install `sklearn`: `pip install scikit-learn`.
16. Make a new folder to store the trained model: `mkdir models`.
17. Run the script from command line: `python src/train_digits_model.py`.
18. Check is a new model is saved in the `models` folder: `ls models`.
19. Now, let’s build a Gradio app. Our goal is to hand-draw a digit and use the model to determine the digit. 
20. Create a new file to write code for this app: `touch src/digits_app.py`.
21. Open it in VSCode and write all the code. 
22. Before we run it, we need to install Gradio: `pip install gradio`.
23. Run the app: `python src/digits_app.py`. This will print a local URL. Click on it to open it in a browser and interact with the app. 
24. Press Ctrl + C to exit and get back to the command line.
25. Deactivate the virtual environment: `deactivate`.
