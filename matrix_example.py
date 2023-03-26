matrix_5x5 = [[1, 3, 4, 6, 7],
              [2, 4, 6, 8, 9],
              [3, 4, 6, 9, 11],
              [4, 5, 1, 2, 9],
              [5, 7, 12, 4, 3]]
row = [column[4] for column in matrix_5x5]
row1 = {}
for column in matrix_5x5:
    row1[column[0]] = column[3]
print(row1)