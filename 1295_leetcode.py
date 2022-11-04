class A:
    def findNumbers(nums):
        count = 0
        for num in nums:
            # if len(str(num)) % 2 == 0:
            #     count += 1
            
            if lengthOfNum(num) % 2 == 0:
                count += 1
                
        return count

    def lengthOfNum(num):
        c = 0
        
        while num > 0:
            c += 1
            num = num / 10
        
        return c

print(A.findNumbers([12,345,2,6,7896]))