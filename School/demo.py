x = [2, 2, 8, 5, 6, 6]
y = set(x)

def t(L):
    if L in y:
        return 1
    else:
        return 0

# output : 2 2 8 5 6 6 
a = filter(t, x)
for i in a:
    print(i, end=' ')

