# bottom up
def min_drops(floors, eggs):
    opt_floors = {}
    L = sp = [[float("inf") for j in range(eggs+1)] for i in range(floors)]
    for i in range(floors):
        sp[i][1] = i+1
    for j in range(1, eggs+1):
        sp[0][j] = 1
    for i in range(1, floors):
        for j in range(2, eggs+1):
            current_min = float("inf")
            current_index = -1
            for n in range(1, i+1):
                if current_min >= max(sp[i-n][j], sp[n-1][j-1]) + 1:
                    current_min = max(sp[i-n][j], sp[n-1][j-1]) + 1
                    current_index = n
            sp[i][j] = current_min
            opt_floors[i,j] = current_index
    return sp[floors-1][eggs]

# top down 
def eggDrop(eggs, floors, memo={}):
    if floors == 0 or floors == 1:
        return floors
    if eggs == 1:
        return floors
    if (eggs, floors) in memo:
        return memo[(eggs,floors)]
    else:
        min_drops = float('inf')
        for i in range(1, floors+1):
            drops = 1 + max(eggDrop(eggs-1, i-1, memo), eggDrop(eggs, floors-i, memo))
            if drops < min_drops:
                min_drops = drops
        memo[(eggs, floors)] = min_drops
        return min_drops


# recursive
def total_EnglishStr(n,k):
    if n < k:
        return 26**n
    m = 0
    for i in range(k):
        m += 5**i * 21 * total_EnglishStr(n-i-1, k)
    return m

# top down
def total_EnglishStr_tp(n, k, memo={}):
    if n < k:
        return 26 ** n
    if (n, k) in memo:
        return memo[(n, k)]
    m = 0
    for i in range(k):
        m += 5 ** i * 21 * total_EnglishStr_tp(n - i - 1, k, memo)
    memo[(n, k)] = m
    return m


# bitstring
def total_bitstrings(n,k):
    if n < k:
        return 2**n 
    m = 0 
    for i in range(k):
        m += total_bitstrings(n-i-1, k)
    return m

# top down
def total_bitstrings_tp(n, k, memo={}):
    m = 0
    if n < k:
        return 2**n 
    if (n,k) in memo:
        return memo[(n,k)]
    m = 0 
    for i in range(k):
        m += total_bitstrings_tp(n-i-1, k, memo)
    return m 


print(total_bitstrings(11, 5))
print(total_bitstrings_tp(11, 5))