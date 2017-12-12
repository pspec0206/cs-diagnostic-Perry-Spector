def fibonacci_iterative(num):
  num1, num2 = 0, 1
  for number in range(0, num):
    num1, num2 = num2, num1 + num2
    print(num2)


def factorial_recursive(num):
  finalNumber = 1
  while num >= 1:
    finalNumber *= num
    num -= 1
  print(finalNumber)


def main():
  
  userNumber = int(input("Whats ur number?"))
  if userNumber == "":
    userNumber = 10
  fibonacci_iterative(userNumber)
  print("\n")
  
  print("Factorial Recursion: ")
  factorial_recursive(userNumber)


main()
