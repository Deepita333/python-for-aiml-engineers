# Conditional Statements in Python 🐍

Conditional statements are the building blocks of decision-making in programming. They allow a script to perform different actions based on a set of conditions. In Python, these are primarily handled by `if`, `elif`, and `else`.

---

## The `if` Statement

The `if` statement is the simplest form of a conditional. It executes a block of code only if a specified condition evaluates to `True`.

**Syntax:**

```python
age = 20

if age >= 18:
    print("You are eligible to vote.")
```
## The `if-else` Statement

The if-else statement provides an alternative block of code to run when the if condition is False.


**Syntax:**

if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False

```python
temperature = 15

if temperature > 25:
    print("It's a hot day!")
else:
    print("It's not a hot day.")
```
## The `if-elif-else` Statement

The if-elif-else statement (short for "else if") is used to check multiple conditions in sequence. As soon as a condition evaluates to True, its corresponding code block is executed, and the rest of the chain is skipped. The final else block is optional and runs if none of the preceding conditions are met.

**Syntax:**

if first_condition:
    # Executes if first_condition is True
elif second_condition:
    # Executes if first_condition is False and second_condition is True
else:
    # Executes if all previous conditions are False

``` python

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")
```

Output: Grade: B

## Nested if Statements

You can also place one if statement inside another. This is called nesting and allows for more complex decision-making logic.

**Syntax:**
```python 
num = 15

if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("And it is an even number.")
    else:
        print("And it is an odd number.")
else:
    print("The number is not positive.")
```
Output: The number is positive.
        And it is an odd number.

## Common Comparison Operators
Conditions in these statements often use comparison operators to compare values.

| Operator | Description              | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal to                 | `a == b` |
| `!=`     | Not equal to             | `a != b` |
| `<`      | Less than                | `a < b`  |
| `>`      | Greater than             | `a > b`  |
| `<=`     | Less than or equal to    | `a <= b` |
| `>=`     | Greater than or equal to | `a >= b` |
