my_list = [11,3,23,7]

#               ┌─────┬─────┬─────┬─────┐
#     my_list = │ 11  │  3  │ 23  │  7  │
#               └─────┴─────┴─────┴─────┘
#                 0      1      2      3


my_list.append(17)
print(my_list)

#                     ┌─────┬─────┬─────┬─────┬─────┐
#     my_list =       │ 11  │  3  │ 23  │  7  │  17 │
#                     └─────┴─────┴─────┴─────┴─────┘
#                        0     1     2     3     4
#                        ^                       ^
#    No re-indexing ─────┘                       └────── append(17)

# Explanation:
# append(17) just places the new element at index 4.
# No re-indexing. Just one operation.
# Therefore, O(1).


my_list.pop()
print(my_list)

#                     ┌─────┬─────┬─────┬─────┐   ┌─────┐
#     my_list =       │ 11  │  3  │ 23  │  7  │   │  17 │
#                     └─────┴─────┴─────┴─────┘   └─────┘
#                       0      1      2      3        4
#                       ^                             ^
#   No re-indexing ─────┘                             └──── pop()

# Explanation:
# pop() removes the last element.
# No re-indexing.
# Therefore, O(1).


my_list.pop(0)
print(my_list)

#  pop(0) ────────────┐
#                     v
#                 ┌─────┐   ┌─────┬─────┬─────┐
#       my_list = │ 11  │   │  3  │ 23  │  7  │
#                 └─────┘   └─────┴─────┴─────┘
#                    0        1      2      3
#                             ↑      ↑      ↑
#                       (INDEX-1)(INDEX-1)(INDEX-1)

# After pop(0): EVERY Index changes

#               ┌─────┬─────┬─────┐
#     my_list = │  3  │ 23  │  7  │
#               └─────┴─────┴─────┘
#                 0      1      2
#                 ↑      ↑      ↑
#  re-indexing ───┴──────┴──────┘

# Explanation:
# pop(0) removes index 0.
# Every index changes.
# Therefore, O(n).


my_list.insert(0,11)
print(my_list)

#       insert(0,11) ───────┐
#                           v
#                        ┌─────┬─────┬─────┬─────┐
#     my_list =          │ 11  │  3  │ 23  │  7  │
#                        └─────┴─────┴─────┴─────┘
#                                0      1      2
#                                ↑      ↑      ↑
#                          (INDEX+1)(INDEX+1)(INDEX+1)


# After insert(0,11): EVERY Index changes

#               ┌─────┬─────┬─────┬─────┐
#     my_list = │ 11  │  3  │ 23  │  7  │
#               └─────┴─────┴─────┴─────┘
#                 0      1     2     3
#                 ↑      ↑     ↑     ↑
#  re-indexing ───┴──────┴─────┴─────┘

# Explanation:
# insert(0,11) makes space at index 0.
# Indexes change.
# Therefore, O(n).


my_list.insert(1,'Hi')
print(my_list)

#                           ┌────────── insert(1,'Hi')
#                           v
#                  ┌─────┬─────┬─────┬─────┬─────┐
#     my_list =    │ 11  │ 'Hi'│  3  │ 23  │  7  │
#                  └─────└─────┴─────┴─────┴─────┘
#                     0           1      2      3
#                                 ↑      ↑      ↑
#                           (INDEX+1)(INDEX+1)(INDEX+1)

# After insert(1, "Hi"), HALF of the index changes, Therefore O(1/2n) -> O(n) (1/2 is constant)

#               ┌─────┬─────┬─────┬─────┬─────┐
#     my_list = │ 11  │ "Hi"│  3  │ 23  │  7  │
#               └─────┴─────┴─────┴─────┴─────┘
#                 0      1     2     3     4
#                        ↑     ↑     ↑     ↑
#      re-indexing ──────┴─────┴─────┴─────┘

# Explanation:
# insert(1,'Hi) makes space at index 1.
# Indexes change.
# Therefore, O(n).


my_list.pop(1)
print(my_list)

#         pop(1) ────────────┐
#                            v
#                 ┌─────┐ ┌─────┐ ┌─────┬─────┬─────┐
#       my_list = │ 11  │ │ "Hi"│ │  3  │ 23  │  7  │
#                 └─────┘ └─────┘ └─────┴─────┴─────┘
#                    0       1      2      3      4
#                                   ↑      ↑      ↑
#                             (INDEX-1)(INDEX-1)(INDEX-1)

# After pop(1): HALF of the index changes, Therefore O(1/2n) -> O(n) (1/2 is constant)

#               ┌─────┬─────┬─────┬─────┐
#     my_list = │ 11  │  3  │ 23  │  7  │
#               └─────┴─────┴─────┴─────┘
#                  0    1      2      3
#                       ↑      ↑      ↑
#        re-indexing ───┴──────┴──────┘

# Explanation:
# pop(1) removes index 1.
# HALF of the index changes.
# Therefore, O(n).



def find_number(n):
    global my_list
    for i in my_list:        # <-- visiting each element one-by-one
        if i == n:           # <-- comparing each element
            print(i)

find_number(7)
# We are scanning the entire list one element at a time.
# In worst case, we check ALL elements.
# Therefore, this operation grows with list size → O(n)


print(my_list[3])
# Direct access by index (jump straight to index 3)
# No looping, no scanning, no re-indexing.
# Therefore, constant time → O(1)
