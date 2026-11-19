def clean_customers(df):
    """Drop duplicate customers and tidy the state codes."""
    out = df.drop_duplicates(subset="customer_id").copy()
    out["state"] = out["state"].str.strip().str.upper()
    return out
