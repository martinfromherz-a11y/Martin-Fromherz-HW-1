def calculate_cost(consumption_kwh, price_per_kwh):
    return consumption_kwh * price_per_kwh


## Calculate total electricity cost
## consumption_kwh: Energy consumed in kWh
## price_per_kwh: Price per kWh in EUR
##return: Total cost in EUR


def calculate_revenue(production_kwh, market_price):
    return production_kwh * market_price

    ##Calculate revenue from selling electricity.
    ## roduction_kwh: Energy produced in kWh
    ## market_price: Selling price per kWh in EUR
    ## return: Revenue in EUR


def calculate_profit(revenue, cost):
    return revenue - cost

    ## Calculate net profit.
    ## revenue: Total revenue in EUR
    ## cost: Total cost in EUR
    ## return: Net profit in EUR


if __name__ == "__main__":
    consumption = 3500
    production = 7000
    price_buy = 0.20
    price_sell = 0.12

    cost = calculate_cost(consumption, price_buy)
    revenue = calculate_revenue(production, price_sell)
    profit = calculate_profit(revenue, cost)

    print(f"Cost: €{cost:.2f}")
    print(f"Revenue: €{revenue:.2f}")
    print(f"Profit: €{profit:.2f}")

#########################################################################################################