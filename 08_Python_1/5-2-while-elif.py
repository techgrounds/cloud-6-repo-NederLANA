i=100
while i:
    num = int(input("Guess what number I'm thinking of?  "))
    if num < i:
        print("Wrong! " +str(num) +" is too low. Try again.")
        print()
    elif num > i:
        print("Nope! " +str(num) +" is too high. Guess again.")
        print()
    else:
        print("Wow! I was totally thinking " +str(num) +" too. Mind blown....")
        print()
        break 