# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. 
# Return the total profit made, rounded to the nearest dollar.

cost_per_unit = 15
price_per_unit = 34
inventory = 487

def calculate_profit(cost, price, inv):
    net_profit_per_unit = price - cost
    net_profit = inv * net_profit_per_unit
    return net_profit

total_profit_made = calculate_profit(15, 34, 487)

print(f"You've made a total of {total_profit_made} dollars")
     