## Part 1: Quick Onboarding

### 1. The 5-Minute Setup
* **Immediate Start:** Use a free online compiler like [Replit](https://replit.com/) or Google Colab to run code in seconds.
* **Local Environment:** You have already installed **Python** and **Visual Studio Code (VS Code)**, which is the perfect setup for building local financial models.

### 2. The Best Free Resources
* **Harvard’s CS50P (YouTube/edX):** An incredibly engaging, free introductory course focused entirely on Python.
* **Automate the Boring Stuff with Python:** Focuses strictly on writing practical scripts to automate daily tasks.
* **University of Helsinki’s Python MOOC:** A highly regarded, text-based course with built-in browser practice.

---

## Part 2: The Core Syntax Reference

### 1. Numbers and Basic Math
In finance, you will primarily deal with `int` (whole numbers, like shares) and `float` (decimals, like stock prices). Python handles math intuitively. The exponent operator (`**`) is especially crucial for compound interest and discounting cash flows (like calculating Net Present Value).

```python
shares = 100          # integer
price = 150.25        # float

# Basic Math
total_value = shares * price 
daily_return = (155.0 - price) / price

# Exponents (e.g., compounding 5% over 5 years)
compounded = 1000 * (1.05 ** 5) 
2. Lists
A list is a collection of items in a specific order, perfect for storing time-series data like historical cash flows or a week's worth of closing prices. Python lists are "zero-indexed" (the first item is at position 0).
Python

# A list of 5 daily closing prices
closing_prices = [148.50, 150.00, 151.25, 149.80, 152.10]

# Accessing the first price
monday_price = closing_prices[0]
3. Conditionals (if/elif/else)
Conditionals allow your code to make decisions, which is how you build trading alerts or flag risk metrics (like exceeding a target Loan-to-Value ratio). Python uses indentation (spaces) to group code.
Python

current_price = 145.0
target_buy_price = 150.0

if current_price < target_buy_price:
    print("Buy signal triggered!")
elif current_price == target_buy_price:
    print("Hold and watch.")
else:
    print("Price too high.")
4. Loops (for)
Loops are the workhorse of data analysis. They allow you to iterate through financial data without manually clicking and dragging formulas down a column.
Python

portfolio = [1000, 2000, 1500]
total_value = 0

# This loops three times, adding each asset to the total
for asset in portfolio:
    total_value = total_value + asset

print(total_value) 
5. Dictionaries (Key-Value Pairs)
Dictionaries store data using "keys." They are perfect for mapping a stock ticker to its current price, or assigning actuals and forecasts to specific SaaS expense categories.
Python

# Creating a dictionary of stock tickers and prices
current_prices = {
    "AAPL": 150.00,
    "MSFT": 310.25,
    "TSLA": 215.50
}

# Pulling a specific value using its key
apple_price = current_prices["AAPL"]

# Adding or updating a value
current_prices["NVDA"] = 450.00
6. Functions (def)
Functions bundle code into reusable blocks. Instead of rewriting complex financial formulas over and over, you define the logic once and pass new data into it whenever needed.
Python

# Defining the function
def calculate_position_value(shares, price):
    value = shares * price
    return value

# Using (calling) the function
my_aapl_value = calculate_position_value(50, 150.00)
print(my_aapl_value)  # Outputs 7500.0
Part 3: Your Week 1 Assignments
Open VS Code, create a new file named finance_basics.py, and complete these assignments. Run the file after writing each one.
Assignment 1: The ROI Calculator (Math & Variables)
	1	Create a variable called buy_price and set it to 250.0.
	2	Create a variable called sell_price and set it to 285.5.
	3	Write a formula to calculate the percentage return ((sell - buy) / buy) * 100.
	4	print() the result. It should output 14.2.
Assignment 2: The Stop-Loss Trigger (Lists & Conditionals)
	1	Create a list called portfolio_values with these numbers: [10500, 10200, 9800].
	2	Create a variable for the current value by pulling the last item from the list (Hint: use portfolio_values[2]).
	3	Write an if/else statement: If the current value drops below 10000, print "WARNING: Stop-loss breached". Otherwise, print "Portfolio stable".
Assignment 3: The Simple Moving Average (Loops)
	1	Create a list of daily prices: prices = [45.5, 46.0, 46.5, 45.0, 47.0].
	2	Create a variable called sum_prices and set it to 0.
	3	Write a for loop that iterates through your prices list and adds each price to sum_prices.
	4	After the loop finishes, divide sum_prices by 5 to find the average.
	5	print() the average. It should output 46.0.
Assignment 4: Portfolio Tracker (Dictionaries)
	1	Create a dictionary called holdings representing shares owned: "AAPL" (50 shares), "JPM" (100 shares), and "V" (25 shares).
	2	You just bought 10 more shares of Apple. Update the "AAPL" value in your dictionary to 60.
	3	print() the "AAPL" value to verify it updated correctly.
Assignment 5: Reusable ROI (Functions)
	1	Create a function called get_roi that takes two arguments: buy_price and sell_price.
	2	Inside the function, calculate the percentage ROI using the formula from Assignment 1.
	3	Have the function return the calculated ROI.
	4	Call your function using a buy price of 100 and a sell price of 150, and print() the result. It should output 50.0.
