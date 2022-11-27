import random

explodingCondition = ""

def explodingFunc():
    global explodingCondition
    explodingCondition = str(input("Is it exploding? (Y/N) "))
    if explodingCondition == "Y":
        explodingCondition = True
    elif explodingCondition == "N":
        explodingCondition = False
    else:
        print("Incorrect command")
        explodingFunc()

continueCheck = "Y"
while continueCheck == "Y":
    finalresult = 0
    numberOfRolls = int(input("Enter number of rolls: "))
    diceType = int(input("Enter dice type: "))
    explodingFunc()
    print("Rolling", numberOfRolls,"D",diceType)
    print("Results:")
    for i in range (numberOfRolls):
        result = random.randrange(1, diceType+1)
        print(result)
        finalresult = finalresult + result
        while result == diceType and explodingCondition:
            result = random.randrange(1, diceType+1)
            print(result)
            finalresult = finalresult + result
    print("Final:", finalresult)
    continueCheck = str(input("Roll again? (""Y"" to continue) "))
