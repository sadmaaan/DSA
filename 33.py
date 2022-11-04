import re


def search(nums, target):
    s = 0
    e = len(nums) - 1
    while(s<=e):
        mid = s + (e-s // 2)
        if(mid == target):
            return mid
        elif(s < e):
            if(mid < target):
                s = mid + 1
            else:
                e = mid - 1
        elif(s > e):
            if(mid < target):
                e = mid - 1
            else:
                s = mid + 1
print(search([4,5,6,7,0,1,2], 1))
    