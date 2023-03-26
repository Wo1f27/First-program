def list_indices(number):
    list_with_indices = list()
    for item in range(len(number)):
        list_with_indices.append(item)
    return list_with_indices


print(list_indices([8, 19, 45, 76, 900]))
