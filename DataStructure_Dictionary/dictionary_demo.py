animals = {
    "cow":"moo",
    "chicken":"cluck",
    "horse":"neigh",
    "pig":"oink"
}

choice=input("Choose an animal.")

if choice in animals:
    print(animals[choice] + " " + animals[choice])
else:
    print("E-I-E-I-O")