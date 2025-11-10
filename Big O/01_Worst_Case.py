# Dealing with Time Complexity and Space Complexity
# There are 3 Greek letters commonly used to describe algorithm performance:

#   Ω (Omega)   - Best Case
#   Θ (Theta)   - Average Case
#   O (Big O)   - Worst Case

# Let's suppose we want to find a number in a list.

#            ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┐
#   List  =  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │
#            └─────┴─────┴─────┴─────┴─────┴─────┴─────┘
#               Ω                 Θ                 O
#           Best Case        Average Case       Worst Case

#   Ω (Best Case): Finding 1 — we find it in one operation.
#   Θ (Average Case): Finding 4 — we search about half the list on average.
#   O (Worst Case): Finding 7 — we might have to search the entire list.

# Note:
# When we talk about "Big O", we usually refer to the *worst-case* performance,
# which helps us understand the upper bound of an algorithm’s growth rate.
