print("Enter the price of oroduct that you bought: ", end = "")
productPrice = float(input())

print("How many products did u buy: ", end = "")
productNumber = int(input())


print("Enter discount: ", end = "")
discount = int(input())

discPrice = productPrice - (productPrice*(discount/100))
num = discPrice * productNumber

print(num)

