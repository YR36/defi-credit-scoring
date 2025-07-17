import pandas as pd

def compute_wallet_features(df: pd.DataFrame) -> pd.DataFrame:
    # pick amount column
    if 'amount' in df.columns:
        df['amt'] = df['amount'].astype(float)
    elif 'value' in df.columns:
        df['amt'] = df['value'].astype(float)
    elif 'underlyingAmount' in df.columns:
        df['amt'] = df['underlyingAmount'].astype(float)
    else:
        raise KeyError(
            "Cannot find numeric field in columns: " + ", ".join(df.columns)
        )

    grouped = df.groupby('wallet')
    agg = grouped.agg(
        total_deposited = ('amt', lambda x: x[df.loc[x.index, 'action']=='deposit'].sum()),
        total_borrowed  = ('amt', lambda x: x[df.loc[x.index, 'action']=='borrow'].sum()),
        num_tx          = ('amt', 'count'),
        unique_days     = ('timestamp', lambda ts: pd.to_datetime(ts).dt.date.nunique()),
    ).fillna(0)

    agg['borrow_deposit_ratio'] = agg.total_borrowed / (agg.total_deposited + 1)
    return agg.reset_index()
