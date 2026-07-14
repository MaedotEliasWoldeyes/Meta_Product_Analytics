/*
=========================================================
Meta Product Analytics Project
Exploratory Data Analysis (EDA)

Author: Maedot E Woldeyes

Purpose:
Perform exploratory data analysis to understand
the structure, quality, and distribution of the
synthetic product analytics dataset before
performing business analysis.
=========================================================
*/

USE meta_product_analytics;

-- =====================================================
-- 1. Dataset Overview
-- =====================================================
-- Count the total number of events recorded in the
-- application.

SELECT
    COUNT(*) AS total_events
FROM events;

-- =====================================================
-- 2. Event Type Distribution
-- =====================================================
-- Identify which user actions occur most frequently
-- across the platform.

SELECT
    event_type,
    COUNT(*) AS event_count
FROM events
GROUP BY event_type
ORDER BY event_count DESC;

-- =====================================================
-- 3. Session Duration Summary
-- =====================================================
-- Calculate the average, shortest, and longest
-- session durations.

SELECT
    ROUND(AVG(session_duration), 2) AS avg_session_minutes,
    MIN(session_duration) AS shortest_session,
    MAX(session_duration) AS longest_session
FROM sessions;

-- =====================================================
-- 4. Session Duration Distribution
-- =====================================================
-- Group session durations into time buckets to
-- understand how long users typically stay active.

SELECT
    CASE
        WHEN session_duration < 5 THEN '0–5 Minutes'
        WHEN session_duration < 15 THEN '5–15 Minutes'
        WHEN session_duration < 30 THEN '15–30 Minutes'
        WHEN session_duration < 60 THEN '30–60 Minutes'
        ELSE '60+ Minutes'
    END AS session_bucket,

    COUNT(*) AS total_sessions

FROM sessions

GROUP BY session_bucket

ORDER BY MIN(session_duration);

-- =====================================================
-- 5. Average Events per Session
-- =====================================================
-- Measure user activity by calculating the average
-- number of events generated during a session.

SELECT

    ROUND(AVG(event_count), 2) AS avg_events_per_session

FROM (

    SELECT

        session_id,
        COUNT(*) AS event_count

    FROM events

    GROUP BY session_id

) AS session_events;