import timeit

runs = 1000000
total_time = 0
for _ in range(runs):
    start = timeit.default_timer() # these are laptop dependent, i.e. better computers will do better than my laptop
    n = 0
    for i in range(10):
        n += i
    end = timeit.default_timer()
    total_time += end - start

print(total_time/runs)

# in general the more tests you do, the more precise answer you are going to get