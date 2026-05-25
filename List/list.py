# Lists are mutable and zero index based;
# Example:
cities = ['Los Angeles','London', 'Tokyo'];
cities[0] = 'New York'
cities[-1] #'Tokyo';

# Another Way to create a list using list() constructor;
developer = "Nitin-Rajdharmesh"
list(developer) # ['N', 'i', 't', 'i', 'n', '-', 'R', 'a', 'j', 'd', 'h', 'a', 'r', 'm', 'e', 's', 'h']

# Length of the List:
len(developer) # 16


# Updating particular point in the list ;
cities[1] = 'Japan'
print(cities) 


# If you beyond the range of the list 
# You will get the indexError

# If you want to remove the element from the list you can use the del keyword;

fruits = ['Apple', 'Banana', 'Cherry', 'Date']
del fruits[1]
print(fruits) # ['Apple', 'Cherry', 'Date']

# To check something in the list use {in} keyword;
print("Apple" in fruits)

# Nested List;
matrix = [1,2,3,[4,5,6],7,8,9];
print(matrix[3][1]) #Accessing the list inside the list;

#List unpacking:
front_end = ['Nitin', 23, 'Front-end Developer']

name , age , role  = front_end
print(name)
print(age)
print(role);

# If you need other info from the list you can use the *;
name , *rest = front_end
print(rest);

# If the number of variables is less than the number of value from the list then u will get the value error from the python;


# Slicing;
numbers = [1,2,3,4,5,6,7,8,9]
numbers[2:5] # [3,4,5]
evenNumbers = numbers[1::2]
print(evenNumbers) # [2,4,6,8]


# Common Methods for the List;

# Append(): used to add item at the end of the list;
numbers.append(10)
# If you want to add a list at the end of the list;

numbers.append([11,12,13])
#  but it will be the nested list not induvidual elements;

# To add the induvidual element of the list you can use the extend() method;
numbers.extend([11,12,13])
print(numbers) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12, 13], 11, 12, 13]


# Adding an element at the specific index ;
numbers.insert(1,25)
print(numbers) # [1, 25, 2, 3, 4, 5, 6, 7, 8, 9, 10, [11, 12, 13], 11, 12, 13]


# if you want to remove the element from the list u can use the remove()
numbers.remove(25)
# It  will only remove the first occurrence of the element from the list;;

# Remove an element at pecific index;
numbers.pop(1) # it will remove the element at index 1 and return the value of the removed element;

# if you don't specify the index in the pop() it will remove the last element;


# If you want to empty the list ;
numbers.clear()
print(numbers) # [];


# Sort() it will sort the list ;

numbers = [5,2,9,1,5,6];
numbers.sort();
print(numbers) # [1, 2, 5, 5, 6, 9];

# Sort() will modify the orginal list;
# Sorted() wil return new sorted list;
crime = [19,2,35,1,67,41];
crime_numbers = sorted(crime);
print(crime_numbers);



# To Reverse the List:
numbers.reverse();


# To find the index of the specific element;

programming_languages = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby']
print(programming_languages.index('Java')) # 2

# If  it can' be found then it will show value error;

