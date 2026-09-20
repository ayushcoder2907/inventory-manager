def is_valid_quantity(quantity):
    """Return True if quantity is a positive integer."""
    if not isinstance(quantity, int):
        raise TypeError("quantity must be an integer")

    return quantity > 0


def calculate_total(price, quantity):
    """Return the total price for an item."""
    if price < 0:
        raise ValueError("price cannot be negative")

    if not is_valid_quantity(quantity):
        raise ValueError("quantity must be positive")

    return price * quantity


def apply_discount(total, percentage):
    """Apply a percentage discount to a total."""
    if total < 0:
        raise ValueError("total cannot be negative")

    if percentage < 0 or percentage > 100:
        raise ValueError("percentage must be between 0 and 100")

    return total - (total * percentage / 100)


def format_price(amount):
    """Format a numeric amount as a price string."""
    if amount < 0:
        raise ValueError("amount cannot be negative")

    return f"₹{amount:.2f}"
