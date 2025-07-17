import os
import pandas as pd
import matplotlib.pyplot as plt

from src.load_data import load_transactions

def extract_numeric_columns(df):
    return df.select_dtypes(include=['number'])

def flatten_action_data(df):
    # Expand the 'actionData' dictionary into separate columns
    if 'actionData' in df.columns:
        action_data = df['actionData'].apply(pd.Series)
        df = df.drop(columns=['actionData'])
        df = pd.concat([df, action_data], axis=1)
    return df

def run():
    print("🔍 Working directory:", os.getcwd())

    # Updated path
    json_path = os.path.join("data", "user-wallet-transactions.json")

    try:
        df = load_transactions(json_path)
        print(f"✅ Loaded {len(df)} transactions")
    except FileNotFoundError as e:
        print(e)
        return

    df = flatten_action_data(df)

    print("ℹ️  Columns in JSON:", list(df.columns))

    numeric_df = extract_numeric_columns(df)
    if numeric_df.empty:
        print(f"❌ Feature error: Cannot find numeric field in columns: {', '.join(df.columns)}")
        return

    print("✅ Numeric columns found:", list(numeric_df.columns))

    # Save as CSV
    output_csv = "output_numeric_features.csv"
    numeric_df.to_csv(output_csv, index=False)
    print(f"📁 Saved numeric features to '{output_csv}'")

    # Plotting histograms
    for col in numeric_df.columns:
        plt.figure(figsize=(8, 5))
        numeric_df[col].dropna().hist(bins=30)
        plt.title(f'Distribution of {col}')
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        filename = f"hist_{col}.png"
        plt.savefig(filename)
        print(f"📊 Saved histogram: {filename}")
        plt.close()

if __name__ == "__main__":
    run()
