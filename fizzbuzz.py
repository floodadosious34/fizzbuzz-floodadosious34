# add your code here
userNumber = int(input("Please enter a number: "))

if userNumber % 3 == 0 and userNumber % 5 ==0:
    print("FizzBuzz")
elif userNumber % 3 == 0:
    print("Fizz")
elif userNumber % 5 == 0:
    print("Buzz")
else:
    print(userNumber, "is not Fizz or Buzz")
