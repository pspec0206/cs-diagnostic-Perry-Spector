import random
def rollDie(n):
  randomRoll = random.randrange(0, n + 1)
  return randomRoll

def main():
  numberOfSides = input("Number of sides?")
  
  while numberOfSides != "":
    numberOfSides = int(numberOfSides)
    result = rollDie(numberOfSides)
    print(result)

    numberOfSides = input("Play again!?!?")

main()
  
