# Reflection
# 1. The most surprising thing about lists in Python is how easy it is to
# change them by adding, removing, or sorting items. I expected that changing
# a list would take more steps, but Python has built-in methods that make it simple.
#
# 2. At my ice cream job, a Python list could have been useful for keeping
# track of daily sales amounts. Instead of manually comparing the numbers in
# Excel, I could use a list to quickly find the total, average, best, and worst sales days.


# EXERCISE 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# EXERCISE 2
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])


# EXERCISE 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# EXERCISE 4
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# EXERCISE 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("TypeError caught. Tuples are useful for coordinates because they cannot be changed.")

print(coords)


# EXERCISE 6
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))


# EXERCISE 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = price * 0.90
    discounted.append(round(new_price, 2))

print("Original:", prices)
print("Discounted:", discounted)


# EXERCISE 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))

average_high_sales = sum(high_sales) / len(high_sales)
print("Average:", round(average_high_sales, 2))