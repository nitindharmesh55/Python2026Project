# If you don't provide any argument to the range you will get the typeError;
# Range only accept integer not float;

# If you want to create negative sequance of number then use negative steps strat from the big number and goes to 0;

for nnum in range(40, 0, -10):
    print(nnum);


numbers = list(range(0 , 10, 2))
print(numbers)



for i in range(10):
    for j in range(i):
        print(j * "*")


# Number Triangle;

for i in range(1 , 6):
    print( i*i)




# Enumerate ans zip function:

language = ["Spanish", "English", "Russian", "Hindi"];
index = 0;

for languages in language:
    print(f"index:{index} and language:{languages}")
    index += 1



# Enumerate() Keep track of the index return an object
print(list(enumerate(language)))



for index ,  Lime in enumerate(language):
    print(f"index {index} and Languages {Lime}")


# Emurate() also take starting part as well;


developers = ["Naomi" , "Dario", "Jessica", "Tom"]
ids = [1 , 2 , 3, 4]

print(list(zip(developers, ids)));




even_numbers = []
for num in range(21):
    if num % 2  == 0:
        even_numbers.append(num)

print(even_numbers)



Even_numbers = [num for num in range(21) if num % 2 == 0]
print(Even_numbers)


# Comprehansive numbers;
numberss = [*range(6)]
result = [(num, "Even") if num % 2 == 0 else(num , "odd") for num in numberss]
print(result)


# Filter(): Select element from an iterable that meet the specific condition;

fruits = ["apple", "banana"]

for index, value in enumerate(fruits):
    print(index, value)

names = ["Nitin", "Raj"]
scores = [90, 80]

print(list(zip(names, scores)))



# New 

letters = ["a", "b", "c"]

for index, value in enumerate(letters, start=1):
    print(index, value)




#filter :selecct the element that specify the condition;

words = ["tree" , "Sky" , "mountain" , "river", "cloud"]; 

def is_long_word(words):
    return len(words) > 4

long_Words =  list(filter(is_long_word, words));
print(long_Words)

# Filter needs a function as a argumnet;


celsius = [0 , 10, 20, 30, 40]
def to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

fahrenheit =  list(map(to_fahrenheit, celsius))
print(fahrenheit);



# Sum function;

numbbbber = [ 5 , 10, 15, 20]
total = sum(numbbbber);
print(total);

names = ["Nitin", "Raj"]

for index, value in enumerate(names, start=1):
    print(index)


a = ["x", "y", "z"]
b = [1, 2, 3]




letters = ["x", "y"]

for index, value in enumerate(letters, start=5):
    print(index, value)



for item in zip(a, b):
    print(item)

letters = ["a", "b"]

print(list(enumerate(letters)))


#lambda function: more line arrow function;

crimme = [x for x in range(10)];
even_nnumber =  list(filter(lambda x: x % 2 == 0, crimme))
print(even_nnumber);