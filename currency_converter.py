import time

currencies = {
    'USD': {'name': 'US Dollar', 'symbol': '$', 'rate': 1.00},
    'EUR': {'name': 'Euro', 'symbol': '€', 'rate': 0.92},
    'GBP': {'name': 'Pound Sterling', 'symbol': '£', 'rate': 0.78},
    'CNY': {'name': 'Chinese Yuan', 'symbol': '¥', 'rate': 7.26},
    'KWD': {'name': 'Kuwaiti Dinar', 'symbol': 'KD', 'rate': 0.31},
    'SAR': {'name': 'Saudi Riyal', 'symbol': '﷼', 'rate': 3.75},
    'INR': {'name': 'Indian Rupee', 'symbol': '₹', 'rate': 83.3},
    'PKR': {'name': 'Pakistani Rupee', 'symbol': '₨', 'rate': 278.5},
    'KRW': {'name': 'South Korean Won', 'symbol': '₩', 'rate': 1372.7}
}

print("\nAvailable Currencies:")
for code in currencies:
    name = currencies[code]['name']
    symbol = currencies[code]['symbol']
    print(f"{code} - {name} ({symbol})")

from_currency = input("\nWhich currency do you want to convert FROM? : ").upper()
to_currency = input("Which currency do you want to convert TO? : ").upper()

if from_currency not in currencies or to_currency not in currencies:
    print("\nX Invalid currency code. Please restart and try again.")
else:
    amount_input = input(f"Enter amount in {from_currency}: ")

    if not amount_input.replace('.', '', 1).isdigit():
        print("\nX Invalid amount. Please enter numbers only.")
    else:
        amount = float(amount_input)

        usd = amount / currencies[from_currency]['rate']
        converted = usd * currencies[to_currency]['rate']

        print("\nConverting", end="")
        for _ in range(3):
            print(".", end="", flush=True)
            time.sleep(0.5)

        from_symbol = currencies[from_currency]['symbol']
        to_symbol = currencies[to_currency]['symbol']

        print(f"\n\n{from_symbol}{amount:.2f} {from_currency} = {to_symbol}{converted:.2f} {to_currency}")
