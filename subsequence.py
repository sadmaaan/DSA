def subseq(s, s_new, l):
    if len(s) == 0:
        if s_new != '':
            l.append(s_new)
        return
    
    ch = s[0]
    subseq(s[1:], s_new + ch, l)
    subseq(s[1:], s_new, l)

    return l

l = []
subseq("abc", "", l)
print(l)