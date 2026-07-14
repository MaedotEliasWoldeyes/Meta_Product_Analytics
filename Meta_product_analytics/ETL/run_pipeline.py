"""
=========================================================
Meta Product Analytics Project
ETL Pipeline Runner

Author: Maedot E Woldeyes

Purpose:
Run the complete ETL pipeline from start to finish.

Pipeline Steps:
1. Generate synthetic users
2. Generate user sessions
3. Generate posts
4. Generate user events
5. Generate advertisement click records
6. Load all generated data into MySQL
=========================================================
"""

import subprocess
import sys

# =========================================================
# List of ETL scripts
# =========================================================
# These scripts are executed in order because later
# datasets depend on earlier ones.
#
# Users    → Sessions → Posts → Events
#                     ↓
#                 Ad Clicks
#                     ↓
#                 Load to MySQL
# =========================================================

scripts = [
    "ETL/generate_users.py",
    "ETL/generate_sessions.py",
    "ETL/generate_posts.py",
    "ETL/generate_events.py",
    "ETL/generate_ad_clicks.py",
    "ETL/load_to_mysql.py"
]

# =========================================================
# Execute Pipeline
# =========================================================

print("=" * 60)
print("Starting Meta Product Analytics ETL Pipeline")
print("=" * 60)

for script in scripts:

    print(f"\nRunning {script}...")

    # Run the current script using the same Python
    # interpreter as the virtual environment.
    result = subprocess.run(
        [sys.executable, script]
    )

    # Stop the pipeline immediately if a script fails.
    if result.returncode != 0:
        print("\n" + "=" * 60)
        print(f"❌ Pipeline stopped because {script} failed.")
        print("=" * 60)
        break

else:
    print("\n" + "=" * 60)
    print("✅ ETL Pipeline completed successfully!")
    print("All synthetic data has been generated and loaded.")
    print("=" * 60)