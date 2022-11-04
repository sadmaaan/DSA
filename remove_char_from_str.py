def remove_char(s, s_ans):
    if len(s) == 0:
        print(s_ans)
        return
    
    ch = s[0]
    if ch == 'a':
        remove_char(s[1:] ,s_ans)
    else:
        remove_char(s[1:], s_ans + ch)

def remove_char2(s):
    if len(s) == 0:
        return s
    
    ch = s[0]
    if ch == 'a':
        return remove_char2(s[1:])
    else:
        return ch + remove_char2(s[1:])



s = "abaytshda"
# remove_char(s, "")
print(remove_char2(s))