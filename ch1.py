# grokking algorithms chapter 1

## binary search
'''
item {*} - the item for which to search
list {list} - sorted list
return {int} - the index of the item, or None if not found.
'''
def binary_search(item, list):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        elif item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None

print(binary_search(155, list(range(100, 300))))            # 55
print(binary_search(-20, list(range(300))))                 # None
print(binary_search(100, [0, 4, 10, 25, 100, 150, 240]))    # 4

########################################

# 1.1   7 steps
# 1.2   8 steps