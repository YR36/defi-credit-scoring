DeFi Wallet Credit Scoring Model
Project Overview
This project aims to assign a credit score (ranging from 0 to 1000) to individual DeFi wallets based on their historical transaction behavior within the Aave V2 protocol. The goal is to identify reliable and responsible users (higher scores) versus potentially risky, bot-like, or exploitative behavior (lower scores).

The solution is implemented as a one-step Python script that processes raw transaction data from a JSON file, engineers relevant features, computes a credit score for each wallet, and outputs the results.

Architecture and Processing Flow
The credit scoring system follows a clear, modular architecture:

Data Loading (src/load_data.py):

The process begins by loading raw transaction data from a specified JSON file (user-wallet-transactions.json).

It handles potential FileNotFoundError or parsing issues.

Data Preprocessing (run_scoring.py - flatten_action_data):

The actionData field, which is a nested dictionary in the raw JSON, is flattened into top-level columns. This makes the data more accessible for feature engineering.

Feature Engineering (src/features.py - compute_wallet_features):

Transaction-level data is aggregated to create wallet-level features. These features are designed to capture different aspects of a wallet's interaction with the Aave V2 protocol.

Key features computed include:

total_deposited: Sum of all assets deposited by the wallet.

total_borrowed: Sum of all assets borrowed by the wallet.

num_tx: Total number of transactions performed by the wallet.

unique_days: Number of distinct days the wallet was active.

borrow_deposit_ratio: Ratio of total borrowed amount to total deposited amount (with a small offset to prevent division by zero). This is a crucial indicator of risk.

Credit Scoring (run_scoring.py - assign_credit_score):

A credit score between 0 and 1000 is assigned to each wallet based on the engineered features.

Scoring Logic:

Each wallet starts with a base score of 500.

Features (total_deposited, num_tx, unique_days, borrow_deposit_ratio) are normalized to a 0-1 scale to ensure fair contribution.

Positive contributions: Higher total_deposited, num_tx, and unique_days increase the score.

Negative contributions/Risk mitigation: A lower borrow_deposit_ratio (indicating less reliance on borrowed funds relative to deposits) increases the score.

The score is capped between 0 and 1000.

Output Generation (run_scoring.py):

The script saves the final wallet credit scores to a CSV file named wallet_scores.csv.

It also generates a histogram visualizing the distribution of these credit scores, saved as hist_credit_scores.png.

Deliverables
Upon running the script, the following outputs will be generated:

wallet_scores.csv: A CSV file containing wallet addresses and their corresponding credit_score.

hist_credit_scores.png: A histogram image illustrating the distribution of the calculated credit scores.

README.md: This document, explaining the model and its usage.

analysis.md: A detailed analysis of the wallet scores and their implications.

How to Run the Script
To run the credit scoring script, follow these steps:

Clone the Repository:

git clone <your-repo-url>
cd <your-repo-name>

Create data Directory:
Ensure you have a data directory in the root of your project.

mkdir data

Download Data:
Download the user-wallet-transactions.json file from the provided link and place it inside the data/ directory.

Direct Download Link (JSON)

Compressed Zip File (ZIP)
(If you download the zip, remember to extract user-wallet-transactions.json into the data directory.)

Install Dependencies:
Make sure you have pandas and matplotlib installed.

pip install pandas matplotlib

Run the Script:
Execute the main scoring script from the project root:

python run_scoring.py

The script will print progress messages to the console, and upon successful completion, you will find wallet_scores.csv and hist_credit_scores.png in your project's root directory.