# O(log n) Search

# We want to find number 1 in a sorted list of 8 items:
#            ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐
#   List  =  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │  8  │
#            └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘


# We DO NOT search one by one like linear search.

# STEP 1: Cut the list in half → [1,2,3,4] | [5,6,7,8]
# Middle value is 4
# Since 1 < 4 → the answer must be in the LEFT half
# So we THROW AWAY the entire right half.

#            ┌─────┬─────┬─────┬─────┐   ┌─────┬─────┬─────┬─────┐
#            │  1  │  2  │  3  │  4  │   │  5  │  6  │  7  │  8  │
#            └─────┴─────┴─────┴─────┘   └─────┴─────┴─────┴─────┘
#                    ^                           ^
#   Keep  ───────────┘                           └────────────✗✗✗✗ Discard


# STEP 2: Cut the list in half → [1,2] | [3,4]
# Middle value is 2
# Since 1 < 2 → the answer must be in the LEFT half again
# So we THROW AWAY the right half.

#            ┌─────┬─────┐   ┌─────┬─────┐
#            │  1  │  2  │   │  3  │  4  │
#            └─────┴─────┘   └─────┴─────┘
#                  ^                ^
#   Keep ──────────┘                └────────✗✗ Discard


# STEP 3: Cut the left half → [1] | [2]
# We want 1 → FOUND ✅
# Discard the other value.

#            ┌─────┐   ┌─────┐
#    FOUND → │  1  │   │  2  │
#            └─────┘   └─────┘
#                         ^
#                         └────────✗ Discard


# It took 3 steps to find a value from a list of 8 values.
# For n = 8 → 3 operations
# As the list grows, number of steps grows very slowly.

# It just so happens that 2^3 = 8 or log˅2 8 = 3

# For n = 1073741824
# log˅2 1073741824 = 31
# To find a value in a list of 1073741824 values it will take 31 operations using O(log n) search

# O(log n) Graph

#   Number of Operations
#           ^
#        10 |             
#         9 | 
#         8 |
#         7 |         
#         6 |
#         5 |
#         4 |                           * <-- O(log n)
#         3 |           *
#         2 |*
#         1 |
#         0 -------------------------------------> n
#            1 2  4  6  8  10  12  14  16  18  20


#  Graph Compairing O(n^2) , O(n) , O(1) and O(log n)

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
#         9 | 
#         8 |           *
#         7 |         
#         6 |        *
#         5 |
#         4 |     *                     * <-- O(log n)
#         3 |           *
#         2 |*        
#         1 |  *  *  *  *   *   *   *   *   *  * <-- O(1)
#         0 ---------------------------------------> n
#            1 2  4  6  8  10  12  14  16  18  20
