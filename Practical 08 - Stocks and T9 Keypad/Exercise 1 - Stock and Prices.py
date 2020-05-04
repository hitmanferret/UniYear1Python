stock = {
    "banana":6,
    "apple":0,
    "orange":32,
    "pear":15
}

prices = {
    "banana":40,
    "apple":20,
    "orange":15,
    "pear":30
}

basket_1 = {
    "banana":4,
    "pear":3
}

basket_2 = {
    "apple":1,
    "pear":3
}

##def basket_price(basket, stock, prices):
##    total_cost = 0
##    for key1,val1 in basket.items():
##        if val1 <= stock[key1]:
##            cost = val1*(prices[key1])
##            total_cost += cost
##            stock[key1] = (stock[key1]-val1)
##        else:
##            return -1
##    return total_cost
##
##cost = basket_price(basket_1, stock, prices)
##print(cost)
##print(stock)



##def add_stock(items, stock):
##    for key2,val2 in items.items():
##        stock.update({key2:val2})
##    return stock
##
##stock = add_stock({"apple":5, "kiwi":10}, stock)
##print(stock)



def price_increase(increase, prices):
    for key, val in prices.items():
        prices[key] = val * (1 + increase)
    return prices

new_prices = price_increase(0.2, prices)
print(new_prices)






