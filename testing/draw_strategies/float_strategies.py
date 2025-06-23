from hypothesis.strategies import floats, SearchStrategy, just

all_valid_floats = floats(
    allow_nan=False, allow_infinity=False, allow_subnormal=True, width=64
)

small_floats = floats(min_value=-10.0, max_value=10.0, allow_subnormal=True, width=64)
small_normal_floats = floats(
    min_value=-10.0, max_value=10.0, allow_subnormal=False, width=64
)


def order_of_magnitude_floats(
    number_of_orders: int, positive_only: bool = False, can_be_zero: bool = True
) -> SearchStrategy[float]:
    assert number_of_orders > 0
    min_abs = 1.0
    max_abs = 10.0**number_of_orders

    positive = floats(min_value=min_abs, max_value=max_abs, width=64)
    negative = floats(min_value=-max_abs, max_value=-min_abs, width=64)

    res = positive
    if not positive_only:
        res = res | negative
    if can_be_zero:
        res = just(0.0) | res

    return res
