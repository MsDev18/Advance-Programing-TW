price = int(input("Enter price: "))

if price > 200:
    discount = 0.20
elif price > 100:
    discount = 0.10
elif price > 50:
    discount = 0.05
else:
    discount = 0.0

finalPrice = price + (price * discount)
print(f"price -> {price} || discount -> {discount} || final price -> {finalPrice}")