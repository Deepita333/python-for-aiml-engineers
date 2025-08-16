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
## 8️⃣ Python Lists

In Python, **lists** are ordered, mutable (changeable) collections of items. They can store elements of any data type, and the same list can contain items of different types.

### type()
From Python's perspective, lists are defined as objects with the data type 'list':
**<class 'list'>**

### Creating a List

```python
# Empty list
my_list = []

# List with elements
fruits = ["apple", "banana", "cherry"]

# List with mixed data types
mixed_list = [1, "hello", 3.5, True]
```
### Accessing List Items
Lists are indexed (starting from 0).
You can use positive or negative indexing.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[-1])  # cherry
```
### Slicing Lists
```python
fruits = ["apple", "banana", "cherry", "orange", "mango"]

print(fruits[1:3])  # ['banana', 'cherry']
print(fruits[:2])   # ['apple', 'banana']
print(fruits[2:])   # ['cherry', 'orange', 'mango']
```

### Changing List Items
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

### Adding Items to a List
```python
fruits = ["apple", "banana"]

fruits.append("cherry")       # Add at the end
fruits.insert(1, "orange")    # Insert at index 1

print(fruits)  # ['apple', 'orange', 'banana', 'cherry']
```

### Removing Items from a List

```python
fruits = ["apple", "banana", "cherry"]

fruits.remove("banana")  # Removes 'banana'
fruits.pop()             # Removes last item
del fruits[0]            # Deletes item at index 0

print(fruits)  # ['cherry']
```

### List Functions and Methods
```python
numbers = [5, 2, 9, 1]

print(len(numbers))  # 4
print(max(numbers))  # 9
print(min(numbers))  # 1

numbers.sort()       # Sort in ascending order
numbers.reverse()    # Reverse the list
numbers.clear()      # Clear all items
```
### Looping Through a List
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
### List Comprehensions

A concise way to create lists.

```python
numbers = [x for x in range(5)]
print(numbers)  # [0, 1, 2, 3, 4]

squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

```

### Nested Lists

Lists can contain other lists.
```python
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3
```


### Summary

- Lists are ordered, mutable, and can store different data types.

- Indexing starts at 0.

- Common operations: append, insert, remove, pop, sort, reverse.

- Supports slicing, nesting, and list comprehensions.

## 9️⃣ Python Tuples

A **tuple** in Python is an ordered, immutable collection of items.  Unlike lists, tuples **cannot be modified** (no adding, removing, or changing elements once created).  
They are useful when you want to store a collection of values that should remain constant.


### Creating Tuples

```python
# Empty tuple
t1 = ()

# Tuple with integers
t2 = (1, 2, 3)

# Tuple with mixed data types
t3 = (1, "hello", 3.5)

# Tuple without parentheses (packing)
t4 = 1, 2, 3

# Nested tuple
t5 = (1, (2, 3), (4, 5))

# Tuple with one element (note the comma)
t6 = (5,)
```
### Accessing Tuple Elements
```python 
t = (10, 20, 30, 40, 50)

print(t[0])   # First element → 10
print(t[-1])  # Last element → 50
print(t[1:4]) # Slicing → (20, 30, 40)
```

### Tuple Operations 
```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
print(t1 + t2)  # (1, 2, 3, 4, 5, 6)

# Repetition
print(t1 * 2)   # (1, 2, 3, 1, 2, 3)

# Membership
print(2 in t1)   # True
print(10 not in t1) # True

# Length
print(len(t1))   # 3
```

### Tuple Methods

Tuples have only two built-in methods:

```python
t = (1, 2, 2, 3, 4)

print(t.count(2))   # 2 (counts occurrences of 2)
print(t.index(3))   # 3 (returns first index of value 3)

# Tuple Unpacking : in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
t = (100, 200, 300)

# Unpacking
a, b, c = t
print(a, b, c)  # 100 200 300

# Extended unpacking
t2 = (1, 2, 3, 4, 5)
x, *y, z = t2 # If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
print(x)  # 1
print(y)  # [2, 3, 4]
print(z)  # 5
```

### Immutability of Tuples

Tuples cannot be changed after creation:
```python 
t = (1, 2, 3)
# t[0] = 100   # ❌ Error: 'tuple' object does not support item assignment


# However, if a tuple contains mutable elements (like lists), those can be modified:

t = (1, [2, 3], 4)
t[1][0] = 99
print(t)   # (1, [99, 3], 4)
```

### Why Use Tuples?

- Immutability → safer for constant data.

- Performance → faster than lists in certain operations.

- Hashable → can be used as dictionary keys and set elements (if they contain only immutable data).

Python Sets

In Python, a **set** is an unordered collection of unique and immutable elements.  
It is commonly used when you want to store multiple items without duplicates.

---

## 🔟 Python Sets
```python
# Using curly braces
fruits = {"apple", "banana", "cherry"}

# Using set() constructor
numbers = set([1, 2, 3, 4, 4, 5])  # Duplicates removed
print(numbers)  # {1, 2, 3, 4, 5}
```
⚠️ Note: Empty curly braces {} create a dictionary, not a set.
To create an empty set, use set().

### Set Properties
- Unordered: No defined order (cannot be indexed like lists).

- unique: No duplicate elements.

- Mutable: You can add or remove items, but elements must be immutable (e.g., you cannot have lists inside sets).

### Accessing Elements
Sets are unordered, so you cannot access elements by index.
You can loop through a set instead:

```python
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)
```
### Adding Elements
``` python
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # {"apple", "banana", "cherry"}

# Add multiple items
fruits.update(["orange", "mango"])
print(fruits)  # {"apple", "banana", "cherry", "orange", "mango"}
```
### Removing Elements
``` python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")   # Raises error if not found
print(fruits)

fruits.discard("apple")   # No error if not found
print(fruits)

fruits.pop()  # Removes a random element
print(fruits)

fruits.clear()  # Empty the set
print(fruits)   # set()
```

### Set Operations
Sets support mathematical operations like union, intersection, and difference.

``` python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (all elements)
print(A | B)        # {1, 2, 3, 4, 5, 6}
print(A.union(B))   # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(A & B)        # {3, 4}
print(A.intersection(B))  # {3, 4}

# Difference (in A but not in B)
print(A - B)        # {1, 2}
print(A.difference(B))  # {1, 2}

# Symmetric Difference (elements in either set, not both)
print(A ^ B)        # {1, 2, 5, 6}
print(A.symmetric_difference(B))  # {1, 2, 5, 6}
```

### Set Membership

```python
A = {1, 2, 3}
print(2 in A)   # True
print(5 not in A) # True
```
### Frozen Sets
A frozenset is an immutable version of a set (cannot be modified after creation).

```python

frozen = frozenset([1, 2, 3, 2])
print(frozen)  # frozenset({1, 2, 3})

# You cannot add or remove elements from a frozenset
```
### Summary
- Set = mutable, unordered, unique elements.

- Frozen Set = immutable version of set.

- Useful for mathematical set operations and removing duplicates.


