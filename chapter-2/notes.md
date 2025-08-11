Python supports several built-in data types that allow you to store, organize, and manipulate different forms of data. Let’s explore the most commonly used data types with practical examples:

***

## 1. Numeric Types

### a) Integer (`int`)
- Whole numbers, positive or negative.
```python
x = 10
y = -7
print(type(x))  # Output: 
```

### b) Float (`float`)
- Numbers with decimal points.
```python
price = 12.99
pi = 3.14159
print(type(price))  # Output: 
```

### c) Complex (`complex`)
- Numbers with real and imaginary parts.
```python
number = 2 + 3j
print(type(number))  # Output: 
```

***

## 2. Text Type

### a) String (`str`)
- Sequence of Unicode characters.
```python
name = "Alice"
message = 'Hello, World!'
print(type(name))  # Output: 
```

***

## 3. Sequence Types

### a) List (`list`)
- Ordered, mutable (changeable), allows duplicates.
```python
fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"  # Lists are mutable
print(fruits)  # Output: ['orange', 'banana', 'cherry']
```

### b) Tuple (`tuple`)
- Ordered, immutable (cannot change), allows duplicates.
```python
coordinates = (10, 20)
# coordinates = 5  # Error: Tuples are immutable
print(type(coordinates))  # Output: 
```

### c) Range (`range`)
- Immutable sequence of numbers, commonly used in loops.
```python
r = range(5)
print(list(r))  # Output: [0, 1, 2, 3, 4]
```

***

## 4. Set Types

### a) Set (`set`)
- Unordered, mutable, unique items (no duplicates).
```python
numbers = {1, 2, 3, 2}
print(numbers)  # Output: {1, 2, 3}
numbers.add(4)
print(numbers)  # Output: {1, 2, 3, 4}
```

#### **Union and Intersection Operations**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: All unique elements from both sets
print(A | B)  # Output: {1, 2, 3, 4, 5, 6}
print(A.union(B))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements common to both sets
print(A & B)  # Output: {3, 4}
print(A.intersection(B))  # Output: {3, 4}
```

### b) Frozenset (`frozenset`)
- Immutable version of a set.
```python
fs = frozenset([1, 2, 3])
# fs.add(4)  # Error: frozensets are immutable
```

***

## 5. Mapping Type

### a) Dictionary (`dict`)
- Collection of key-value pairs, mutable, keys are unique.
```python
person = {"name": "Alice", "age": 30}
print(person["name"])      # Output: Alice
person["age"] = 31         # Update value
person["city"] = "Mumbai"  # Add new key-value pair
print(person)
# Output: {'name': 'Alice', 'age': 31, 'city': 'Mumbai'}

# Iterating over a dictionary
for key, value in person.items():
    print(key, value)
```

#### **More Dictionary Examples**
```python
# Nested dictionary
users = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25}
}
print(users["user1"]["name"])  # Output: Alice

# Creating a dictionary from two lists
keys = ["name", "age"]
values = ["Bea", 28]
employee = dict(zip(keys, values))
print(employee)  # Output: {'name': 'Bea', 'age': 28}
```

***

## 6. Boolean Type

### a) Boolean (`bool`)
- Represents truth values.
```python
is_active = True
is_closed = False
print(type(is_active))  # Output: 
```

***

## 7. Binary Types

### a) Bytes (`bytes`)
- Immutable sequence of bytes.
```python
b = b'hello'
print(type(b))  # Output: 
```

### b) Bytearray (`bytearray`)
- Mutable sequence of bytes.
```python
ba = bytearray(5)
print(ba)  # Output: bytearray(b'\x00\x00\x00\x00\x00')
```

***

### Summary Table

| Data Type   | Example                                      | Mutable       | Notes                         |
|-------------|----------------------------------------------|---------------|-------------------------------|
| int         | 42                                           | No            | Whole numbers                 |
| float       | 3.14                                         | No            | Decimal numbers               |
| complex     | 2 + 3j                                       | No            | Complex numbers               |
| str         | "hello"                                      | No            | Unicode strings               |
| list        | [1][2][3]                                    | Yes           | Ordered collection            |
| tuple       | (1, 2, 3)                                    | No            | Ordered and immutable         |
| set         | {1, 2, 3}                                    | Yes           | Unordered unique values       |
| frozenset   | frozenset([1,[2][3])                         | No            | Immutable set                 |
| dict        | {"name": "Alice", "age": 30}                 | Yes           | Key-value mapping             |
| bool        | True, False                                  | No            | Logical values                |
| bytes       | b'hello'                                     | No            | Binary literal                |
| bytearray   | bytearray(5)                                 | Yes           | Mutable binary sequence       |
| NoneType    | None                                         | No            | Absence of value              |

***

## Conclusion

Understanding these fundamental data types—and being able to manipulate them with Python’s syntax—is essential for effective programming and data analysis in Python.
