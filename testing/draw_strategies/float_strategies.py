from hypothesis.strategies import floats

all_valid_floats = floats(
    allow_nan=False, allow_infinity=False, allow_subnormal=True, width=64
)

small_floats = floats(min_value=-10.0, max_value=10.0, allow_subnormal=True, width=64)
small_normal_floats = floats(
    min_value=-10.0, max_value=10.0, allow_subnormal=False, width=64
)

order_of_magnitude_floats = floats(
    min_value=0.01, max_value=100.0, allow_subnormal=False, width=64
) | floats(min_value=-100.0, max_value=-0.01, allow_subnormal=False, width=64)
