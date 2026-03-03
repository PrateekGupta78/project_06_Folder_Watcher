import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    
    # remove rows with missing email
    df = df.dropna(subset=["email"])

    # keep only valid phone (10 digits)
    df = df[df["phone"].astype(str).str.len() == 10]

    # keep only valid email
    df = df[df["email"].str.contains("@", na=False)]

    return df