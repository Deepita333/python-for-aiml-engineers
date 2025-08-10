# Module 1: Python Foundations

## 🎯 Learning Objectives
By the end of this module, you will:
- Understand Python syntax and basic programming concepts
- Use Python variables, data types, and operators
- Work with core data structures
- Write reusable functions

---

## 1️⃣ Getting Started

### Installing Python
- Download from [python.org](https://www.python.org/downloads/)
- Recommended IDEs: VS Code, PyCharm, Jupyter Notebook, Google Colab

### Check if Python is Installed

To check if you have Python installed:

### On Linux
```bash
python --version
```
### On macOS
```bash
python3 --version
```

## 2️⃣ Your First Python Program
Let's write our first Python file, called program.py, which can be created in any text editor:
```python
print("Hello, World!")
```
Simple as that. Save your file.

### Running the Program
Open your command line, navigate to the directory where you saved your file, and run:
```bash
python hello.py
```
Expected Output:
Hello, World!

## 3️⃣ Python Indentation
- Indentation refers to the spaces at the beginning of a code line.

- In other programming languages, indentation is for readability only.

- In Python, indentation is very important because it defines code blocks.

Example
```python
if 5 > 2:
    print("Five is greater than two!")
```
If you skip indentation, Python will give an error:

Example(Invalid)
```python
if 5 > 2:
print("Five is greater than two!")
```
## 4️⃣ Python Comments
Comments can be used to:

- Explain Python code

- Make the code more readable

- Prevent execution when testing

### Creating a Comment
Comments start with # and Python will ignore them.
```python
# This is a comment
print("Hello, World!")
```
Multiline Comments
Python does not have a dedicated syntax for multiline comments.

Option 1: Use # for each line
```python
# This is a comment
# written in
# more than just one line
print("Hello, World!")
```

Option 2: Use Multiline Strings
Since Python ignores string literals not assigned to a variable, you can use triple quotes:

```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```
## 5️⃣ Variables and Data Types
- Python has no command for declaring a variable.

- A variable is created the moment you first assign a value to it.

### Rules for Python variables:

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Variable names are case-sensitive (age, Age and AGE are three different variables)
- A variable name cannot be any of the Python keywords.

```python 
x = 5
print(x)
y = "Deepita"
print(y)
```
### Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:
```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```
### One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:
```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```
