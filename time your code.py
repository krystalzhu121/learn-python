from timeit import timeit

code1 = """

def indexsearching(numbs, target):
    for i in range(len(numbs)):
        for j in range(i+1, len(numbs)):
            if numbs[i]+numbs[j] == target:
                return (i, j)
    return "not find"


indexsearching([3, 2, 4], 6)
"""

print(timeit(code1, number=100000))
