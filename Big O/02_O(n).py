# Example of O(n)

def print_items(n):  # <-- We passed in a number 'n'
    for i in range(n):  # <-- It runs 'n' times
        print(i)        # <-- Each iteration is one operation

print_items(10) # <-- here n = 10 → "10 Operations", So its O(n)



#  Graph for O(n)

#   Number of Operations
#           ^
#        10 |                             * <-- O(n)
#        9  |                          *
#        8  |                       *
#        7  |                    *
#        6  |                 *
#        5  |              *
#        4  |           *
#        3  |        *
#        2  |     *
#        1  |  *
#        0  |---------------------------------> n
#           0  1  2  3  4  5  6  7  8  9  10

#  As 'n' increases, the number of operations grows linearly.
#  If n = 10  → 10 operations
#  If n = 100 → 100 operations
#  If n = 1000 → 1000 operations

#  So the growth is linear → This is O(n)
