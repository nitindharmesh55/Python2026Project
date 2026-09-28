weight =  float(input("Enter the Weight:  "));
unit = input("Pound or Kilograms (K or P): ");

if unit == "K":
    kilo =  weight * 2.20
    print(f"Weight in Kilo: {kilo}Kg");
elif unit == "P":
    pound =  weight * 0.45
    print(f"Weight in Pound: {pound}P")