
import pytest
from coupon_validator import coupon_discount, best_discount, is_expired


def test_empty_cart():
    with pytest.raises(ValueError, match="empty cart"):
        coupon_discount("WELCOME10", 0, True, "mon")


def test_welcome_new_user():
    assert coupon_discount("WELCOME10", 200, True, "mon") == 20


def test_welcome_existing_user():
    assert coupon_discount("WELCOME10", 200, False, "mon") == 0


def test_weekend_large_cart():
    assert coupon_discount("WEEKEND20", 500, True, "sat") == 100


def test_weekend_small_cart():
    assert coupon_discount("WEEKEND20", 200, True, "sun") == 50


def test_weekday_coupon():
    assert coupon_discount("WEEKEND20", 500, True, "mon") == 0


def test_flat100_above_threshold():
    assert coupon_discount("FLAT100", 301, False, "mon") == 100


def test_flat100_at_threshold():
    assert coupon_discount("FLAT100", 300, False, "mon") == 0


def test_invalid_coupon():
    assert coupon_discount("INVALID", 500, False, "mon") == 0


def test_best_discount_updates():
    assert best_discount(
        ["WELCOME10", "FLAT100"], 1000, True, "mon"
    ) == 100


def test_best_discount_does_not_update():
    assert best_discount(
        ["INVALID"], 100, False, "mon"
    ) == 0


def test_best_discount_cap():
    assert best_discount(
        ["WELCOME10"], 100, True, "mon"
    ) == 10


def test_best_discount_empty_list():
    assert best_discount([], 100, True, "mon") == 0


def test_expired_nonpositive_validity():
    assert is_expired(10, 5, 0) is True


def test_coupon_expired():
    assert is_expired(16, 5, 10) is True


def test_coupon_not_expired():
    assert is_expired(15, 5, 10) is False
