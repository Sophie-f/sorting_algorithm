def binary(array, y):
    mid = len(array) // 2
    if y == array[mid]:
        return mid
    elif len(array) > 1 and y < array[mid]:
        return binary(array[0:mid], y)
    elif len(array) > 1 and y > array[mid]:
        index = binary(array[mid:len(array)], y)
        if index == "not find":
            return index
        else:
            return mid+index
    else:
        return "not found"


def binary_2(array, x):  # not recursive and can not show the index of x element
    up = len(array)
    down = 0
    while up >= down:
        mid = (up+down) // 2
        if x == array[mid]:
            return mid
        if x < array[mid]:
            up = mid-1
        elif x > array[mid]:
            down = mid+1
    return "not found"
