print("Pls, enter 2 numbers")
print("Enter first number:", end = "")
n1 = input()
print("Enter second number: ", end = "")
n2 = input()

result = [
    "First number is bigger than second number and they are not equal",
    "Numbers are equal",
    "First number isn't bigger than second one",
]

index = (n1 == n2) + (n1 < n2) *2

print(result[index])


