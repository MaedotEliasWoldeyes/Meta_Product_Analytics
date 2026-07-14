# Meta Product Analytics Dashboard

An end-to-end product analytics project that simulates user activity on a social media platform using synthetic data. The project demonstrates the complete analytics workflow, from data generation and ETL to SQL analysis and interactive Tableau dashboard development.


## Dashboard Preview

Below is the interactive Tableau dashboard built for this project.
<img width="1920" height="1044" alt="dashboard" src="https://github.com/user-attachments/assets/18daf4b0-a8ff-49c1-bf8e-669d6c5d1611" />


# Project Overview

Modern product teams rely on user behavior data to understand engagement, monitor product performance, and support business decisions. This project simulates a real-world product analytics environment by generating synthetic user activity and building an executive dashboard to analyze user behavior.

The project follows a complete analytics pipeline:

- Generate realistic product data using Python
- Load data into MySQL
- Analyze user activity with SQL
- Build an interactive Tableau dashboard
- Present business insights through visual analytics


# Business Problem

Product managers and analysts need answers to questions such as:

- How many users actively use the platform?
- Which product features receive the most engagement?
- Which devices and operating systems are most popular?
- How has user growth changed over time?
- Who are the most engaged users?
- How long do users spend during each session?

This project was designed to answer those questions through an interactive analytics dashboard.


# Technologies Used

- Python
- Pandas
- NumPy
- Faker
- SQLAlchemy
- MySQL
- SQL
- Tableau
- GitHub


# Dataset

Synthetic data was generated using Python and the Faker library to simulate user activity on a social media platform.

| Dataset | Records |
|---------|---------:|
| Users | 1,000 |
| Sessions | 16,099 |
| Posts | 10,000 |
| Events | 202,003 |
| Ad Clicks | 25,762 |

The dataset includes:

- User profiles
- Login sessions
- Product interaction events
- User-generated posts
- Advertisement clicks


# Project Workflow

## 1. Data Generation

Python scripts were developed to generate realistic synthetic datasets representing user behavior within a social media application.

Generated datasets include:

- Users
- Sessions
- Posts
- Events
- Advertisement Clicks


## 2. ETL Pipeline

The generated CSV files were imported into MySQL using a Python ETL pipeline.

The ETL process included:

- Loading CSV files
- Creating database tables
- Maintaining table relationships
- Validating imported records

## 3. SQL Analysis

SQL queries were used to validate the data and analyze product metrics including:

- User counts
- Session counts
- Event distribution
- Device usage
- Operating system usage
- Session duration
- User engagement


## 4. Tableau Dashboard

An interactive executive dashboard was built in Tableau to visualize product performance and user engagement.

Dashboard filters allow users to explore the data by:

- Country
- Device
- Operating System


# Dashboard Features

The dashboard includes:

- Total Users
- Total Sessions
- Total Posts
- Total Events
- Total Ad Clicks
- Event Distribution
- User Growth Trend
- User Engagement Distribution
- Country Engagement
- Device Usage
- Operating System Distribution
- Average Session Duration by Device
- User Session Frequency


# Key Insights

- Most users belong to the Casual User segment, while a small number of Power Users generate the highest engagement.
- Viewing the feed is the most common user activity across the platform.
- User growth remains relatively stable over time.
- User activity is distributed across multiple countries, devices, and operating systems.
- Session duration varies slightly by device, providing insights into user behavior across platforms.


# Repository Structure

Meta_Product_Analytics/
│
├── data/
│   ├── users.csv
│   ├── sessions.csv
│   ├── posts.csv
│   ├── events.csv
│   └── ad_clicks.csv
│
├── ETL/
│   ├── generate_data.py
│   ├── generate_events.py
│   └── load_to_mysql.py
│
├── SQL/
│   ├── schema.sql
│   └── analysis_queries.sql
│
├── Tableau/
│   ├── Meta_Product_Analytics.twbx
│   └── dashboard.png
│
├── requirements.txt
└── README.md

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/meta-product-analytics-dashboard.git
```

Navigate to the project folder:

```bash
cd meta-product-analytics-dashboard
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

# Requirements

The project uses the following Python libraries:

- pandas
- numpy
- Faker
- SQLAlchemy
- mysql-connector-python


# Future Improvements

Possible future enhancements include:

- Cohort retention analysis
- Funnel analysis
- A/B testing metrics
- User churn prediction
- Cloud database integration
- Real-time dashboard updates


# Author

**Maedot Elias**

M.S. Data Analytics  
University of Nevada, Las Vegas

**Skills:** SQL • Python • Tableau • MySQL • Data Analytics • Business Intelligence

GitHub: https://github.com/MaedotEliasWoldeyes

LinkedIn: https://linkedin.com/in/yourprofile

Tableau Public: https://public.tableau.com/app/profile/yourprofile
