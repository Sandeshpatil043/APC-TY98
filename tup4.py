colors = ("red", "blue", "green", "yellow", "black")

color = input("Enter color: ").lower()

if color in colors:
    print("Color exists")
else:
    print("Color does not exist")