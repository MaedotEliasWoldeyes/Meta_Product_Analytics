from faker import Faker
import pandas as pd
import random

# -------------------------------------------------------
# Initialize Faker
# -------------------------------------------------------
# Faker is included for consistency across the ETL pipeline.
# (Not directly used in this script but can be useful if
# additional ad-related timestamps are added later.)
fake = Faker()

# -------------------------------------------------------
# Load Events Dataset
# -------------------------------------------------------
# Ads are shown during specific user actions, so we first
# load the events that were previously generated.
events_df = pd.read_csv("data/raw/events.csv")

# -------------------------------------------------------
# Ad Categories
# -------------------------------------------------------
# Possible categories of advertisements displayed to users.
ad_categories = [
    "Technology",
    "Fashion",
    "Gaming",
    "Food",
    "Travel",
    "Finance",
    "Education",
    "Entertainment"
]

# -------------------------------------------------------
# Generate Advertisement Records
# -------------------------------------------------------

ad_clicks = []

# Ad IDs start at 1 and increase sequentially.
ad_id = 1

# Loop through every user event.
for _, event in events_df.iterrows():

    # ---------------------------------------------------
    # Ads are only shown during events where users are
    # likely to encounter advertisements.
    #
    # Examples:
    # - Opening the app
    # - Browsing the feed
    # - Viewing a post
    # ---------------------------------------------------
    if event["event_type"] in ["Open App", "View Feed", "View Post"]:

        # Only about 20% of eligible events display an ad.
        if random.random() < 0.20:

            # Simulate whether the user clicked the ad.
            # Approximately 12% of displayed ads receive
            # a click.
            clicked = random.random() < 0.12

            ad_clicks.append({

                # Unique advertisement record ID.
                "ad_id": ad_id,

                # Link the advertisement to the event
                # where it was displayed.
                "event_id": event["event_id"],

                # Random advertisement category.
                "ad_category": random.choice(ad_categories),

                # Indicates whether the user clicked the ad.
                "clicked": clicked
            })

            # Increment the advertisement ID.
            ad_id += 1

# -------------------------------------------------------
# Save Advertisement Data to CSV
# -------------------------------------------------------

ad_clicks_df = pd.DataFrame(ad_clicks)

ad_clicks_df.to_csv(
    "data/raw/ad_clicks.csv",
    index=False
)

print(f"Generated {len(ad_clicks_df)} ad records successfully!")