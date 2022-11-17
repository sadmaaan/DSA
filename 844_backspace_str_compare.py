def backspaceCompare(s, t):
    s_list = []
    t_list = []

    i = 0
    ls = 0
    lt = 0
    while i < len(s) or i < len(t):
        if ls < len(s):
            if s[ls] != '#':
                s_list.append(s[ls])
                ls += 1
            else:
                del s_list[-1]
                ls += 1
        
        if lt < len(t):
            if t[lt] != '#':
                t_list.append(t[lt])
                lt += 1
            else:
                del t_list[-1]
                lt += 1
        i += 1
    
    return s_list, t_list

print(backspaceCompare("a#c", "b"))
            
            
