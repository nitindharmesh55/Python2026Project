import math;
friend = 0

friend  =  friend + 1;
friend += 1;

print(friend);



x =  3.14

y = 4

z = 5;

result =  round(x); #nearest integer
result =  abs(y) # absolute value of number;
result = pow(4, 3) #pow(base, exponent);

result = max(x , y, z);
result =  min(x, y, z);


print(math.pi);
print(math.e);

result = math.sqrt(x);
print(round(result));




# Exercie; 

radius = int(input("Enter the Radius of Circle: "));

area =  2 * math.pi * radius;

print(f"Area of circle: {round(area, 2)}cm^2");



# Hypotenious ;

a = float(input("Enter side A: "))
b = float(input("Enter side B: "));

c = round (math.sqrt(pow(a, 2) + pow(b, 2)), 2);

print(f"Hypotenius: {c}");

