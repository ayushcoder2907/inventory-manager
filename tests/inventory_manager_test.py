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


# def test_apply_discount():
#     """Test applying a discount."""
#     total = 1000
#     percentage = 10
#
#     result = apply_discount(total, percentage)
#
#     assert result == 900
