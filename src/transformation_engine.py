import pandas as pd
from pathlib import Path

def build_curated_data():
    preprocessed_folder = Path(__file__).resolve().parent.parent / "data" / "preprocessed"

    claimsFile = preprocessed_folder / "claims_20260815.parquet"
    customersFile = preprocessed_folder / "customers_20260815.parquet"
    paymentFile = preprocessed_folder / "payments_20260815.parquet"
    policiesFile = preprocessed_folder / "policies_20260815.parquet"

    claimsDf = pd.read_parquet(claimsFile)
    customersDf = pd.read_parquet(customersFile)
    paymentsDf = pd.read_parquet(paymentFile)
    policiesDf = pd.read_parquet(policiesFile)

    print("claim columns : ", list(claimsDf.columns))
    print("customer columns : ", list(customersDf.columns))
    print("Payment columns : ", list(paymentsDf.columns))
    print("Policies columns : ", list(policiesDf.columns))

    print("claim rows : ", len(claimsDf))
    print("customer rows : ", len(customersDf))
    print("payment rows : ", len(paymentsDf))
    print("policies rows : ", len(policiesDf))

    claim_policy_df = pd.merge(claimsDf, policiesDf, on='Policy_ID', how= "left", suffixes=("_claims", "_policies"))

    print("Claim and policy merged successfully")
    print("Claim Policy Rows: ", len(claim_policy_df))
    print("Claim Policy Columns : ", list(claim_policy_df.columns))

    claim_policy_customer_df = pd.merge(claim_policy_df, customersDf, on="Customer_ID", how="left", suffixes=("","_customers"))
    print("Claim_policy_df and customers merged successfully")
    print("Claim Policy customers Rows: ", len(claim_policy_customer_df))
    print("Claim Policy customers Columns : ", list(claim_policy_customer_df.columns))

    claim_policy_customer_payment_df = pd.merge(claim_policy_customer_df, paymentsDf, how="left", on="Policy_ID", suffixes=("", "_payments"))
    print("Claim_policy_customer_df and payment merged successfully")
    print("Claim Policy customers payment Rows: ", len(claim_policy_customer_payment_df))
    print("Claim Policy customers payment Columns : ", list(claim_policy_customer_payment_df.columns))

    curated_columns = [
        "Claim_ID",
        "Policy_ID",
        "Claim_Amount",
        "Claim_Date",
        "Customer_ID",
        "Policy_Type",
        "Premium_Amount",
        "Start_Date",
        "Customer_Name",
        "Gender",
        "Age",
        "City",
        "Payment_ID",
        "Payment_Date",
        "Payment_Amount"
    ]

    curated_df = claim_policy_customer_payment_df[curated_columns]

    print("Curated columns selected successfully")
    print("Curated Rows:", len(curated_df))
    print("Curated Columns:", list(curated_df.columns))

    curated_folder = Path(__file__).resolve().parent.parent / "data" / "curated"
    curated_folder.mkdir(exist_ok=True, parents=True)
    outputFile = curated_folder / "curated_enriched.parquet"
    curated_df.to_parquet(outputFile, index=False)
    print("curated file created successfully")

    verify_df = pd.read_parquet(outputFile)
    print("CURATED FILE VERIFICATION")
    print("Rows:", len(verify_df))
    print("Columns:", list(verify_df.columns))


