import numpy as nd;

array = nd.array([1,2,3,4]);
print(array)



array1 = nd.array(['A'])
print(array1)

array01 = nd.array([[['A', 'B', 'C'], ['D', 'F', 'N'], ['G', 'H', "O"]], [['A', 'B', 'C'], ['D', 'F', 'N'], ['G', 'H', "O"]], [['A', 'B', 'C'], ['D', 'F', 'N'], ['G', 'H', "O"]]]);
print(array01.shape) 
print(array01[0][0][1])


array2d = nd.array([[1,2,3,4],
                             [5, 6, 7, 8],
                             [9, 10, 11, 12]])

print(array2d[0: :2]);
print('\n');
print(array2d[0:, :: -2])

print("Nitin")
print(array2d[1:, 1:3])