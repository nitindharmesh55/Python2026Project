# String Mathods;

name =  input("Enter Your Full Name: ");

result =  len(name);
print(result);

# Find first occurence of given character 

occurence =  name.rfind(" ");
print(occurence);

# Capitalize;
cap =  name.capitalize();
print(cap);

# UpperCase
upper = name.upper();
print(upper);

# LowerCase
lower =  name.lower();
print(lower);

# Isdigit  return boolean is string contain any number or integer;

isDigit =  name.isdigit();

print(isDigit);

# isalpha ; boolean if string contain alphabatic character;

alpha = name.isalpha();

print(alpha);



phone =  input("Enter Your number: ");

dash =  phone.count("-");
# count method lets you count the chracter;

print(dash);



rep = phone.replace("-", "%");

print(rep);

# print(help(str));



# Validate User;
# 1. Username is no more than 12 character;
# 2. Username must not contain space;
# 3. UserName must not contain digits;

username =  input("Enter Your Name: ");

if len(username) > 12:
    print("Your username must 12 character")
elif not username.find(" ") == -1:
    print("your username can't contain space");
elif not username.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {username}");




# 1:39:09