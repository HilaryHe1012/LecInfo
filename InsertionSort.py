import timeit
# coding directly in instead of calling help functions -> not a significant improvement
def insertionSort(array):
    for i in range(1,len(array)):
        j = i-1
        # single assignement
        value = array[i]
        while j >= 0 and value < array[j] :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = value
    return

array = [7,5,6,1,3,9]
insertionSort(array)
for i in array:
    print(i)