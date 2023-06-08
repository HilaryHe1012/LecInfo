import random
import timeit

L = [12, 2, 4, 5, 15]
def subset_sum(numbers, target):
    if target == 0:
        return True
    if target < 0:
        return False
    if numbers == []:
        return False
    return subset_sum(numbers[:-1], target) or subset_sum(numbers[:-1], target - numbers[-1])


def total_calls(d):
    calls = 0
    for sp in d.keys():
        calls += d[sp]
    return calls

def max_value(d):
    current_max = 0
    for sp in d.keys():
        if d[sp] > current_max:
            current_max = d[sp]
            max_key = sp
    return (max_key, current_max)

def subset_sum_dynamic(numbers, target):
    sp = [[False for j in range(target + 1)] for i in range(len(numbers) + 1)]
    d = {}
    for i in range(len(numbers) + 1):
        sp[i][0] = True
    for i in range(1, len(numbers) + 1):
        for j in range(1, target + 1):
            if numbers[i - 1] > j:
                sp[i][j] = sp[i - 1][j]
                if sp[i - 1][j]:
                    d[i, j] = ((i - 1, j), False)
            else:
                sp[i][j] = sp[i - 1][j] or sp[i - 1][j - numbers[i - 1]]
                if sp[i - 1][j]:
                    d[i, j] = ((i - 1, j), False)
                elif sp[i - 1][j - numbers[i - 1]]:
                    d[i, j] = ((i - 1, j - numbers[i - 1]), True)
    return sp[len(numbers)][target]

def recover_solution(d, numbers, t):
    L = []
    i, j = len(numbers), t
    while i > 0 and j > 0:
        info = d[(i,j)]
        if info[1]:
            L.append(numbers[i-1])
        i, j = info[0][0], info[0][1]
    return L


def subset_sum_top_down(numbers, target):
    sp = {}
    for i in range(len(numbers) + 1):
        sp[(i,0)] = True
    for i in range(target + 1):
        sp[(0,i)] = i == 0
    top_down_aux(numbers, len(numbers), target, sp)
    #return sp[(len(numbers),target)]
    return sp

def top_down_aux(numbers, i, j, sp):
    if numbers[i - 1] > j:
        if not (i - 1, j) in sp:
            top_down_aux(numbers, i - 1, j, sp)
        sp[(i, j)] = sp[(i - 1, j)]
    else:
        if not (i - 1, j) in sp:
            top_down_aux(numbers, i - 1, j, sp)
        if not (i - 1, j - numbers[i - 1]) in sp:
            top_down_aux(numbers, i - 1, j - numbers[i - 1], sp)
        sp[(i, j)] = sp[(i - 1, j)] or sp[(i - 1, j - numbers[i - 1])]

def recover_subset_recur(numbers, target, sp):
    i, j = len(numbers), target
    subset = []
    while i > 0 and j > 0:
        if sp[(i, j)] == sp[(i - 1, j)]:
            i -= 1
        else:
            subset.append(numbers[i - 1])
            i -= 1
            j -= numbers[i]
    subset.reverse()
    return subset if sp[(len(numbers), target)] else None


def create_random_list(length, max_value):
    L = []
    for _ in range(length):
        L.append(random.randint(0, max_value))
    return L

def experiment(n, m):
    total_top = 0
    total_bot = 0
    for _ in range(m):
        L = create_random_list(n, n)
        target = random.randint(1,n*50)

        start = timeit.default_timer()
        subset_sum_dynamic(L, target)
        end = timeit.default_timer()
        total_bot += end - start

        start = timeit.default_timer()
        subset_sum_top_down(L, target)
        end = timeit.default_timer()
        total_top += end - start

    return (total_top/total_bot)

"""
def experiment(n, m):
    total_top = 0
    total_bot = 0
    for _ in range(m):
        L = create_random_list(n, n)
        target = random.randint(1,n**2)

        start = timeit.default_timer()
        subset_sum_dynamic(L, target)
        end = timeit.default_timer()
        total_top += end - start

        start = timeit.default_timer()
        subset_sum_bottom_up(L, target)
        end = timeit.default_timer()
        total_bot += end - start

    return (total_top/total_bot)


def subset_sum(numbers, target):
    if target == 0:
        return True
    if target < 0:
        return False
    if numbers == []:
        return False
    return subset_sum(numbers[:-1], target) or subset_sum(numbers[:-1], target - numbers[-1])

def subset_sum_dynamic(numbers, target):
    sp = [[False for j in range(target+1)] for i in range(len(numbers) + 1)]
    for i in range(len(numbers) + 1):
        sp[i][0] = True
    for i in range(1,len(numbers) + 1):
        for j in range(1,target+1):
            if numbers[i-1] > j:
                sp[i][j] = sp[i-1][j]
            else:
                sp[i][j] = sp[i-1][j] or sp[i-1][j - numbers[i-1]]
    print(len(sp) * len(sp[0]))
    return sp[len(numbers)][target]

def subset_sum_top_down(numbers, target):
    sp = {}
    for i in range(len(numbers) + 1):
        sp[(i,0)] = True
    for i in range(target + 1):
        sp[(0,i)] = i == 0
    top_down_aux(numbers, len(numbers), target, sp)
    print(len(sp))
    return sp[(len(numbers),target)]

def top_down_aux(numbers, i, j, sp):
    if numbers[i-1] > j:
        if not (i-1,j) in sp:
            top_down_aux(numbers, i - 1, j, sp)
        sp[(i,j)] = sp[(i-1, j)]
    else:
        if not (i-1,j) in sp:
            top_down_aux(numbers, i - 1, j, sp)
        if not (i - 1, j-numbers[i-1]) in sp:
            top_down_aux(numbers, i - 1, j - numbers[i - 1], sp)
        sp[(i,j)] = sp[(i-1, j)] or sp[(i-1, j-numbers[i-1])]

def subset_sum_dynamic(numbers, target):
    sp = [[False for j in range(target+1)] for i in range(len(numbers) + 1)]
    d = {}
    for i in range(len(numbers) + 1):
        sp[i][0] = True
    for i in range(1, len(numbers) + 1):
        for j in range(1, target + 1):
            if numbers[i - 1] > j:
                sp[i][j] = sp[i - 1][j]
                if sp[i - 1][j]:
                    d[i, j] = ((i - 1, j), False)
            else:
                sp[i][j] = sp[i - 1][j] or sp[i - 1][j - numbers[i - 1]]
                if sp[i - 1][j]:
                    d[i,j] = ((i-1, j), False)
                elif sp[i - 1][j - numbers[i - 1]]:
                    d[i,j] = ((i-1, j - numbers[i-1]), True)
    if sp[len(numbers)][target]:
        print(recover_solution(d, numbers, target))
    return sp[len(numbers)][target]

"""