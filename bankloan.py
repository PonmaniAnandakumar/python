import pandas as pd
from functools import reduce

# Customer data
data = {
    "Name": ["Ravi", "Anu", "Kiran", "Meena"],
    "Age": [30, 22, 45, 19],
    "Income": [40000, 28000, 50000, 30000],
    "CreditScore": [720, 680, 750, 600],
    "LoanAmount": [300000, 200000, 400000, 150000]
}

df = pd.DataFrame(data)

# FILTER – eligible customers
eligible = df[
    (df["Age"] >= 21) &
    (df["Income"] >= 25000) &
    (df["CreditScore"] >= 650) &
    (df["LoanAmount"] <= df["Income"] * 10)
].copy()

# MAP – calculate processing fee (2%)
eligible["ProcessingFee"] = list(
    map(lambda x: x * 0.02, eligible["LoanAmount"])
)

# APPLY – loan status
eligible["LoanStatus"] = eligible.apply(
    lambda row: "Approved", axis=1
)

# REDUCE – total approved loan amount
total_loan = reduce(
    lambda x, y: x + y, eligible["LoanAmount"]
)

print("Eligible Customers:")
print(eligible)
print("\nTotal Approved Loan Amount:", total_loan)
