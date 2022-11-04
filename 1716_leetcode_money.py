def totalMoney(n):
    total_money = 0
    count = 0
    temp = 1

    for i in range(1, n // 7 + 2):
        while count <= n:
            total_money += (temp % 8) * i
            if temp != 1 and temp % 7 == 1:
                temp = 1
            count += 1
            temp += 1

        return total_money

print(totalMoney(20))