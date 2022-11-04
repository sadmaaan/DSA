# root = 0.5 * (x + (n / x)), x -> initial guess
def newton_sqrt(n):
    x = n

    while True:
        root = 0.5 * (x + (n / x))
        if abs(root - x) < 0.001:
            break
        x = root

    return root

print(newton_sqrt(40))