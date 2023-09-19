shop1 = {'apple': 10, 'bannana': 12, 'plum': 13, 'kiwi': 14}
shop2 = {'apple': 11, 'bannana': 12, 'plum': 10}
shop3 = {'apple': 15, 'bannana': 7, 'plum': 12}
shops = {'prof': shop1, 'lid': shop2, 'kauf': shop3}

shopping_cart = {'apple': 3, 'bannana': 2, 'plum': 5}


def best_buy(shops: dict, cart: dict) -> str:  # variable number of arguments
    result_per_shop = {}
    result = None
    best_shop_name = None
    for name, shop_products in shops.items():
        print(name, shop_products)
        result_per_shop[name] = 0
        for product, price in shop_products.items():
            print(product, price)
            result_per_shop[name] += cart.get(product, 0) * price
            print(result_per_shop)
    for name, price in result_per_shop.items():
        if result is None:
            result = price
            best_shop_name = name
        elif price < result:
            result = price
            best_shop_name = name

    return best_shop_name

best_shop = best_buy(shops, shopping_cart)
print(best_shop)
