stock = {'apple': 5, 'banana':10, 'orange':7}
print(f"The current stock is {stock}")

for key, val in stock.items():
    if len(stock[val])==6:
        stock[key] = 2*stock[key] 
print(stock)
