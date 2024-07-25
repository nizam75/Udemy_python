def intro(name, age):
    print(f'Hi {name}\n')
    print(f'Your age is: {age}')

name = input("Enter your Name:  ")
age =  int(input("Enter your age:  "))
intro(name, age)
if(age>=18):
    print("You can Vote")
else:
    print("You can not vote")