print("Enter ur name and surename: ", end = "")
name = input()
print("Surename:" , end = "")
surename = input()

print("Variant: ", end = "")
print(name + surename, end = ", ")
print(surename + name, end = ", ")
print(name.lower() + surename.lower() , end = ", ")
print(surename.lower() + name.lower())