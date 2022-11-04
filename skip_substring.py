def skip(s):
    if len(s) == 0:
        return ""
    
    if s[:5] == 'apple':
        return skip(s[5:])
    else:
        return s[0] + skip(s[1:])

def skip2(s):
    if len(s) == 0:
        return ""
    
    if s[:3] == 'app' and s[:5] != 'apple':
        return skip2(s[3:])
    else:
        return s[0] + skip2(s[1:])



s = "abaytappleshdahjakyuiefnncd" # skip apple
print(skip(s))
print(skip2("xvsapprne")) # skip app when apple is in str, otherwise keep apple