def maxProfitPeakValley(prices):
    is_buy = True
    to_sell = None
    income = []

    for i in range(len(prices)):
        current = prices[i]
        next = prices[i + 1] if i + 1 < len(prices) else 0

        if is_buy:
            if current > next:
                continue

            to_sell = current
            is_buy = False
            continue

        if current < next: # sell
            continue

        income.append(current - to_sell)
        to_sell = None
        is_buy = True

    return sum(income)

def maxProfit(prices):
    profit = 0

    for i in range(len(prices) - 1):
        current = prices[i]
        next = prices[i+1]

        if current < next:
            profit += next - current

    return profit

result = maxProfit([7,1,5,3,6,4])

print(result)