# Python List

# lookup -> L[i] -> O(1)
# copy -> O(n)

# append -> O(1) -> after a huge amount of test cases, the spikes(outliers) is increasing linearly and the space between 
# each outlier is increasing linearly -> O(n) worst case and O(1) worst amortised (constant amortised time)
# it is actually array behind the sceen, and keep track of the tail, once you append on that tail index, python creates a new array and increases
# it by 12.5%. Then copy all values from the old list to the new list, which is O(n)
