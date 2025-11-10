# ✅ Big-O Core Rules (Revision Sheet)


🔹 ✅ **Rule 1: Simple loop → O(n)**

```python
for i in arr:
    print(i)

```

🔹 ✅ **Rule 2: Dual nested same-size loops → O(n²)**

```python
for i in range(n):
    for j in range(n):
        print(i, j)

```

🔹 ✅ **Rule 3: Independent loops → O(n + m)**

```python
for i in arr:
    print(i)

for j in nums:
    print(j)
```

🔹 ✅ **Rule 4: Nested, independent loops → O(n * m)**

```python
for i in arr:
    for j in nums:
        print(i, j)
```


🔹 ✅ **Rule 5: If inner loop depends on outer loop → triangular → O(n²)**  

```python
for i in range(n):
    for j in range(i):
        print(i, j)
```



🔹 ✅ **Rule 6: Constant inner loop → O(n)**

```python
for i in range(n):
    for j in range(10):   # constant
        print(i, j)
```

🔹 ✅ **Rule 7: Doubling/Halving → O(log n)**

```python
x = 1
while x < n:
    x *= 2

```

🔹 ✅ **Rule 8: Outer loop n + inner loop log n → O(n log n)**

```python
for i in range(n):
    x = 1
    while x < n:
        x *= 2

```

🔹 ✅ **Rule 9: Drop constants & lower-order terms**

```python
O(50n) → O(n)
O(n + n²) → O(n²)
O(5n + 20) → O(n)


```

🔹 ✅ **Rule 10: Add when loops are separate, multiply when nested**

```python
Separate loops → O(n + m)
Nested loops  → O(n * m)

```

🔹 ✅ **Rule 11: Accessing an element by index in a list/array → O(1)**

```python
x = arr[5]
```
🔹 ✅ **Rule 12: Append/Pop at the end of a Python list (amortized O(1))**

```python

arr.append(10)  # O(1)
arr.pop()       # O(1)

```
🔹 ✅ **Rule 13: Dictionary/Set lookup (hash-based access) → O(n)**

```python

exists = key in my_dict  
value  = my_dict[key]    

```
