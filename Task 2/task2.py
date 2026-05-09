def main():
    # Hardcoded dictionary to define stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 150,
        "MSFT": 400,
        "AMZN": 175
    }

    portfolio = {}
    total_investment = 0

    print("--- Stock Portfolio Tracker ---")
    print(f"Available stocks: {', '.join(stock_prices.keys())}")

    # User inputs stock names and quantity
    while True:
        symbol = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
        
        if symbol in stock_prices:
            try:
                quantity = int(input(f"Enter quantity for {symbol}: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
                
                # Calculate value for this specific entry
                price = stock_prices[symbol]
                value = price * quantity
                
                # Update portfolio and total
                portfolio[symbol] = portfolio.get(symbol, 0) + quantity
                total_investment += value
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print("Stock symbol not found in database. Please try again.")

    # Display total investment value
    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        print(f"{stock}: {qty} shares @ ${stock_prices[stock]} each")
    
    print("-" * 25)
    print(f"Total Investment Value: ${total_investment}")

    # Optionally save the result in a .txt file
    save_choice = input("\nWould you like to save this result to a file? (y/n): ").lower()
    if save_choice == 'y':
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock Portfolio Summary\n")
            f.write("=" * 25 + "\n")
            for stock, qty in portfolio.items():
                f.write(f"{stock}: {qty} shares | Value: ${qty * stock_prices[stock]}\n")
            f.write("-" * 25 + "\n")
            f.write(f"Total Portfolio Value: ${total_investment}\n")
        print("Summary saved to 'portfolio_summary.txt'.")

if __name__ == "__main__":
    main()