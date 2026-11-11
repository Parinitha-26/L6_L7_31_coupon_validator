
from datetime import datetime, date


# Function 1: Split and validate coupon code
def split_code(code):
    try:
        if not isinstance(code, str) or not code.strip():
            return None

        parts = code.strip().upper().split('-')

        if len(parts) != 2:
            return None

        prefix, value = parts

        if not prefix.isalnum() or not value.isdigit():
            return None

        return prefix, int(value)

    except (ValueError, TypeError, AttributeError):
        return None


# Function 2: Find the most expensive item
def most_expensive(prices_csv):
    try:
        if not isinstance(prices_csv, str) or not prices_csv.strip():
            return None

        prices = []

        for p in prices_csv.split(','):
            p = p.strip()

            if not p:
                return None

            price = float(p)

            if price < 0 or price != price:
                return None

            if price == float('inf') or price == float('-inf'):
                return None

            prices.append(price)

        if not prices:
            return None

        return max(prices)

    except (ValueError, TypeError, AttributeError, OverflowError):
        return None


# Function 3: Calculate days since 1 January 2024
def expiry_days(date_text):
    try:
        if not isinstance(date_text, str) or not date_text.strip():
            return None

        input_date = datetime.strptime(
            date_text.strip(), "%Y-%m-%d"
        ).date()

        start_date = date(2024, 1, 1)

        return (input_date - start_date).days

    except (ValueError, TypeError, AttributeError):
        return None


# Main function
def main():
    print("==== Running split_code ====")
    user_input = input("Enter a coupon code (e.g. save-20): ")
    result = split_code(user_input)
    print("Prefix and Value:", result)

    print("\n==== Running most_expensive ====")
    user_input = input("Enter item prices as CSV (e.g. 199,49.5,320): ")
    result = most_expensive(user_input)
    print("Most Expensive Item:", result)

    print("\n==== Running expiry_days ====")
    user_input = input("Enter an expiry date as YYYY-MM-DD: ")
    result = expiry_days(user_input)
    print("Days Since 2024:", result)


if __name__ == "__main__":
    main()
