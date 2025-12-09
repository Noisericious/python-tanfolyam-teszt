def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

n = 5
print(f"A számok összege 1-től {n}-ig: {sum_recursive(n)}")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

# van egy tömb, vagy kollekció. végig kell járni, valami miatt. hogyan járnád végig a tömböt ciklus nélkül? rekurzióval, ami ciklusokkal teli fv., így jó válasz nincs.

stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack.pop())
print(stack.pop())
