import pandas as pd

print("Loading bank.csv...")

# ---------------------------------------
# 1. LOAD DATA
# ---------------------------------------

df = pd.read_csv("bank.csv")

print("\nOriginal columns:")
print(df.columns.tolist())

print("\nOriginal Data:")
print(df.head())


# ---------------------------------------
# 2. CLEAN COLUMN NAMES
# ---------------------------------------

# Remove extra spaces and invisible spaces
df.columns = (
    df.columns
    .str.strip()
    .str.replace("\xa0", " ", regex=False)
    .str.replace(r"\s+", " ", regex=True)
)

print("\nCleaned columns:")
print(df.columns.tolist())


# ---------------------------------------
# 3. FIND WITHDRAWAL COLUMN
# ---------------------------------------

withdrawal_column = None
deposit_column = None

for column in df.columns:

    column_clean = column.strip().upper()

    if "WITHDRAWAL" in column_clean:
        withdrawal_column = column

    if "DEPOSIT" in column_clean:
        deposit_column = column


if withdrawal_column is None:
    raise Exception(
        "WITHDRAWAL AMT column not found. "
        f"Available columns: {df.columns.tolist()}"
    )

if deposit_column is None:
    raise Exception(
        "DEPOSIT AMT column not found. "
        f"Available columns: {df.columns.tolist()}"
    )


print("\nWithdrawal column found:", withdrawal_column)
print("Deposit column found:", deposit_column)


# ---------------------------------------
# 4. CONVERT AMOUNTS TO NUMERIC
# ---------------------------------------

def clean_amount(value):

    if pd.isna(value):
        return None

    # Remove commas
    value = str(value).replace(",", "").strip()

    # Remove extra characters except digits, decimal point and minus
    value = (
        value
        .replace("₹", "")
        .replace("'", "")
    )

    return value


df[withdrawal_column] = df[withdrawal_column].apply(clean_amount)
df[deposit_column] = df[deposit_column].apply(clean_amount)

df[withdrawal_column] = pd.to_numeric(
    df[withdrawal_column],
    errors="coerce"
)

df[deposit_column] = pd.to_numeric(
    df[deposit_column],
    errors="coerce"
)


# ---------------------------------------
# 5. HANDLE MISSING VALUES
# ---------------------------------------

# Assignment requirement:
# Replace missing withdrawal amounts
# using the median.

median_withdrawal = df[withdrawal_column].median()

print("\nMedian withdrawal amount:", median_withdrawal)

df[withdrawal_column] = df[withdrawal_column].fillna(
    median_withdrawal
)

# Missing deposits are treated as zero
df[deposit_column] = df[deposit_column].fillna(0)


# ---------------------------------------
# 6. REMOVE DUPLICATES
# ---------------------------------------

before = len(df)

df = df.drop_duplicates()

after = len(df)

print("\nDuplicate rows removed:", before - after)


# ---------------------------------------
# 7. GROUP BY ACCOUNT NUMBER
# ---------------------------------------

summary = df.groupby("Account No").agg(
    Total_Money_Spent=(withdrawal_column, "sum"),
    Total_Money_Deposited=(deposit_column, "sum"),
    Total_Transactions=("Account No", "count")
).reset_index()


# ---------------------------------------
# 8. SAVE REPORT
# ---------------------------------------

summary.to_csv(
    "summary_report.csv",
    index=False
)


print("\n---------------------------------------")
print("FINAL SUMMARY REPORT")
print("---------------------------------------")

print(summary.head(20))

print("\nTotal accounts:", len(summary))

print("\nsummary_report.csv created successfully!")