hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
for price in prices:
  total_price += price
print(total_price)
average_price = total_price / len(prices)
print("Average Haircut Price:")
print(average_price)
# New Price
new_prices = [num - 5 for num in prices]
print(new_prices)
#Task 7
total_revenue = 0
for i in range(0, len(hairstyles)):
  print(i)
  total_revenue += (prices[i] * last_week[i])

print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7
print("Average Daily Total:" + str(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)-1) if new_prices[i] < 30]

print("Cuts Under $30:" + str(cuts_under_30))
