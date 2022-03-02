


userInput = int(input("Please enter a number: "))


if userInput > 1:				#checks if user input is greater than 1, then the for loop checks if the number is divisible by 2
   for i in range(2,userInput):
       if (userInput % i) == 0:
           print("The number,", userInput,"is not a prime number")
           break
   else:
       print("The number,", userInput,"is a prime number")
