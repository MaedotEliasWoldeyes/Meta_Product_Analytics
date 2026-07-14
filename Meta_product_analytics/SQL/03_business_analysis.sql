/*
=========================================================
Meta Product Analytics Project
Business Analysis Queries

Author: Maedot E. Woldeyes

Purpose:
Answer business questions about user behavior,
engagement, devices, account types, and platform usage.

These queries were used to create Tableau dashboards
and generate business insights.
=========================================================
*/

USE meta_product_analytics;

-- =====================================================
-- BUSINESS QUESTION 1
-- Which event types occur most frequently?
-- =====================================================
-- Purpose:
-- Identify the most common actions performed by users.
-- This helps understand how users interact with the app.

SELECT
    event_type,
    COUNT(*) AS total_events,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM events),
        2
    ) AS percentage
FROM events
GROUP BY event_type
ORDER BY total_events DESC;



-- =====================================================
-- BUSINESS QUESTION 2
-- Which countries have the highest user engagement?
-- =====================================================
-- Purpose:
-- Compare engagement across countries using average
-- events generated per active user.

SELECT
    u.country,
    COUNT(e.event_id) AS total_events,
    COUNT(DISTINCT s.user_id) AS active_users,
    ROUND(
        COUNT(e.event_id) /
        COUNT(DISTINCT s.user_id),
        2
    ) AS avg_events_per_user
FROM users u
JOIN sessions s
    ON u.user_id = s.user_id
JOIN events e
    ON s.session_id = e.session_id
GROUP BY u.country
ORDER BY avg_events_per_user DESC;



-- =====================================================
-- BUSINESS QUESTION 3
-- How are users distributed by activity level?
-- =====================================================
-- Purpose:
-- Segment users according to the number of sessions
-- they created.

SELECT
    CASE
        WHEN session_count = 1 THEN 'One-time users'
        WHEN session_count BETWEEN 2 AND 5 THEN 'Occasional users'
        WHEN session_count BETWEEN 6 AND 20 THEN 'Regular users'
        ELSE 'Power users'
    END AS user_segment,

    COUNT(*) AS users

FROM
(
    SELECT
        user_id,
        COUNT(session_id) AS session_count
    FROM sessions
    GROUP BY user_id
) AS user_sessions

GROUP BY user_segment
ORDER BY users DESC;



-- =====================================================
-- BUSINESS QUESTION 4
-- Which actions are performed by each user segment?
-- =====================================================
-- Purpose:
-- Compare behavioral differences between One-time,
-- Occasional, Regular, and Power users.

SELECT

    CASE
        WHEN session_count = 1 THEN 'One-time'
        WHEN session_count BETWEEN 2 AND 5 THEN 'Occasional'
        WHEN session_count BETWEEN 6 AND 20 THEN 'Regular'
        ELSE 'Power'
    END AS user_segment,

    e.event_type,

    COUNT(*) AS events

FROM events e

JOIN sessions s
    ON e.session_id = s.session_id

JOIN
(
    SELECT
        user_id,
        COUNT(session_id) AS session_count
    FROM sessions
    GROUP BY user_id
) us
    ON s.user_id = us.user_id

GROUP BY
    user_segment,
    e.event_type

ORDER BY
    user_segment,
    events DESC;



-- =====================================================
-- BUSINESS QUESTION 5
-- Which devices generate the highest engagement?
-- =====================================================
-- Purpose:
-- Compare average events per user across different
-- devices.

SELECT

    s.device,

    COUNT(e.event_id) AS total_events,

    COUNT(DISTINCT s.user_id) AS users,

    ROUND(
        COUNT(e.event_id) /
        COUNT(DISTINCT s.user_id),
        2
    ) AS avg_events_per_user

FROM sessions s

JOIN events e
    ON s.session_id = e.session_id

GROUP BY s.device

ORDER BY avg_events_per_user DESC;



-- =====================================================
-- BUSINESS QUESTION 6
-- Which account types are the most engaged?
-- =====================================================
-- Purpose:
-- Compare engagement among Personal, Creator,
-- and Business accounts.

SELECT

    u.account_type,

    COUNT(e.event_id) AS total_events,

    COUNT(DISTINCT u.user_id) AS users,

    ROUND(
        COUNT(e.event_id) /
        COUNT(DISTINCT u.user_id),
        2
    ) AS avg_events_per_user

FROM users u

JOIN sessions s
    ON u.user_id = s.user_id

JOIN events e
    ON s.session_id = e.session_id

GROUP BY u.account_type

ORDER BY avg_events_per_user DESC;



-- =====================================================
-- BUSINESS QUESTION 7
-- Who are the most active users?
-- =====================================================
-- Purpose:
-- Identify users with the highest overall activity.

SELECT

    s.user_id,

    COUNT(e.event_id) AS total_events,

    COUNT(DISTINCT s.session_id) AS total_sessions

FROM sessions s

JOIN events e
    ON s.session_id = e.session_id

GROUP BY s.user_id

ORDER BY total_events DESC

LIMIT 10;