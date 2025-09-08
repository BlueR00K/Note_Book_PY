# Working with Interactive Mode in Python

## 1. Syllabus

- Introduction to interactive mode
- Starting Python in interactive mode
- Interactive mode vs. script mode
- The Python REPL (Read-Eval-Print Loop)
- Using the command line and Python shell
- Editing and recalling previous commands
- Using built-in functions and help system
- Importing modules and running code interactively
- Working with variables and objects
- Using underscore (_) and last result
- Multi-line statements and code blocks
- Using the `site` and `rlcompleter` modules
- Tab completion and history
- Running system commands from the REPL
- Using IPython and enhanced shells
- Debugging interactively
- Real-world scenarios and productivity tips
- Best practices and anti-patterns
- Advanced interactive mode features and edge cases
- IPython, Jupyter, and enhanced interactive workflows
- Debugging and profiling in interactive mode
- Real-world productivity patterns
- Anti-patterns and what to avoid
- Summary tables and feature comparison
- Final thoughts and key takeaways

---

## 2. Introduction to Interactive Mode

Interactive mode is a powerful feature of Python that allows you to execute code statements one at a time and see immediate results. It is ideal for experimentation, learning, debugging, and quick calculations. The interactive mode is also known as the Python shell or REPL (Read-Eval-Print Loop).

---

## 3. Starting Python in Interactive Mode

- Open a terminal or command prompt
- Type `python` or `python3` and press Enter
- You will see the Python prompt, usually `>>>`

