"""
=========================================================
Meta Product Analytics Project
Load CSV Files into MySQL

Author: Maedot E Woldeyes

Purpose:
Load all generated CSV files into the MySQL database.
This is the final step of the ETL pipeline.
=========================================================
"""

import pandas as pd
from sqlalchemy import create_engine

# =========================================================
# Database Connection
# =========================================================
# Connect to the MySQL database.

username = "meta_user"
password = "Meta123!"
host = "localhost"
port = "3306"
database = "meta_product_analytics"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
)

print("Connected successfully!")

# =========================================================
# Load CSV Files
# =========================================================
# Read each generated dataset into a pandas DataFrame.

users_df = pd.read_csv("data/raw/users.csv")
sessions_df = pd.read_csv("data/raw/sessions.csv")
posts_df = pd.read_csv("data/raw/posts.csv")
events_df = pd.read_csv("data/raw/events.csv")
ad_clicks_df = pd.read_csv("data/raw/ad_clicks.csv")

# =========================================================
# Function to Load a DataFrame into MySQL
# =========================================================
# This reusable function inserts a DataFrame into the
# specified MySQL table.

def load_table(df, table_name):

    df.to_sql(
        table_name,
        con=engine,
        if_exists="append",
        index=False
    )

    print(f"✓ Loaded {len(df)} rows into {table_name}")

# =========================================================
# Load Tables