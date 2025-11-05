# Currency Converter

def currency_converter():
    print("Currency Converter")
    print("------------------")

    # Define a dictionary of exchange rates
    exchange_rates = {
        "USD": 1.00,  # US Dollar
        "EUR": 0.84,  # Euro
        "GBP": 0.76,  # British Pound
        "JPY": 109.21,  # Japanese Yen
        "CNY": 6.93,  # Chinese Yuan
        "INR": 74.83,  # Indian Rupee
        # Add more currencies as needed
    }

    # Ask the user for the amount to convert
    amount = float(input("Enter the amount to convert: "))

    # Ask the user for the original currency
    original_currency = input("Enter the original currency: ").upper()

    # Ask the user for the target currency
    target_currency = input("Enter the target currency: ").upper()

    # Check if the original and target currencies are valid
    if original_currency not in exchange_rates or target_currency not in exchange_rates:
        print("Invalid currency. Please try again.")
        return

    # Calculate the converted amount
    converted_amount = amount * exchange_rates[target_currency] / exchange_rates[original_currency]

    # Print the result
    print(f"{amount} {original_currency} is equal to {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    currency_converter()