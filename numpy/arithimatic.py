import numpy as np;


array = np.array([1, 2 , 3])

print(array + 1);
print(array - 1)
print(array * 2)
print(array / 2);
print(array % 10)

print(array ** 5);



# Verctorized Math;

array1 =  np.array([1, 2, 3]);

print(np.sqrt(array1));
print(np.round(array1));
print(np.ceil(array1));
# print(np.pi(array1))



radius  = np.array([1, 2 , 3])
print(np.pi * radius ** 2)


# Element wise Arrithimatic
element  = np.array([1 , 2 , 3])
element1 =  np.array([4 , 5 ,6])
print(element + element1)
print(element - element1)
print(element *  element1)
print(element / element1)
print(element ** element1)


# Comparision operator;

scores =  np.array([91, 55 , 100, 73, 82, 64])

scores[scores < 60] = 0
print(scores);