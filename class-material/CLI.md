1. `whoami`
    Prints the current user's login name. Useful to confirm which account your shell session is using.
2. `pwd` (Where am I?)
    Shows the full path of the present working directory. Helps you verify your current location in the filesystem.
3. `date`
    Displays the system date and time. Handy for timestamps in logs or verifying time settings.
4. `echo`
    Prints text or variable values to the terminal. Often used to test shell expansion or write strings into files.
5. `ls`
    Lists files and directories in the current directory. Add flags to control visibility and sorting.
6. `ls -a`
    Lists all entries, including hidden files (those beginning with a dot). Useful to see config files and metadata.
7. `ls -lrt`
    Lists in long format, reverse order, sorted by modification time. Quickly surfaces the most recently changed files at the bottom.
8. `mkdir test` 
    Creates a new directory named `test` in the current location. Add `-p` to create parent directories as needed.
9. Navigation
    Commands to change your current directory and move around the filesystem efficiently.
    1. `cd test`
        Change directory into `test` (a folder in your current directory). Fails if `test` does not exist.
    2. `cd /` 
        Jump to the filesystem root directory. Useful starting point to navigate to absolute paths.
    3. `cd -`
        Toggle back to the previous working directory. Acts like a quick back button for directories.
    4. `cd ..`
        Move up one directory level (to the parent). Chain as `cd ../..` to go up multiple levels.
    5. `cd ~`
        Go to your home directory. Equivalent to `cd` with no arguments.
10. Tab completion
    Press Tab to auto-complete commands and paths. Double-press Tab to see available completions when ambiguous.
11. `touch foo.txt`[^1]
[^1]: Smokey Stover, Bill Holman: The Foo Fighter, FUBAR: Fouled up beyond all recognition?

    Creates an empty file if it doesn't exist, or updates the file's modified timestamp. Often used to quickly create placeholder files.
12. Use `>` and `>>` to add content to the file.
    `>` overwrites a file with new content; `>>` appends to the end. Example: `echo hello > foo.txt`.
13. `cat`
    Concatenates and prints file contents to the terminal. Combine with pipes to preview or process text.
14. `touch foo.png` then `ls *.txt`
    Creates a PNG file and lists files matching the `*.txt` glob. Globs help filter by patterns (e.g., extension).
15. `cp foo.txt bar.txt` 
    Copies `foo.txt` to a new file named `bar.txt`. Use `-r` to copy directories recursively.
16. Let’s move it to one directory higher up: `cp foo.txt ../bar.txt` and then `rm bar.txt`  
    Demonstrates copying a file up one level and then removing the copy. Removing deletes it permanently (use caution).
17. Instead, we can move it directly by using this command: `mv`
    `mv source target` renames or relocates files/directories. Example: `mv foo.txt ../bar.txt` moves and renames in one step.
18. `curl -L https://raw.githubusercontent.com/vishal-git/dapt-631/refs/heads/main/data/geyser.tsv -o geyser.tsv` 
    Downloads the TSV to `geyser.tsv`. `-L` follows redirects; `-o` sets the output filename.
19. `head`
    Prints the first lines of a file (default 10). Use `-n N` to control the number of lines.
20. `tail`
    Prints the last lines of a file (default 10). Use `-f` to follow a file as it grows (live logs).
21. `less`
    Interactive pager to view files one screen at a time. Navigate with arrows, `q` to quit, `/pattern` to search.
22. `wc -l`
    Counts lines in input or a file. Combine with pipes (e.g., `grep pattern file | wc -l`) to count matches.
23. `grep`
    Searches input or files for lines matching a pattern. Supports regex and flags like `-i` (case-insensitive) and `-r` (recursive).
    1. Specific value, like 85.
        Example: `grep 85 geyser.tsv` finds lines containing 85. Quote patterns with spaces or special characters.
    2. `head -n 1 | grep wait` to find specific column name.
        Pipes the header line to `grep` to check if `wait` appears among column names.
24. `rm`
    Removes files. Irreversible—use carefully. Add `-i` for interactive prompts or `-r` to remove directories recursively.
25. `rmdir`
    Removes empty directories only. Use `rm -r directory` to delete directories that contain files.
26. Arrow keys
    Use Up/Down to cycle command history; Left/Right to move the cursor within the current command for editing.
27. Ctrl + C
    Sends an interrupt signal to stop the current foreground process. Use when a command hangs or runs too long.
28. `clear` (Ctrl + L)
    Clears the terminal screen. Ctrl+L is a shortcut that leaves scrollback intact.
29. `exit`
    Closes the current shell session. In scripts, you can pass a status code (0 for success, non-zero for errors).
30. `man`
    Opens the manual page for a command (e.g., `man ls`). Use arrow keys to scroll and `q` to quit.
31. `--help` / `-h`
    Most commands print a brief help summary with `--help` or `-h` (e.g., `ls --help`). Great for quick option lookups.
32. `history`
    Shows your recent commands with line numbers. Combine with `!N` to re-run entry N.
33. `!!`
    Re-runs the previous command. Often used with `sudo` as `sudo !!` to retry with elevated permissions.
34. `which`
    Prints the path to the executable that will run for a command (e.g., `which python`). Helps diagnose PATH issues.
35. Pipes `|` (example: `ls | less`)
    Sends the output of one command to another. `ls | less` lets you scroll long directory listings interactively.