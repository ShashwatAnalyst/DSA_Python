def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
        
    for k in range(n):
        print(k)
    
print_items(10) # <-- Here n = 10 → "110 or 10^2 + 10 Operations", So its O(n^2 + n)


#  Graph for O(n^2 + n)

#   Number of Operations
#           ^     
#        51 |      * <-- O(n^2 + n)
#        46 |
#        41 |     *
#        36 |
#        31 |    *
#        26 |
#        21 |  *
#        16 |
#        11 |*
#         0 |-------------------------------------> n
#           0  2  4  6  8  10  12  14  16  18  20


# O(n^2 + n) simplifies to O(n^2) because n^2 dominates n as n grows.
# The n term grows very slowly compared to n^2, so it becomes "insignificant".
# Big O focuses on the dominant growth term, not the lower-order ones.
# we drop the non-dominant term and keep only O(n^2).

# Therefore, O(n^2 + n) simplifies to O(n^2).
