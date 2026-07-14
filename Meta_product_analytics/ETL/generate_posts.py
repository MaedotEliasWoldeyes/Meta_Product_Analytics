from faker import Faker
import pandas as pd
import random

# -------------------------------------------------------
# Initialize Faker
# -------------------------------------------------------
# Faker is used to generate realistic timestamps.
fake = Faker()

# -------------------------------------------------------
# Load Users Dataset
# -------------------------------------------------------
# Every post must belong to an existing user, so we first
# load the users that were generated previously.
users_df = pd.read_csv("data/raw/users.csv")

# Convert the dataframe into a list of dictionaries
# for easier random selection.
users = users_df.to_dict("records")

# -------------------------------------------------------
# Post Categories
# -------------------------------------------------------
# Possible topics that users can post about.
categories = [
    "Sports",
    "Technology",
    "Gaming",
    "Food",
    "Travel",
    "Fashion",
    "Music",
    "News",
    "Fitness",
    "Education"
]

# -------------------------------------------------------
# Privacy Settings
# -------------------------------------------------------
# Possible visibility options for each post.
privacy_options = [
    "Public",
    "Friends",
    "Private"
]

# -------------------------------------------------------
# Generate Posts
# -------------------------------------------------------

posts = []

# Total number of posts to generate.
NUM_POSTS = 10000

# Create each post.
for post_id in range(1, NUM_POSTS + 1):

    # Randomly select a user to be the creator.
    creator = random.choice(users)

    posts.append({
        "post_id": post_id,
        "creator_id": creator["user_id"],

        # Random content category.
        "category": random.choice(categories),

        # Random creation time within the last year.
        "created_time": fake.date_time_between(
            start_date="-1y",
            end_date="now"
        ),

        # Random privacy setting.
        "privacy": random.choice(privacy_options)
    })

# -------------------------------------------------------
# Save Posts to CSV
# -------------------------------------------------------

posts_df = pd.DataFrame(posts)

posts_df.to_csv(
    "data/raw/posts.csv",
    index=False
)

print(f"Generated {len(posts_df)} posts successfully!")