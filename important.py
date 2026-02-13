import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

excel_path = r"C:\Users\laksh\OneDrive\Desktop\Portfolio Management System\potf.xlsx"
df = pd.read_excel(excel_path)

password = quote_plus("Luckygupt@1990")

engine = create_engine(
    f"postgresql://postgres:{password}@localhost:5432/pg_db"
)

df.to_sql("potf", engine, if_exists="replace", index=False)

print(" Data PostgreSQL me save ho gaya")
