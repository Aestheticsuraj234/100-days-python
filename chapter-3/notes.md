# In-Depth Notes on Conditionals in Python

Conditional statements in Python control the flow of execution depending on whether a condition is **True** or **False**. The main conditional constructs are: `if`, `elif`, `else`, the modern `match-case` (pattern matching), and the ternary (conditional expression).

***

## 1. `if` Statement

The `if` statement evaluates a condition. If the condition is `True`, the code block under it executes.

```python
x = 10
if x > 5:
    print("x is greater than 5")
# Output: x is greater than 5
```

***

## 2. `if-else` Statement

Use `else` to execute a code block when the `if` condition is `False`.

```python
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")
# Output: x is 5 or less
```

***

## 3. `if-elif-else` Statement

Use `elif` ("else if") for multiple, sequential condition checks. Only the first `True` condition executes.

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or lower")
# Output: Grade: B
```

- You can have multiple `elif` branches.
- Only one branch (the first to evaluate `True`) is executed.

***

## 4. Nested `if` Statements

You can nest `if` statements inside each other for more complex logic.

```python
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry permitted")
    else:
        print("ID required")
else:
    print("Entry denied")
# Output: Entry permitted
```

***

## 5. Ternary Conditional Expression

Also known as the "one-line if-else" or "conditional expression." Syntax:

```python
value_if_true if condition else value_if_false
```

**Example:**

```python
x = 8
result = "Even" if x % 2 == 0 else "Odd"
print(result)
# Output: Even
```

- Useful for simple, short conditions.

***

## 6. `match-case` Statement (Structural Pattern Matching)

Introduced in Python 3.10+, `match-case` is similar to `switch-case` in other languages but more powerful—it can pattern-match complex data structures.

### Basic Example:

```python
command = "start"

match command:
    case "start":
        print("Machine started")
    case "stop":
        print("Machine stopped")
    case _:
        print("Unknown command")
# Output: Machine started
```

### Matching with Variables and Patterns:

```python
point = (1, 0)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y} on Y-axis")
    case (x, 0):
        print(f"X={x} on X-axis")
    case (x, y):
        print(f"Point at ({x},{y})")
# Output: X=1 on X-axis
```

**Notes:**
- Use `_` (underscore) as the default/wildcard case.
- You can match against types, values, or even sequence and mapping patterns.

***

## 7. Indentation and Best Practices

- **Indentation** is crucial in Python—blocks under `if`, `elif`, `else`, or `case` must be indented by the same level (typically 4 spaces).
- **Boolean Operators:** Combine multiple conditions with `and`, `or`, and `not`:

```python
a, b = 5, 7
if a < 10 and b < 10:
    print("Both numbers are less than 10")
```

***

## Summary Table

| Statement             | Syntax Example                                  | Description                        |
|-----------------------|-------------------------------------------------|------------------------------------|
| if                    | if cond: ...                                    | Run code if condition is True      |
| if-else               | if cond: ... else: ...                          | Add alternative for False          |
| if-elif-else          | if cond1: ... elif cond2: ... else: ...         | Multiple, sequential checks        |
| Nested if             | if cond: if cond2: ...                          | Conditions inside other conditions |
| Ternary               | a if cond else b                                | Single-line conditional assignment |
| match-case            | match val: case patt: ... case _: ...           | Pattern matching (Py 3.10+)        |

***

These conditionals form the backbone of decision-making in Python programs, making your code responsive and adaptive to different input and scenarios.