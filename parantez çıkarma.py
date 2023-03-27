l = eval(input())
print(l[0])
new_list = []
def out_par(l):
    
    for i in range(len(l)):
        if type(l[i]) != list:
            new_list.append(l[i])
        else:
            out_par(l[i])
    return new_list
print(out_par(l))