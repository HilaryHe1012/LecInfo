def binsearchIter(value, values):
    # takes care of the base case
    if values ==[]: return False

    left, right = 0, len(values) -1
    while left <= right:
        mid = (left + right) //2
        # high probability event first in if statements
        if values[mid] < value:
            left = mid + 1
        elif values[mid] > value:
            right = mid - 1
        else:
            return True
    return False

print(binsearchIter(3, [1,5,7,10]))
# I want to test if my branch works
# I don't want to deal with merge conflict