import pandas as pd

print("Loading dataset...")

# Original Kaggle dataset
df = pd.read_csv(
    "online_retail.csv",
    encoding="latin1"
)

print("Original rows:", len(df))

# -----------------------------
# 1. CLEAN DATA
# -----------------------------

# Remove rows without CustomerID
df = df.dropna(subset=["CustomerID"])

# Remove cancelled invoices
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Remove invalid quantities/prices
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# Convert date
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Customer ID as integer
df["CustomerID"] = df["CustomerID"].astype(int)

# -----------------------------
# 2. CALCULATE TRANSACTION VALUE
# -----------------------------

df["Amount"] = df["Quantity"] * df["UnitPrice"]

# -----------------------------
# 3. CUSTOMER-LEVEL DATA
# -----------------------------

customer = df.groupby("CustomerID").agg(
    total_spent=("Amount", "sum"),
    total_orders=("InvoiceNo", "nunique"),
    total_items=("Quantity", "sum"),
    average_order_value=("Amount", "mean"),
    last_purchase=("InvoiceDate", "max"),
    country=("Country", "first")
).reset_index()

# -----------------------------
# 4. DAYS SINCE LAST PURCHASE
# -----------------------------

latest_date = df["InvoiceDate"].max()

customer["days_since_purchase"] = (
    latest_date - customer["last_purchase"]
).dt.days

# -----------------------------
# 5. SIMULATED RECOVERY EVENT
# -----------------------------

# We are NOT claiming these events exist
# in the Kaggle dataset.
# These are prototype/simulated events.

def assign_event(row):

    if row["days_since_purchase"] > 180:
        return "checkout_abandoned"

    elif row["days_since_purchase"] > 90:
        return "subscription_failed"

    elif row["days_since_purchase"] > 45:
        return "payment_failed"

    else:
        return "successful"


customer["recovery_event"] = customer.apply(
    assign_event,
    axis=1
)

# -----------------------------
# 6. SIMULATED FAILURE REASON
# -----------------------------

def failure_reason(event):

    if event == "payment_failed":
        return "card_expired"

    elif event == "subscription_failed":
        return "insufficient_funds"

    elif event == "checkout_abandoned":
        return "checkout_abandoned"

    else:
        return "none"


customer["failure_reason"] = customer[
    "recovery_event"
].apply(failure_reason)

# -----------------------------
# 7. SIMULATED RECOVERY ATTEMPTS
# -----------------------------

customer["recovery_attempts"] = 0

customer.loc[
    customer["recovery_event"] != "successful",
    "recovery_attempts"
] = 1

# -----------------------------
# 8. RISK SCORE
# -----------------------------

def calculate_risk(row):

    score = 0

    if row["recovery_event"] == "payment_failed":
        score += 30

    elif row["recovery_event"] == "subscription_failed":
        score += 40

    elif row["recovery_event"] == "checkout_abandoned":
        score += 25

    # Older customers = higher risk
    if row["days_since_purchase"] > 180:
        score += 30

    elif row["days_since_purchase"] > 90:
        score += 20

    elif row["days_since_purchase"] > 45:
        score += 10

    # High-value customers get attention
    if row["total_spent"] > 5000:
        score += 10

    return min(score, 100)


customer["risk_score"] = customer.apply(
    calculate_risk,
    axis=1
)

# -----------------------------
# 9. RISK LEVEL
# -----------------------------

def risk_level(score):

    if score >= 70:
        return "HIGH"

    elif score >= 40:
        return "MEDIUM"

    else:
        return "LOW"


customer["risk_level"] = customer[
    "risk_score"
].apply(risk_level)

# -----------------------------
# 10. RECOVERY PROBABILITY
# -----------------------------

customer["recovery_probability"] = (
    95 - customer["risk_score"] * 0.6
)

customer["recovery_probability"] = (
    customer["recovery_probability"]
    .clip(10, 95)
    .round(1)
)

# -----------------------------
# 11. EXPECTED RECOVERY
# -----------------------------

customer["revenue_at_risk"] = customer["total_spent"]

customer["expected_recovery"] = (
    customer["revenue_at_risk"]
    * customer["recovery_probability"]
    / 100
)

# -----------------------------
# 12. RECOMMENDED ACTION
# -----------------------------

def recommended_action(row):

    if row["recovery_event"] == "payment_failed":
        return "Send payment recovery link"

    elif row["recovery_event"] == "subscription_failed":
        return "Retry payment + reminder"

    elif row["recovery_event"] == "checkout_abandoned":
        return "Send checkout reminder"

    else:
        return "No action required"


customer["recommended_action"] = customer.apply(
    recommended_action,
    axis=1
)

# -----------------------------
# 13. SAVE RECOVERAI DATA
# -----------------------------

customer.to_csv(
    "recoverai_data.csv",
    index=False
)

print()
print("SUCCESS! RecoverAI dataset created.")
print("Customers:", len(customer))
print("File: recoverai_data.csv")

print()
print(customer.head())