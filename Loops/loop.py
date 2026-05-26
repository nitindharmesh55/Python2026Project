# Loops used to repeat block of code;
programming_languages =  ["rust" , "Java", "python", "C++"]

for languages in programming_languages:
    print(languages)


# For Strings;
code = "Happy Coding"
for char in code:
    print(char)



# Nested for Loops;

categories = ["fruites" , "Vegetable"];
foods = ["Apple","Carrot", "Banana"]

for category in categories:
    for food in foods:
        print(category, food)



# WhileLoops :
# Repeat the code untill the condition become false;

secret_number = 3;
guess = 0
while guess != secret_number:
    guess = int(input("Gess the number(1-5): "))
    if guess != secret_number:
        print("Wrong! Try Again")
print("You got it!")


# Break will stop the execution of a loop;

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)


# Continue: Skipp the iteration ;

developer_namess =  ["jess" , "Naomi" , "Tom"]

for developer in developer_namess:
    if developer == "Naomi":
        continue
    print(developer);


# For while and elese ;
words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in "aioue":
            print(f"{word} contain letter {letter}")
            break
    else:
        print(f"{word} has no vowel")





for i in [1 ,2]:
    for j in [ 3 , 4]:
        print(i , j)








# Range in Loops:

#Generate sequance of integer;
# range(strt, stop , step);

for num in range(0 , 10, 2):
    print(num)


vart = range(0 , 3);
for i in vart:
    print(i);