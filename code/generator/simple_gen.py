from typing import List


def fib(n: int) -> List[int]:
    numbers = []
    current, nxt = 0, 1
    while len(numbers) < n:
        current, nxt = nxt, current + nxt
        numbers.append(current)

    return numbers


# TODO: Try it with generators!


result = fib(50)

for n in result:
    print(n, end=', ')
    if n > 10000:
        break

print()
print("Done")
