# O(a + b)
def print_items_1(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print_items_1(5,6) 

# O(a * b)
def print_items_2(a,b):
    for i in range(a):
        for j in range(b):
            print(i,j)
        
    
print_items_2(5,6) 

# O(a + b)
# Two separate loops, each runs independently.
# Total operations = a + b
# Therefore, O(a + b)

# O(a * b)
# Two nested loops, inner loop runs b times for each of a iterations.
# Total operations = a * b
# Therefore, O(a * b)
