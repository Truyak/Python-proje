def reverse(l):
    l = l[::-1]
    for i in range(1,len(l)+1):
        if type(l[i-1]) == list:
            l[i-1] = l[i-1][::-1]
    return l
l = eval(input())
print(reverse(l))
