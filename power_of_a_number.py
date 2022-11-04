def pow(n, p): # positive power only
    ans = 1
    # for i in range(p): # time complexity -> O(n)
    #     ans *= n
    while p > 0: # time complexity -> O(logp)
        last_bit = p & 1
        if last_bit == 1:
            ans *= n
        n *= n
        p = p >> 1

    return ans
print(pow(2, 5))

# def myPow(self, x: float, n: int) -> float: positive and negative power
#         m = n
#         n = abs(n)
#         ans = 1.0

#         while n:
#             last_bit = n & 1
#             if last_bit:
#                 ans *= x
#             x *= x
#             n = n >> 1

#         return ans if m >= 0 else 1/ans