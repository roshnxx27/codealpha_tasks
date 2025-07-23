# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 310,
    "AMZN": 145
}

portfolio = {}
total_investment = 0

print("📈 Stock Portfolio Tracker")
print("Available Stocks & Prices:")
for stock, price in stock_prices.items():
    print(f"  {stock}: ${price}")
print("\nEnter 'done' to finish entering stocks.\n")

# User input loop
while True:
    stock_name = input("Enter stock symbol (e.g., AAPL): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not found. Please enter a valid symbol from the list.\n")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
        if quantity < 0:
            print("⚠️ Quantity can't be negative.\n")
            continue
    except ValueError:
        print("⚠️ Please enter a valid number.\n")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

# Calculate total investment
print("\n🧾 Portfolio Summary:")
summary_lines = []
for stock, qty in portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    line = f"{stock}: {qty} shares × ${stock_prices[stock]} = ${value}"
    print(line)
    summary_lines.append(line)

print(f"\n💰 Total Investment: ${total_investment}")

# Optional: Save to file
save = input("\nDo you want to save the summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        f.write("------------------------\n")
        for line in summary_lines:
            f.write(line + "\n")
        f.write(f"\nTotal Investment: ${total_investment}\n")
    print("📁 Saved as 'portfolio_summary.txt'.")