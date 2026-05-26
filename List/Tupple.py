programming_languages = ('python', 'Javascript', 'java', 'C++')
# programming_languages[0] = "Javascript" # typeError

# To Access the value from the tupple;
print(programming_languages[1])
# To Access the last value you can use the negative index;
print(programming_languages[-1])

# Count(); how many time a specific item appeared in tupple;
print(programming_languages.count("Java"))

# if no argument passed into the count it will show you typeerror;


# Index(); find the index of item;
print(programming_languages.index("python"))

# index start where to start searching;

# programming_languages.index("python", 3) # start searching from 3 index;

# We can also add stop index;
# programming_languages.index("python", 2, 5)



# Sorted();
numbers = (13, 2, 78, 3, 45, 67, 18, 7)
print(sorted(numbers))

# Key; 
value = sorted(programming_languages, key=len)
print(value)

# Reverse;
value2 = sorted(programming_languages, reverse=True);
print(value2)