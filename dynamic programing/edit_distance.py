# Uses python3
def edit_distance(s, t, memo={}):
    #write your code here
    if (len(s),len(t)) in memo: return memo[(len(s),len(t))]
    if len(s)==0: return len(t)
    elif len(t)==0: return len(s)
    else:
        diff = int(s[-1]!=t[-1])
    memo[(len(s),len(t))] = min(edit_distance(s,t[:-1],memo)+1,edit_distance(s[:-1],t,memo)+1,edit_distance(s[:-1],t[:-1],memo)+diff)
    return memo[(len(s),len(t))]
print(edit_distance(input(), input()))
