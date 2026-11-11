
from hypothesis import given, strategies as st
from coupon_validator import split_code, most_expensive, expiry_days


# Test 1: Coupon code should not crash
@given(st.text() | st.none())
def test_split_code_no_crash(s):
    try:
        split_code(s)
    except Exception as e:
        assert False, f"split_code crashed with input {s!r}: {e}"


# Test 2: Price processing should not crash
@given(st.text() | st.none())
def test_most_expensive_no_crash(s):
    try:
        most_expensive(s)
    except Exception as e:
        assert False, f"most_expensive crashed with input {s!r}: {e}"


# Test 3: Date processing should not crash
@given(st.text() | st.none())
def test_expiry_days_no_crash(s):
    try:
        expiry_days(s)
    except Exception as e:
        assert False, f"expiry_days crashed with input {s!r}: {e}"
