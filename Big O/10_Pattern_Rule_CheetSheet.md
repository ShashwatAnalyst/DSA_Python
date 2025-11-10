# ✅ Big-O Core Rules (Revision Sheet)


🔹 ✅ **Rule 1: If inner loop depends on outer loop → triangular → O(n²)**  
Example:
```python
for i in range(n):
    for j in range(i):
        print(i, j)
```

🔹 ✅ **Rule 2: Independent loops → O(n + m)**
Example:
```python
for i in arr:
    print(i)

for j in nums:
    print(j)
```

🔹 ✅ **Rule 3: Nested, independent loops → O(n * m)**
Example:
```python
for i in arr:
    for j in nums:
        print(i, j)
```

🔹 ✅ **Rule 4: Constant inner loop → O(n)**
Example:
```python
for i in range(n):
    for j in range(10):   # constant
        print(i, j)
```

🔹 ✅ **Rule 5: Doubling/Halving → O(log n)**
Example:
```python
x = 1
while x < n:
    x *= 2

```

🔹 ✅ **Rule 6: Outer loop n + inner loop log n → O(n log n)**
Example:
```python
for i in range(n):
    x = 1
    while x < n:
        x *= 2

```

🔹 ✅ **Rule 7: Simple loop → O(n)**
Example:
```python
for i in arr:
    print(i)

```

🔹 ✅ **Rule 8: Dual nested same-size loops → O(n²)**
Example:
```python
for i in range(n):
    for j in range(n):
        print(i, j)

```

🔹 ✅ **Rule 9: Drop constants & lower-order terms**
Example:
```python
O(50n) → O(n)
O(n + n²) → O(n²)
O(5n + 20) → O(n)


```

🔹 ✅ **Rule 10: Add when loops are separate, multiply when nested**
Example:
```python
Separate loops → O(n + m)
Nested loops  → O(n * m)

```