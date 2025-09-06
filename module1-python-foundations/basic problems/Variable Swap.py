# You are given two variables, a = 10 and b = 20. Without using a third variable, swap their values so that a becomes 20 and b becomes 10. Print the new values of a and b.
a = 10
b = 20
print(f"Before swap: a = {a}, b = {b}")


a, b = b, a

print(f"After swap: a = {a}, b = {b}")
