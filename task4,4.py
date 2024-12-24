print("Enter 2 sentenses!")
print("1: ", end = "")
w1 = input()
print("2: ", end = "")
w2 = input()

info = [
    "Not the same",
    "The same",
]

index = (w1 is w2)*1

print(info[index])

