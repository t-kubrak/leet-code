def maxProfit(prices):
    is_buy = True
    to_sell = None
    income = []

    for i in range(len(prices)):
        price = prices[i]
        next_price = prices[i + 1] if i + 1 < len(prices) else 0

        if is_buy:
            if price > next_price:
                continue

            to_sell = price
            is_buy = False
            continue

        if price < next_price:
            continue

        income.append(price - to_sell)
        to_sell = None
        is_buy = True

    return sum(income)

result = maxProfit([7,1,5,3,6,4])

print(result)