```sh
$ python
Python 3.12.0 (default, Oct  2 2025, ...) 
[GCC ...] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can also start interactive mode by running `python -i script.py` to execute a script and then drop into the shell.

---

## 4. Interactive Mode vs. Script Mode

- **Interactive mode:** Executes statements one at a time, shows results immediately
- **Script mode:** Runs a file as a program, output only as specified by print statements
- Use interactive mode for exploration, script mode for production code

---

## 5. The Python REPL (Read-Eval-Print Loop)

- **Read:** Accepts user input
- **Eval:** Evaluates the input as Python code
- **Print:** Displays the result
- **Loop:** Repeats the process

The REPL is the core of interactive mode, making Python a great tool for rapid prototyping and learning.

---

## 6. Using the Command Line and Python Shell

- You can pass expressions directly: `python -c "print(2 + 2)"`
- Use the up/down arrows to recall previous commands
- Use Ctrl+D (Unix) or Ctrl+Z (Windows) to exit

---

## 7. Editing and Recalling Previous Commands

- Use the arrow keys to navigate command history
- Ctrl+A/E to move to start/end of line
- Ctrl+K/U to kill/undelete text
- Use `readline` features for advanced editing (Unix)

---

## 8. Using Built-in Functions and Help System

- Use `help()` for documentation
- Use `dir()` to list attributes of objects
- Use `type()` to check types

```python
>>> help(str)
>>> dir(list)
>>> type(42)
```

---

## 9. Importing Modules and Running Code Interactively

- Import standard and third-party modules as usual
- Define functions and classes interactively
- Use `from module import ...` for specific imports

```python
>>> import math
>>> math.sqrt(16)
4.0
```

---

## 10. Working with Variables and Objects

- Assign variables and use them immediately
- Objects persist until you exit the session
- Use `_` to access the last result

```python
>>> x = 10
>>> x * 2
20
>>> _ + 5
25
```

---

## 11. Using Underscore (_) and Last Result

- The special variable `_` holds the result of the last expression
- Useful for quick calculations and chaining operations

---

## 12. Multi-line Statements and Code Blocks

- Use indentation for multi-line code
- The REPL will show `...` for continuation lines

```python
>>> for i in range(3):
...     print(i)
...
0
1
2
```

---

## 13. Using the `site` and `rlcompleter` Modules

- The `site` module is automatically imported and sets up the environment
- `rlcompleter` enables tab completion (Unix)
- Add `import rlcompleter; import readline; readline.parse_and_bind('tab: complete')` to your startup file for tab completion

---

## 14. Tab Completion and History

- Tab completion works for variable names, modules, and attributes
- Command history is saved in `.python_history` (Unix)
- Use `PYTHONSTARTUP` environment variable to customize startup

---

## 15. Running System Commands from the REPL

- Use `os.system()` or `subprocess` to run shell commands

```python
>>> import os
>>> os.system('ls')
```

---

## 16. Using IPython and Enhanced Shells

- IPython is a powerful alternative to the default REPL
- Features: syntax highlighting, magic commands, better history, rich output
- Start with `ipython` in your terminal

---

## 17. Debugging Interactively

- Use `pdb` for interactive debugging
- Set breakpoints with `breakpoint()`
- Inspect variables and step through code

```python
>>> import pdb; pdb.set_trace()
```

---

## 18. Real-World Scenarios and Productivity Tips

- Test code snippets before adding to scripts
- Explore libraries and APIs interactively
- Use for quick calculations and data exploration
- Debug and inspect objects on the fly

---

## 19. Best Practices and Anti-Patterns

- Use interactive mode for learning, prototyping, and debugging
- Avoid writing large programs interactively—use scripts or notebooks
- Save useful code to files for reuse
- Be aware that variables are lost when you exit

---

## 20. Summary and Key Takeaways

- Interactive mode is a core strength of Python for rapid development
- Use the REPL for exploration, learning, and debugging
- Enhance your workflow with tab completion, history, and IPython

---

## 21. Advanced Interactive Mode Features and Edge Cases

### 21.1. Customizing the Interactive Startup Environment

- Use the `PYTHONSTARTUP` environment variable to run a Python script at startup.
- Customize your environment with imports, functions, or tab completion.

**Example:**
Create a file `~/.pystartup`:

```python
import rlcompleter, readline
readline.parse_and_bind('tab: complete')
print('Custom Python interactive environment loaded!')
```

Then set the environment variable:

```sh
export PYTHONSTARTUP=~/.pystartup
```

### 21.2. Using the `code` Module for Custom REPLs

You can embed an interactive interpreter in your own scripts:

```python
import code
vars = {'x': 42}
code.interact(local=vars)
```

### 21.3. Advanced Tab Completion and History Management

- Use `readline` for advanced history and editing (Unix)
- Save and load command history with `readline.write_history_file()` and `readline.read_history_file()`

### 21.4. Multi-line Editing and Paste Mode

- Use Ctrl+E (IPython) or `%paste` magic for multi-line code
- In standard REPL, paste code blocks and use correct indentation

### 21.5. Using the Interactive Mode in IDEs and Editors

- Most editors (VS Code, PyCharm, Thonny) have built-in interactive consoles
- These often support history, variable inspection, and code completion

---

## 22. IPython, Jupyter, and Enhanced Interactive Workflows

### 22.1. IPython Features

- Magic commands (e.g., `%timeit`, `%run`, `%history`)
- Rich output (tables, plots, HTML)
- Shell command integration (`!ls`, `!pwd`)
- Interactive debugging (`%debug`)

**Example:**

```python
%timeit sum(range(1000))
!echo "Hello from the shell!"
```

### 22.2. Jupyter Notebooks

- Interactive documents with code, text, and visualizations
- Great for data science, teaching, and prototyping
- Supports rich output, widgets, and inline plots

---

## 23. Debugging and Profiling in Interactive Mode

### 23.1. Using `pdb` and Breakpoints

- Set breakpoints with `breakpoint()` (Python 3.7+)
- Use `pdb.set_trace()` for manual debugging
- Inspect variables, step through code, and evaluate expressions

### 23.2. Profiling Code Interactively

- Use `cProfile` or `%prun` (IPython) to profile code

**Example:**

```python
import cProfile
cProfile.run('sum(range(10000))')
```

---

## 24. Real-World Scenarios and Productivity Patterns

### 24.1. Rapid Prototyping and Experimentation

- Test new libraries and APIs before integrating into projects
- Prototype algorithms and data transformations interactively

### 24.2. Data Exploration and Visualization

- Use interactive mode to load, filter, and plot data
- Combine with matplotlib, pandas, or seaborn for instant feedback

### 24.3. Scripting and Automation

- Use the REPL to test shell commands, file operations, and automation scripts

### 24.4. Teaching and Learning

- Interactive mode is ideal for demonstrations, tutorials, and live coding

---

## 25. Anti-Patterns and What to Avoid

- Writing large, complex programs interactively (use scripts or notebooks)
- Relying on interactive mode for reproducible research (prefer notebooks or scripts)
- Forgetting to save important code from the REPL
- Using interactive mode for production automation

---

## 26. Summary Table: Interactive Mode Features

| Feature                        | Standard REPL | IPython | Jupyter |
|--------------------------------|:-------------:|:-------:|:-------:|
| Tab completion                 |      ✓        |    ✓    |    ✓    |
| Command history                |      ✓        |    ✓    |    ✓    |
| Magic commands                 |      ✗        |    ✓    |    ✓    |
| Rich output (plots, HTML)      |      ✗        |    ✓    |    ✓    |
| Shell command integration      |      ✗        |    ✓    |    ✓    |
| Debugging tools                |      ✓        |    ✓    |    ✓    |
| Multi-line editing             |      ✓        |    ✓    |    ✓    |
| Variable inspection            |      ✓        |    ✓    |    ✓    |
| Widgets                        |      ✗        |    ✗    |    ✓    |

---

## 27. Final Thoughts

- Mastering interactive mode and enhanced shells will make you a more productive Python developer
- Use the right tool (REPL, IPython, Jupyter) for the task
- Always save and document important code and experiments

---
