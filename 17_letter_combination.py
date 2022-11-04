def combination(str_after, str_main):
    if len(str_main) == 0:
        print(str_after)
        return
    
    digit = int(str_main[0])
    for i in range((digit-1)*3, digit*3, 1):
        ch = ord('a') + (i % 26)
        combination(str_after + chr(ch), str_main[1:])


combination("", "12")