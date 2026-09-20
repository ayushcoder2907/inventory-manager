import pytest
from src.inventory_manager import (
    is_valid_quantity,
    calculate_total,
    apply_discount,
    format_price,
)


def test_valid_quantity():
    """Test a valid inventory quantity."""
    quantity = 10

    result = is_valid_quantity(quantity)

    assert result == True


def test_invalid_quantity():
    """Test that zero quantity is invalid."""
    quantity = 0

    result = is_valid_quantity(quantity)

    assert result == False


def test_quantity_type_error():
    """Test that non-integer quantity raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_quantity("10")


def test_apply_discount():
    """Test applying a discount."""
    total = 1000
    percentage = 10

    result = apply_discount(total, percentage)

    assert result == 900.0


def test_calculate_total():
    """Test calculating the total price."""
    result = calculate_total(25, 4)

    assert result == 100


def test_format_price():
    """Test formatting a price amount."""
    result = format_price(42.5)

    assert result == "₹42.50"


def test_calculate_total_validation_errors():
    """Test invalid total calculations raise errors."""
    with pytest.raises(ValueError):
        calculate_total(-1, 2)

    with pytest.raises(ValueError):
        calculate_total(10, 0)


def test_apply_discount_validation_errors():
    """Test invalid discounts raise errors."""
    with pytest.raises(ValueError):
        apply_discount(-1, 10)

    with pytest.raises(ValueError):
        apply_discount(100, 101)


def test_format_price_validation_error():
    """Test invalid price formatting raises an error."""
    with pytest.raises(ValueError):
        format_price(-5)
