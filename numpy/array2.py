import numpy as np;

a = np.array([
    [75, 60, 82, 80],
    [90, 73, 75, 85],
    [82, 92, 80, 63]
])

# priiting the highest value of the array;
print(a.max());



# Highest Value from ech subjects
print(np.max(a, axis = 0)); 


# Sum of the highest marks of the student 1;
sumOfStudent =  np.sum(a, axis = 1);
print(sumOfStudent[0])



# Creating Student marks:

Students = np.array([
  [0, 12 , 13, 10, 3, 6, 0, 0, 0, 0, 0, 8, 4, 0, 14, 0, 7, 29, 0, 5],
  [9, 3, 0, 10, 0 , 10, 0 , 0 , 0 , 0 , 0, 0, 2 , 0, 18 , 0, 9 , 30, 13 ,4]
])

# Sum of the first Test:
total  = np.sum(Students, axis = 0)
percentage  =  (total / 60) * 100;

# Sort the student by theri percentage ;

sortedArray = np.argsort(percentage)
print(sortedArray)

topThree =  sortedArray[-3 : ][::-1];
print(topThree);

for name in topThree:
    print(f'Roll Number Of Three Top Student {name + 1}: {percentage[name]:.2f}\n');
