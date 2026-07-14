"""
=========================================================
Meta Product Analytics Project
Generate Synthetic Users

Author: Maedot E Woldeyes

Purpose:
Generate realistic synthetic user profiles for a
social media platform.
=========================================================
"""

from faker import Faker
import pandas as pd
import random

# =========================================================
# Initialize Faker and project settings
# =========================================================

fake = Faker()

# Number of synthetic users to generate
NUM_USERS = 1000

# =========================================================
# User attribute options
# =========================================================

countries = [
    "USA", "Canada", "UK", "Germany",
    "France", "India", "Brazil", "Australia"
]

genders = [
    "Male",
    "Female",
    "Other"
]

account_types = [
    "Personal",
    "Creator",
    "Business"
]

languages = [
    "English",
    "Spanish",
    "French",
    "German",
    "Hindi"
]

referral_sources = [
    "Instagram Ad",
    "Facebook",
    "Friend Invite",
    "Google Search",
    "TikTok"
]

# =========================================================
# Generate Users
# =========================================================
# Create realistic user profiles with demographic
# information and account attributes.


users = []

for user_id in range(100001, 100001 + NUM_USERS):

    users.append({
        "user_id": user_id,
        "signup_date": fake.date_between(start_date='-2y', end_date='today'),
        "country": random.choice(countries),
        "age": random.randint(18, 65),
        "gender": random.choice(genders),
        "account_type": random.choice(account_types),
        "language": random.choice(languages),
        "referral_source": random.choice(referral_sources),
        "email_verified": random.choice([True, False])
    })

users_df = pd.DataFrame(users)

# Save generated users to CSV
users_df.to_csv("data/raw/users.csv", index=False)

print(users_df.head())

print(f"\nGenerated {NUM_USERS} users successfully!")




