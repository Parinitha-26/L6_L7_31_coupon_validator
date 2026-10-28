
import pytest

from coupon_validator import (
    coupon_discount,
    best_discount,
    is_expired,
)


def test_empty_cart_raises_error():
    with pytest.raises(ValueError, match="empty cart"):
        coupon_discount("WELCOME10", 0, True, "mon")


def test_welcome10_new_user():
    assert coupon_discount("WELCOME10", 1000, True, "mon") == 100


def test_welcome10_existing_user():
    assert coupon_discount("WELCOME10", 1000, False, "mon") == 0


def test_weekend20_qualifying_cart():
    assert coupon_discount("WEEKEND20", 500, True, "sat") == 100


def test_weekend20_small_cart():
    assert coupon_discount("WEEKEND20", 200, True, "sun") == 50


def test_weekend20_weekday():
    assert coupon_discount("WEEKEND20", 500, True, "mon") == 0


def test_flat100_qualifying_cart():
    assert coupon_discount("FLAT100", 301, False, "mon") == 100


def test_flat100_cart_at_threshold():
    assert coupon_discount("FLAT100", 300, False, "mon") == 0


def test_unknown_coupon():
    assert coupon_discount("INVALID", 500, False, "mon") == 0


def test_best_discount_selects_largest():
    assert best_discount(
        ["WELCOME10", "FLAT100"], 1000, True, "mon"
    ) == 100


def test_best_discount_applies_cap():
    assert best_discount(
        ["WELCOME10"], 100, True, "mon"
    ) == 10


def test_best_discount_empty_codes():
    assert best_discount([], 100, True, "mon") == 0


def test_best_discount_no_discount():
    assert best_discount(
        ["INVALID"], 100, False, "mon"
    ) == 0


def test_expired_nonpositive_validity():
    assert is_expired(10, 5, 0) is True


def test_expired_after_validity():
    assert is_expired(16, 5, 10) is True


def test_not_expired_at_validity_boundary():
    assert is_expired(15, 5, 10) is False
