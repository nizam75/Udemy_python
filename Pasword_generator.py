import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = int(input("Howmany letters you wants"))
nr_symbols = int(input("Howmany symbols you wants"))
nr_numbers = int(input("Howmany numbers you wants"))

password_list = []
for letter in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
  password_list.append(random.choice(symbols))
for number in range(1, nr_numbers + 1):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)
#print(password_list)
password = ""
for char in password_list:
  password += char
print(f"yor password is: {password}")
