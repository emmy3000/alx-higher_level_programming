# 0x03. Python - Data Structures: Lists, Tuples


## 0. Print a list of integers

#### Write a function that prints all integers of a list.

- Prototype: **def print_list_integer(my_list=[]):**
- Format: one integer per line.
- Invoke Python's built-in `__import__()` function to import modules at runtime.
- Assume that the list only contains integers.
- Do not cast integers into strings.
- Invoke `str.format()` method to print integers.


## 1. Secure access to an element in a list

#### Write a function that retrieves an element from a list like in C.

Prototype: def **element_at(my_list, idx):**
- If idx is negative, the function returns None.
- If idx is out of range (> of number of element in my_list) the function returns None.
- Not allowed to import any module.
- Not allowed to use try/except.


## 2. Replace element

#### Write a function that replaces an element of a list at a specific position (like in C).

Prototype: **def replace_in_list(my_list, idx, element):**
- If idx is negative, the function should not modify anything, and returns the original list.
- If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list.
- Not allowed to import any module.
- Not allowed to use try/except.


## 3. Print a list of integers... in reverse!

#### Write a function that prints all integers of a list, in reverse order.

Prototype: **def print_reversed_list_integer(my_list=[]):**
- Format: one integer per line.
- Not allowed to import any module.
- Assume that the list only contains integers.
- Not allowed to cast integers into strings.
- Use `str.format()` to print integers.
