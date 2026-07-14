from faker import Faker
import pandas as pd
import random

# -------------------------------------------------------
# Initialize Faker
# -------------------------------------------------------
# Faker is used to generate realistic event timestamps.
fake = Faker()

# -------------------------------------------------------
# Load Sessions Dataset
# -------------------------------------------------------
# Every event must belong to an existing session, so we
# first load the sessions that were previously generated.
sessions_df = pd.read_csv("data/raw/sessions.csv")

# Convert login and logout times into datetime objects so
# Faker can generate timestamps between them.
sessions_df["login_time"] = pd.to_datetime(sessions_df["login_time"])
sessions_df["logout_time"] = pd.to_datetime(sessions_df["logout_time"])

# -------------------------------------------------------
# Event Types
# -------------------------------------------------------
# These represent common actions users perform while
# interacting with the social media platform.
event_types = [
    "View Feed",
    "View Post",
    "Like",
    "Comment",
    "Share",
    "Search",
    "View Profile",
    "Follow",
    "Open App",
    "Logout"
]

# -------------------------------------------------------
# Event Probabilities
# -------------------------------------------------------
# Assign different probabilities so that some actions occur
# more frequently than others, creating a more realistic
# user behavior dataset.
probabilities = [
    0.35,   # View Feed
    0.25,   # View Post
    0.12,   # Like
    0.05,   # Comment
    0.03,   # Share
    0.07,   # Search
    0.05,   # View Profile
    0.03,   # Follow
    0.04,   # Open App
    0.01    # Logout
]

# -------------------------------------------------------
# Generate Events
# -------------------------------------------------------

events = []

# Event IDs begin at 1 and increase sequentially.
event_id = 1

# Loop through every session.
for _, session in sessions_df.iterrows():

    # Each session generates between 5 and 20 user actions.
    num_events = random.randint(5, 20)

    # Generate each event within the session.
    for _ in range(num_events):

        events.append({

            # Unique event identifier.
            "event_id": event_id,

            # Link event to its session.
            "session_id": session["session_id"],

            # Select an event using weighted probabilities.
            "event_type": random.choices(
                event_types,
                weights=probabilities,
                k=1
            )[0],

            # Generate a realistic timestamp between the
            # user's login and logout time.
            "event_time": fake.date_time_between(
                start_date=session["login_time"],
                end_date=session["logout_time"]
            )
        })

        # Increment the event ID.
        event_id += 1

# -------------------------------------------------------
# Save Events to CSV
# -------------------------------------------------------

events_df = pd.DataFrame(events)

events_df.to_csv(
    "data/raw/events.csv",
    index=False
)

print(f"Generated {len(events_df)} events successfully!")

