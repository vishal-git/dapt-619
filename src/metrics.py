def percent_change(old, new):
    """Percent change from old to new. 80 -> 100 is 25.0"""
    if old == 0:
        raise ValueError("old value cannot be zero")
    return (new - old) / abs(old) * 100
