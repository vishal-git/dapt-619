import polars as pl


def load_raw(path="data/raw/churn_raw.csv"):
    return pl.read_csv(path)


def clean(df: pl.DataFrame) -> pl.DataFrame:
    """Return a cleaned copy of the raw data. Never modify the raw file."""
    # step 1: one transformation per data problem in your README's issues table
    # --
    return df
