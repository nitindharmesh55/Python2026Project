def number_pattern(n):
    numbers = ""
    for nums in range(1 , n+1):
        numbers += str(nums) + " "
    return numbers


print(number_pattern(4))


# str = "Hello word"
# line = str.split()
# print(line)

def not_string(str):
  line = str.split()
  for word in line:
    if word.lower() == 'not':
      return str
    else:
      return "not" +" "+ word

print(not_string("is not"))



sttr = "Hello"


lime =  list(sttr)
lime[-1], lime[0] = lime[0] , lime[-1]
newtt = "".join(lime)
print(newtt)


def string_splosion(str):
  newStrirng = ""
  for lime in str:
    newString += lime
  return newStrirng 

print(string_splosion("Nitin"))