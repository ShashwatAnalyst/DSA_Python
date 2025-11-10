def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10) # <-- here n = 10 → "20 Operations", So its O(2n)


#  Graph for O(2n)

#   Number of Operations
#           ^
#        20 |                             * <-- O(2n)
#        18 |                          *
#        16 |                       *
#        14 |                    *
#        12 |                 *
#        10 |              *
#         8 |           *
#         6 |        *
#         4 |     *
#         2 |  *
#         0 |---------------------------------> n
#           0  1  2  3  4  5  6  7  8  9  10

# O(n) and O(2n) both grow linearly.
# Big O describes the growth pattern, not the exact number of steps.
# Doubling the work changes the constant factor, but not the growth rate.
# Since the rate of growth is still linear, we drop constants.

# Therefore, O(2n) simplifies to O(n).
