import matplotlib.pyplot as plt
import pandas as pd

def plot_distribution(df: pd.DataFrame) -> None:
    """
    Plot and save a histogram of the credit_score column.
    """
    plt.figure()
    plt.hist(df['credit_score'], bins=10, edgecolor='black')
    plt.xlabel('Credit Score')
    plt.ylabel('Number of Wallets')
    plt.title('Wallet Credit Score Distribution')
    plt.tight_layout()
    plt.savefig('score_distribution.png')
    plt.show()

if __name__ == '__main__':
    # quick local test
    df = pd.read_csv('wallet_scores.csv')
    plot_distribution(df)
