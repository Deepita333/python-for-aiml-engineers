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
## 5️⃣ Variables 
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
## 6️⃣ Python Data Types
Python has the following data types built-in by default, in these categories:

## 1. Basic (Built-in) Data Types

| Type        | Example         | Description                                   |
|-------------|----------------|-----------------------------------------------|
| **int**     | `42`           | Whole numbers (positive, negative, zero).     |
| **float**   | `3.14`         | Numbers with decimals.                        |
| **complex** | `2 + 3j`       | Complex numbers with real & imaginary parts.  |
| **str**     | `"Hello"`      | Text/strings.                                  |
| **bool**    | `True`, `False`| Boolean values (logical truth).               |
| **NoneType**| `None`         | Represents “no value” or null.                |

---

## 2. Sequence Types

| Type      | Example         | Description                     |
|-----------|----------------|---------------------------------|
| **list**  | `[1, 2, 3]`    | Ordered, mutable collection.    |
| **tuple** | `(1, 2, 3)`    | Ordered, immutable collection.  |
| **range** | `range(5)`     | Sequence of numbers.            |

---

## 3. Set Types

| Type         | Example                 | Description                        |
|--------------|------------------------|------------------------------------|
| **set**      | `{1, 2, 3}`            | Unordered, unique elements.        |
| **frozenset**| `frozenset({1, 2, 3})` | Like `set` but immutable.          |

---

## 4. Mapping Type

| Type    | Example                               | Description              |
|---------|---------------------------------------|--------------------------|
| **dict**| `{"name": "Deepita", "age": 21}`      | Key–value pairs.         |

---

## 5. Binary Types

| Type          | Example                                | Description                      |
|---------------|----------------------------------------|----------------------------------|
| **bytes**     | `b"hello"`                             | Immutable sequence of bytes.     |
| **bytearray** | `bytearray([65, 66, 67])`              | Mutable sequence of bytes.       |
| **memoryview**| `memoryview(b"hello")`                 | View of memory without copying.  |

---

### note: 
You can get the data type of any object by using the type() function:
```python
x = 5
print(type(x))
```
output will be : 
<class 'int'>
```python
x = "Hello World"
print(type(x))
```
output will be: <class 'str'>

## 7️⃣ Python Operators

In Python, **operators** are special symbols that perform operations on variables and values.

---

## 1. Arithmetic Operators

| Operator | Name              | Example      | Result  |
|----------|-------------------|--------------|---------|
| `+`      | Addition          | `5 + 3`      | `8`     |
| `-`      | Subtraction       | `5 - 3`      | `2`     |
| `*`      | Multiplication    | `5 * 3`      | `15`    |
| `/`      | Division          | `5 / 2`      | `2.5`   |
| `//`     | Floor Division    | `5 // 2`     | `2`     |
| `%`      | Modulus           | `5 % 2`      | `1`     |
| `**`     | Exponentiation    | `2 ** 3`     | `8`     |

---

## 2. Comparison Operators

| Operator | Name                     | Example     | Result  |
|----------|--------------------------|-------------|---------|
| `==`     | Equal to                  | `5 == 3`    | `False` |
| `!=`     | Not equal to              | `5 != 3`    | `True`  |
| `>`      | Greater than              | `5 > 3`     | `True`  |
| `<`      | Less than                 | `5 < 3`     | `False` |
| `>=`     | Greater than or equal to  | `5 >= 3`    | `True`  |
| `<=`     | Less than or equal to     | `5 <= 3`    | `False` |

---

## 3. Logical Operators

| Operator | Name   | Example                | Result  |
|----------|--------|------------------------|---------|
| `and`    | AND    | `(5 > 3) and (2 > 1)`  | `True`  |
| `or`     | OR     | `(5 > 3) or (2 < 1)`   | `True`  |
| `not`    | NOT    | `not (5 > 3)`          | `False` |

---

## 4. Assignment Operators

| Operator | Example      | Equivalent To   |
|----------|--------------|-----------------|
| `=`      | `x = 5`      | `x = 5`         |
| `+=`     | `x += 3`     | `x = x + 3`     |
| `-=`     | `x -= 3`     | `x = x - 3`     |
| `*=`     | `x *= 3`     | `x = x * 3`     |
| `/=`     | `x /= 3`     | `x = x / 3`     |
| `//=`    | `x //= 3`    | `x = x // 3`    |
| `%=`     | `x %= 3`     | `x = x % 3`     |
| `**=`    | `x **= 3`    | `x = x ** 3`    |
| `&=`     | `x &= 3`     | `x = x & 3`     |
| `|=`     | `x |= 3`     | `x = x \| 3`    |
| `^=`     | `x ^= 3`     | `x = x ^ 3`     |
| `>>=`    | `x >>= 3`    | `x = x >> 3`    |
| `<<=`    | `x <<= 3`    | `x = x << 3`    |

---

## 5. Bitwise Operators

| Operator | Name          | Example    | Result (Binary) |
|----------|---------------|------------|-----------------|
| `&`      | AND           | `5 & 3`    | `1` (0001)      |
| `\|`     | OR            | `5 \| 3`   | `7` (0111)      |
| `^`      | XOR           | `5 ^ 3`    | `6` (0110)      |
| `~`      | NOT           | `~5`       | `-6`            |
| `<<`     | Left Shift    | `5 << 1`   | `10` (1010)     |
| `>>`     | Right Shift   | `5 >> 1`   | `2` (0010)      |

---

## 6. Membership Operators

| Operator | Example         | Result  |
|----------|-----------------|---------|
| `in`     | `"a" in "cat"`  | `True`  |
| `not in` | `"b" not in "cat"` | `True`  |

---

## 7. Identity Operators

| Operator | Example           | Result  |
|----------|-------------------|---------|
| `is`     | `x is y`          | True if both refer to same object |
| `is not` | `x is not y`      | True if they refer to different objects |

---

## Example Code

```python
x = 10
y = 5

print(x + y)      # Arithmetic → 10 + 5 = 15
print(x > y)      # Comparison → 10 > 5 → True
print(x and y)    # Logical AND (non-boolean values)
                  # In Python, 'and' returns the last truthy value
                  # Since both 10 and 5 are truthy → returns 5
print(x & y)      # Bitwise AND
                  # 10 = 1010 (binary)
                  #  5 = 0101 (binary)
                  # AND = 0000 (binary) = 0
print("a" in "apple")  # Membership → 'a' is in "apple" → True

```
