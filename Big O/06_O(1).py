def add_items(n):
    return n + n + n

print(add_items(10)) # <-- Here , n = 10 → "1 Operation" 
# and it will remain "1 Operation" for whatever value on n, So its O(1)

# O(1) Graph

#   Number of Operations
#           ^     
#        50 |
#        45 |
#        40 |
#        35 |
#        30 |
#        25 |
#        20 |
#        15 |
#        10 |
#         8 |
#         6 |
#         4 |
#         2 |
#         1 |  *  *  *  *   *   *   *   *   *   * <-- O(1)
#         0 ---------------------------------------> n
#              2  4  6  8  10  12  14  16  18  20

#  Graph Compairing O(n^2) , O(n) and  O(1)

#   Number of Operations
#           ^     
#        50 |      * <-- O(n^2)
#        45 |
#        40 |     *
#        35 |
#        30 |    *
#        25 |
#        20 |  *
#        15 |
#        10 |*             * <-- O(n)
#         8 |           *
#         6 |        *
#         4 |     *
#         2 |  *
#         1 |  *  *  *  *   *   *   *   *   *   * <-- O(1)
#         0 ---------------------------------------> n
#              2  4  6  8  10  12  14  16  18  20

#  As 'n' increases, the number of operations remains 1.
#  If n = 100  → 1 operation
#  If n = 10000 → 1 operation
#  If n = 1000000 → 1 operation

#  So the growth is Constant at 1 → This is O(1)
#  O(1) is the most efficient Big O
