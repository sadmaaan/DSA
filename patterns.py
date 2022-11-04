def pattern7(n):
    for i in range(0, n):
        for j in range(0, n-i):
            print("* ", end="")
        print("\r")



print(pattern7(5))