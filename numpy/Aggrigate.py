import numpy as np;


array1 =  np.array([[1, 2, 3, 4, 5], [6 , 7 , 8 , 9 , 10]])
array2 =  np.array([[1], [2]])

print(array1.shape);
print(array2.shape)

array3 =  array1 +  array2;
print(array3)
print(np.sum(array3));
print(np.mean(array3))
print(np.std(array3))
print(np.argmin(array3))
print(np.argmax(array3))



# Selecting Axis;

print(np.sum(array3, axis=0))
print(np.sum(array3, axis = 1))