from faker import Faker
import pandas as pd
import random
from datetime import timedelta

# -------------------------------------------------------
# Initialize Faker
# -------------------------------------------------------
# Faker is used to generate realistic timestamps.
fake = Faker()

# -------------------------------------------------------
# Load Users Dataset
# -------------------------------------------------------
# Each session must belong to an existing user, so we first
# load the users that were generated previously.
users_df = pd.read_csv("data/raw/users.csv")

# Convert the dataframe into a list of dictionaries.
# This makes it easy to loop through each user.
users = users_df.to_dict("records")

# -------------------------------------------------------
# Device Types
# -------------------------------------------------------
# Possible devices used to access the platform.
devices = [
    "iPhone",
    "Android",
    "Windows",
    "Mac",
    "iPad"
]

# -------------------------------------------------------
# Generate Sessions
# -------------------------------------------------------

sessions = []

# Session IDs start at 1 and increase for every session.
session_id = 1

# Loop through every user.
for user in users:

    # ---------------------------------------------------
    # Decide how active this user is.
    #
    # 80% -> Regular users (1–15 sessions)
    # 18% -> Active users (15–30 sessions)
    #  2% -> Power users (100–500 sessions)
    # ---------------------------------------------------
    chance = random.random()

    if chance < 0.80:
        num_sessions = random.randint(1, 15)

    elif chance < 0.98:
        num_sessions = random.randint(15, 30)

    else:
        num_sessions = random.randint(100, 500)

    # ---------------------------------------------------
    # Generate each session for the current user.
    # ---------------------------------------------------
    for _ in range(num_sessions):

        # Randomly choose a device.
        device = random.choice(devices)

        # Assign the correct operating system based on device.
        os_map = {
            "iPhone": "iOS",
            "iPad": "iOS",
            "Android": "Android",
            "Windows": "Windows",
            "Mac": "macOS"
        }

        operating_system = os_map[device]

        # Generate a random login time within the last year.
        login_time = fake.date_time_between(
            start_date="-1y",
            end_date="now"
        )

        # ---------------------------------------------------
        # Generate realistic session durations.
        #
        # Most sessions are short.
        # Only a small percentage are very long.
        # ---------------------------------------------------
        r = random.random()

        if r < 0.40:
            session_duration = random.randint(2, 10)

        elif r < 0.70:
            session_duration = random.randint(10, 30)

        elif r < 0.90:
            session_duration = random.randint(30, 60)

        elif r < 0.98:
            session_duration = random.randint(60, 120)

        else:
            session_duration = random.randint(120, 180)

        # Calculate logout time.
        logout_time = login_time + timedelta(minutes=session_duration)

        # Save the generated session.
        sessions.append({
            "session_id": session_id,
            "user_id": user["user_id"],
            "device": device,
            "operating_system": operating_system,
            "login_time": login_time,
            "logout_time": logout_time,
            "session_duration": session_duration
        })

        # Increment the session ID.
        session_id += 1

# -------------------------------------------------------
# Save Sessions to CSV
# -------------------------------------------------------
sessions_df = pd.DataFrame(sessions)

sessions_df.to_csv(
    "data/raw/sessions.csv",
    index=False
)

print(f"Generated {len(sessions_df)} sessions successfully!")