def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

print_items(10) # <-- Here n = 10 → "100 or 10^2 Operations", So its O(n^2)

#   O(n^2) Graph

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
#        10 |*             
#         0 |-------------------------------------> n
#           0  2  4  6  8  10  12  14  16  18  20

#  Graph Compairing O(n^2) and O(n)

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
#         0 |-------------------------------------> n
#           0  2  4  6  8  10  12  14  16  18  20

#  As 'n' increases, the number of operations grows quadratically (n^2).
#  If n = 10  → 100 operations
#  If n = 100 → 10000 operations
#  If n = 1000 → 1000000 operations

#  So the growth is quadratic → This is O(n^2)
