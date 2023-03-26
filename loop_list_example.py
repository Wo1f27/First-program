def loop_list(L:list):
    L.append(L)
    return L


L = list()
L = [1, 6]
print(loop_list(L))
