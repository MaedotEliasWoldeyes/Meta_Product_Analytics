/*
=========================================================
Meta Product Analytics Project
Database Setup

Author: Maedot E Woldeyes

Purpose:
Create the MySQL database, user account,
permissions, and all tables required for the
Meta Product Analytics ETL pipeline.
=========================================================
*/

-- =====================================================
-- Create Database User
-- =====================================================

CREATE USER 'meta_user'@'localhost'
IDENTIFIED BY 'Meta123!';

GRANT ALL PRIVILEGES
ON meta_product_analytics.*
TO 'meta_user'@'localhost';

FLUSH PRIVILEGES;

-- =====================================================
-- Create Database
-- =====================================================

CREATE DATABASE meta_product_analytics;

USE meta_product_analytics;

SHOW DATABASES;

-- =====================================================
-- Users Table
-- =====================================================

CREATE TABLE users (

    user_id INT PRIMARY KEY,

    signup_date DATETIME,

    country VARCHAR(100),

    age INT,

    gender VARCHAR(20),

    account_type VARCHAR(50),

    language VARCHAR(50),

    referral_source VARCHAR(100),

    email_verified BOOLEAN

);

-- =====================================================
-- Sessions Table
-- =====================================================

CREATE TABLE sessions (

    session_id INT PRIMARY KEY,

    user_id INT,

    device VARCHAR(50),

    operating_system VARCHAR(50),

    login_time DATETIME,

    logout_time DATETIME,

    session_duration INT,

    FOREIGN KEY (user_id)
        REFERENCES users(user_id)

);

-- =====================================================
-- Posts Table
-- =====================================================

CREATE TABLE posts (

    post_id INT PRIMARY KEY,

    creator_id INT,

    category VARCHAR(100),

    created_time DATETIME,

    privacy VARCHAR(50),

    FOREIGN KEY (creator_id)
        REFERENCES users(user_id)

);

-- =====================================================
-- Events Table
-- =====================================================

CREATE TABLE events (

    event_id INT PRIMARY KEY,

    session_id INT,

    event_type VARCHAR(100),

    event_time DATETIME,

    FOREIGN KEY (session_id)
        REFERENCES sessions(session_id)

);

-- =====================================================
-- Advertisement Clicks Table
-- =====================================================

CREATE TABLE ad_clicks (

    ad_id INT PRIMARY KEY,

    event_id INT,

    ad_category VARCHAR(100),

    clicked BOOLEAN,

    FOREIGN KEY (event_id)
        REFERENCES events(event_id)

);