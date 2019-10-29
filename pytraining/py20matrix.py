matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)
print()

matrix[1][1] = 'x'  # update an element
print(matrix)
print()

matrix[2].append(10)  #append an element to a row
print(matrix)
print()

matrix[2].pop()  # delete an element from a row
print(matrix)
print()

matrix.insert(2, [10, 11, 12])  # add a row
print(matrix)
print()

# iterating over all the elements
for row in matrix:
    for col in row:
        print(col, end='\t')
    print()
