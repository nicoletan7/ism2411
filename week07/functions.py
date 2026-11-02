# Self-Assessment

# 1. The first bug I saw in Exercise 5 was that total = sale was
# replacing the total each time instead of adding each sale to the total.
# I found this by looking through the code and using print statements to
# see how the value had changed. This showed me that checking variable values
# can help me figure out mistakes when my code does not give the expected output.

# 2. The apply_discount(price, tier) function takes the original price
# and the customer's tier as inputs. It checks if the tier is gold,
# silver, bronze, or none and applies the correct discount. It returns
# the new price after the discount. A colleague could use the function
# without reading the body as long as they know to enter a price and tier.

# 3. I used ChatGPT to help explain the exercises and
# understand the errors in Exercise 5. It helped my understanding
# by explaining why the errors occurred.


# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate


tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


print(f"gold:   ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none:   ${apply_discount(200, 'none'):.2f}")


# --- Exercise 3 ---

starting_price = 200

discounted_price = apply_discount(starting_price, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

tax = calculate_tax(discounted_price, 0.07)
after_tax = discounted_price + tax
print(f"After tax: ${after_tax:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# --- Exercise 4 ---

orders = [
    (200, "gold"),
    (150, "silver"),
    (80, "bronze"),
    (500, "none")
]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---

sales = [120, 80, 250, 175, 90]

# Bug 1: total = sale replaced the total each time instead of adding to it.
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Bug 2: The for loop was missing a colon at the end.
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Bug 3: Using <= made the loop try to access an index that does not exist.
# Using < stops the loop before it goes past the end of the list.
i = 0
while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---

x = 100   # global variable


def double_it():
    x = 999   # local variable
    return x * 2


print(x)
print(double_it())
print(x)

# Scope explanation:
# The x outside of the function is a global variable and has a value of 100.
# The x inside double_it() is a local variable and only exists inside that
# function. Changing x inside the function does not change the global x.
# Therefore, the first print gives 100, double_it() gives 1998, and the
# final print still gives 100.