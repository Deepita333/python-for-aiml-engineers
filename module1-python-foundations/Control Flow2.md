## Loops in Python 🔁
Loops are a fundamental concept in programming that allow you to execute a block of code multiple times. This is useful for iterating over lists, processing data, or performing any action that needs to be repeated. Python has two primary types of loops: the for loop and the while loop.

## The `for` Loop
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). It's best used when you know how many times you want the loop to run.

**Syntax:**
``` python
for item in sequence:
    # Code to execute for each item
 ```   
Example (Iterating over a list)

``` Python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```
This loop will print each fruit in the fruits list on a new line.

## The `range()` Function
Often, you'll want to run a loop a specific number of times. The range() function is perfect for this. range(5) generates numbers from 0 up to (but not including) 5.

``` Python
for i in range(5):
    print(f"This is loop number {i}")
```
Output: This is loop number 0
        This is loop number 1
        This is loop number 2
        This is loop number 3
        This is loop number 4

## The `while` Loop
A while loop executes a block of code as long as a specified condition remains True. It's best used when you don't know in advance how many times the loop needs to run.
**Syntax:**
```Python
while condition:
    # Code to execute as long as condition is True
```
Important: You must include logic inside the while loop that will eventually make the condition False, otherwise you will create an infinite loop.

Example: (A simple countdown)

``` Python
count = 5

while count > 0:
    print(count)
    count = count - 1  # This line prevents an infinite loop

print("Blastoff!")
```

## Loop Control Statements
You can change the flow of a loop using control statements. The two most common are break and continue.

### break
The break statement is used to exit a loop completely, regardless of the loop's condition.

Example
```Python
for number in range(10):
    if number == 5:
        break  # Exit the loop when number is 5
    print(number)

print("Loop finished.")
```
This code will print numbers from 0 to 4 and then stop.

### continue
The continue statement is used to skip the rest of the code inside the current iteration and move to the next one.

Example
```Python
for number in range(10):
    if number % 2 == 0:
        continue  # Skip the print statement for even numbers
    print(number)
```
This code will only print the odd numbers between 0 and 9 (1, 3, 5, 7, 9).
