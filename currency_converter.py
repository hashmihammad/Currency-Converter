currencies = {
    'USD': {'name': 'US Dollar', 'symbol': '$', 'rate': 1.00},
    'EUR': {'name': 'Euro', 'symbol': '€', 'rate': 0.92},
    'GBP': {'name': 'Pound Sterling', 'symbol': '£', 'rate': 0.78},
    'CNY': {'name': 'Chinese Yuan', 'symbol': '¥', 'rate': 7.26},
    'KWD': {'name': 'Kuwaiti Dinar', 'symbol': 'KD', 'rate': 0.31},
    'SAR': {'name': 'Saudi Riyal', 'symbol': '﷼', 'rate': 3.75},
    'INR': {'name': 'Indian Rupee', 'symbol': '₹', 'rate': 83.3},
    'PKR': {'name': 'Pakistani Rupee', 'symbol': '₨', 'rate': 278.5},
    'KRW': {'name': 'South Korean Won', 'symbol': '₩', 'rate': 1372.7},
    'JPY': {'name': 'Japanese Yen', 'symbol': '¥', 'rate': 157.3},
}

print("Available Currencies:\n")
for code, data in currencies.items():
    print(f"{code}: {data['name']} ({data['symbol']})")

from_currency = input("\nEnter the currency you want to convert FROM (e.g., USD): ").upper()
to_currency = input("Enter the currency you want to convert TO (e.g., PKR): ").upper()
amount = float(input("Enter the amount to convert: "))

if from_currency in currencies and to_currency in currencies:
    usd = amount / currencies[from_currency]['rate']
    converted = usd * currencies[to_currency]['rate']
    symbol1 = currencies[to_currency]['symbol']
    symbol2 = currencies[from_currency]['symbol']
    print(f"\n{symbol2}{amount} {from_currency} = {symbol1}{converted:.2f} {to_currency}")
else:
    print("\nInvalid currency code entered. Please check and try again.")
