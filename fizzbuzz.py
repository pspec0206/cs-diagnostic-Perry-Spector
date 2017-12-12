'''
1. Enter min Input
2. Enter max Input
3. Make a loop that prints each value between the min and max
4. In the loop, if a number is divisible by 3, print the word fizz
  instead of the actual value
5. In the loop, if a number is divisible by 5, print the word buzz
  instead of the actual value
6. In the loop, if a number is divisible by both 3 and 5, print the
  word fizzbuzz instead of the actual value
'''

def fizzbuzz(minimum, maximum):
  for num in range(minimum, maximum):
    if (num % 3 == 0 and num % 5 == 0 and num != 0):
      print("FIZZBUZZ")
    elif (num % 3 == 0 and num != 0):
      print("fizz")
    elif (num % 5 == 0 and num != 0):
      print("buzz")
    else:
      print(num)

def main():
  start = int(input("What is the minimum number"))
  end = int(input("What is the maximum number"))
  fizzbuzz(start, end + 1)

main()
