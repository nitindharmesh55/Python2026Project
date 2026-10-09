import numpy as np;

arr = np.array(42);
print(arr)

# 1D Array:
arr1 = np.array([1,2,3,4,5,6]);
print(arr1)


# 2D Array;
arr2 =  np.array([[1,2,3], [4, 5, 6]])
print(arr2);


# 3D Array;

arr3 =  np.array([[[1,2,3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print("Love");
print(arr3)


# Dimensions;
print(arr.ndim);

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)


# Defining the array of dimensions;

arr4 =  np.array([1,2,3,4], ndmin = 5);
print(arr4)


# Accessing the Array Element;s

print(arr1[0]);


print(arr1[1] + arr1[2]);


# Accessing the 2D Arrays;
print('2nd Element on 1st row: ', arr2[0, 1]);
print('5th element on 2nd row: ', arr2[1, 2])

# Accessing 3D Array;

print(arr3[0, 1, 2]);



# Negative Indexing;
arr22 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print("Last Element frrom 2nd dim", arr22[1, -4]);



# Slicing: 

# [Start: End];

# [Start: End: Step]



arraysl =  np.array([1, 2, 3, 4, 5, 6, 7])

print(arraysl[1: 5])

print(arraysl[:4])

# Negative Slicing 

print(arraysl[-3:-1]);


# Steps:

print(arraysl[1:5:2]);

print(arraysl[2::2])



# Slicing 2D Arrays;

arr2L = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr2L[1, 1:5])
print(arr2L[0:2, 2])

print(arr2L[0:2, 1:4]);


# ArraysL
print(arraysl[1:4:2]);





# New topic;

a =  np.array([1, 2 , 3, 4]);
print(a.dtype);

b = np.array(["Apple", "Banana", "Cherry"]);
print(b.dtype);


# Converting number to string;

c =  np.array ([1, 2 , 3, 4], dtype='S')
print(c.dtype)


# Create an array with data type 4 byte integer;
d =  np.array([1, 2, 3, 4], dtype='i4');
print(d);
print(d.dtype)

e = np.array([1.1, 2.1, 3.1])

newarr = e.astype('f')

print(newarr)
print(newarr.dtype)



f = np.array([1, 0, 3])

fs = arr.astype(bool)

print(fs)
print(fs.dtype)


acc= np.array([1, 2, 3, 4, 5])
x = acc.copy()
acc[0] = 42

print(acc)
print(x)