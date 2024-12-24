print("Pls, enter 2 numbers")
print("Enter first number:", end = "")
n1 = input()
print("Enter second number: ", end = "")
n2 = input()

result = [
    "Numbers are not equal",
    "Numbers are equal",
]

index = (n1 == n2)*1

print(result[index])