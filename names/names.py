import time

start_time = time.time()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if self.value > value:
            if self.left:
                return self.left.insert(value)
            # check if dot right exists.
            else:
                self.left = new_node
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True

        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# new_BST = BSTNode(names_1[0])
# print('check here ', names_1[0])
# for name_1 in names_1:
#     new_BST.insert(name_1)

# # runtime: 0.1593010425567627 seconds
# for name in names_2:
#     if new_BST.contains(name):
#         duplicates.append(name)

# end_time = time.time()
# print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#  this is O(n2) two for loops but there not nested
#  original runtime was about 5.5 seconds
#  my solution with list and for loops was 2.3 seconds.


def isDuplicate(arr, value):

    for a in arr:
        if a == value:
            duplicates.append(a)


# runtime: 2.3010408878326416 seconds
for x in names_2:
    if isDuplicate(names_1, x):
        duplicates.append(x)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
