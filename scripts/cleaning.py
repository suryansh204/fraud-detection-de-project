import pandas as pd

INPUT_PATH = 'raw_data/PS_20174392719_1491204439457_log.csv'
OUTPUT_PATH = 'cleaned_data/cleaned_paysim.csv'

cols_to_drop = [
    'oldbalanceOrg', 'newbalanceOrig',
    'oldbalanceDest', 'newbalanceDest',
    'nameOrig', 'nameDest'
]

df = pd.read_csv(INPUT_PATH)

df_clean = df.drop(columns=cols_to_drop)

df_clean.to_csv(OUTPUT_PATH, index=False)

print(f"Cleaned data saved to {OUTPUT_PATH} with shape {df_clean.shape}")
