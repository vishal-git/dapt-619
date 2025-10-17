1. Make a new directory: `mkdir demo`
2. Go into that directory: `cd demo`
3. The directory is empty, since we just created it: `ls`
4. Let’s make sure there are no hidden files either: `ls -a`
5. Initialize a git repo: `git init` 
    1. Notice the message that's printed. Point out `.git`.
6. Check the content of the directory now: `ls` still shows nothing but `ls -a` shows the hidden `.git` file.
7. What’s in that `.git` file? `ls .git`
    1. The `objects` and `refs` directories are where all the git files will be stored. [What about the other folders? What’s in these folders?]
8. What’s going on right now? `git status`
    1. Nothing, since we haven't done anything yet.
    2. We will ignore the first line *On branch master* for now. 
9. Let’s create a new file: `echo "hello world" > hello.txt`
    1. Normally, this would contain your Python code, but we will keep it simple for now.
    2. Check the content of the file: `cat hello.txt`.
10. Wouldn’t it be nice to just take a *snapshot* of this state of your project?
    1. Well, git wants to give you some flexibility with what to include and what not to include in your snapshot. 
11. Check the status again: `git status` 
    1. We now see that there's an untracked file, hello.txt.
    2. Git noticed it, but is not doing anything with it right now. Let's change that. 
12. Let's add the file to git: `git add hello.txt` and then run `git status`.
    1. The file has been added. Now we are ready to take that snapshot.
13. Commit your changes: `git commit -m "my first commit"`. 
    1. Your commit message should be more informative than this, but for now we will keep things simple.
    2. Take a moment to point out how this add + commit system helps you ignore some files (e.g., a report) that you don't want to include in the git history.
    3. Sometimes, you may want to sequentially do add + commit to make it look like you first made some changes (to implement a feature) and then added some files (to implement another feature).
    4. Notice the *hash* printed in the output.
    5. We can (recursively) run an internal git command to see what's in that hash: `git cat-file -p <hash-id>`. 
14. Draw a circle on the whiteboard to represent the first node. 
15. Check the history: `git log --all --graph --decorate` 
    1. We only have one node in this graph, so it looks pretty simple. Let’s change that!
16. Add another line to our file: `echo "another line" >> hello.txt` 
    1. Check the content of the file: `cat hello.txt`.
17. Run `git commit` to remind them that since we haven’t added anything yet, it doesn’t do anything. 
18. Add the file: `git add hello.txt` 
19. Check status: `git status`
    1. Yes, we see that this change is ready to be committed. 
20. Commit these changes: `git commit -m "added another line"`
    1. Now we have another node in the graph.
21. Draw another circle on the whiteboard to represent the second node. 
22. Check log: `git log --all -- graph --decorate`
    1. Now we have this graph, in a vertical form.
    2. More recent commits are shown at the top.
23. Let’s talk about HEAD → master now. 
    1. Master is the main branch created in your repo. This is the core, main development branch.
    2. Unless you create another branch, everything is in the master.
    3. HEAD shows where you are currently looking right now. It's a reference. Currently, we are in the master branch at this particular node.
24. Let’s explore `git checkout`. 
    1. We can checkout to a previous commit in the history: `git checkout <previous-commit-prefix>`.
    2. This changes the state of my working directory to how it was at that commit.
    3. `cat hello.txt` would now show only the first line.
    4. Check `git log`, and see what changed? Our HEAD has now moved.
    5. We could go back to `git checkout *master*` now to go back to the latest code. Notice how we don't need to hash here, but we could.
    6. In summary, CHECKOUT moved the HEAD (and changes the content of the working directory).
25. Now let’s explore `git diff`.
    1. Modify the file: `echo "yet another line" >> hello.txt` 
    2. Check what has changed since the last commit: `git diff hello.txt`
    3. Remember, HEAD refers to the latest snapshot. We may have made changes to the file after the latest snapshot. `git diff` by default shows what changed since the snapshot where HEAD is pointing to.
26. Now, let’s explore how to create a new branch.
        ```
        git checkout -b feature-a
        git branch
        touch feature-a.py
        echo "print('feature a')" > feature-a.py
        git status
        git add .
        git commit -m "Added feature A"
        git log --all --graph --decorate
        git checkout master
        ls -- There's no feature-a.py
        git merge feature-a 
        ls -- feature-a.py is now present
        
28. Push
    ```
    git remote -- Shows nothing
    mkdir ../remote
    cd ../remote
    git init
    git config receive.denyCurrentBranch updateInstead
    cd ../demo
    git remote add origin ../remote
    git push origin master:master
    git log --all --graph --decorate --oneline` -- Head points to master, and origin/master
    ```
    Now if I make changes to the local branch, they won't be in the remote branch (yet).
    ```
    git clone ../remote demo2
    ```
    
    Now go back to the original demo, make changes and push to remote.
    ```
    git pull -- on demo2 to retrieve changes
    git fetch + git merge = git pull
    ``` 
    
30. `git clone`
    Creates a copy of a remote repository on your local machine. Use `git clone <repository-url> <directory-name>` to specify where to clone.
