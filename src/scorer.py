import numpy as np
import pandas as pd

def score_wallets(features_df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply a simple weighted scoring, then scale raw values to 0–1000.
    """
    # weights
    w = {
        'total_deposited': 0.3,
        'total_borrowed': -0.2,
        'borrow_deposit_ratio': -0.4,
        'num_tx': -0.1,
        'unique_days': 0.2,
    }

    raw = (
        w['total_deposited'] * np.log1p(features_df['total_deposited']) +
        w['total_borrowed']  * np.log1p(features_df['total_borrowed']) +
        w['borrow_deposit_ratio'] * features_df['borrow_deposit_ratio'] +
        w['num_tx']         * np.log1p(features_df['num_tx']) +
        w['unique_days']    * features_df['unique_days']
    )

    # scale to [0,1000]
    mn, mx = raw.min(), raw.max()
    scaled = 1000 * (raw - mn) / (mx - mn)
    features_df['credit_score'] = scaled.round().astype(int)
    return features_df
