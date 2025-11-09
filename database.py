"""
Database operations for Black-Scholes calculations
Handles SQLite database creation and data storage
"""

import sqlite3
import os


def init_database(db_path='options.db'):
    """
    Initialize SQLite database and create tables if they don't exist
    
    Parameters:
    db_path (str): Path to the database file
    
    Returns:
    sqlite3.Connection: Database connection
    """
    conn = sqlite3.connect(db_path, check_same_thread=False)
    # Enable foreign key constraints
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()
    
    # Create BlackScholesInput table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BlackScholesInput (
            CalculationID INTEGER PRIMARY KEY AUTOINCREMENT,
            StockPrice REAL,
            StrikePrice REAL,
            InterestRate REAL,
            Volatility REAL,
            TimeToMaturity REAL
        )
    ''')
    
    # Create BlackScholesOutput table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BlackScholesOutput (
            CalculationOutputID INTEGER PRIMARY KEY AUTOINCREMENT,
            VolatilityShock REAL,
            StockPriceShock REAL,
            OptionPrice REAL,
            IsCall INTEGER,
            CalculationID INTEGER,
            FOREIGN KEY (CalculationID) REFERENCES BlackScholesInput(CalculationID)
        )
    ''')
    
    conn.commit()
    return conn


def save_calculation(conn, input_params, heatmap_data):
    """
    Save input parameters and heatmap data to database
    
    Parameters:
    conn (sqlite3.Connection): Database connection
    input_params (dict): Dictionary with keys: StockPrice, StrikePrice, InterestRate, Volatility, TimeToMaturity
    heatmap_data (list): List of dictionaries with keys: VolatilityShock, StockPriceShock, OptionPrice, IsCall
    
    Returns:
    int: CalculationID of the saved calculation
    """
    cursor = conn.cursor()
    
    # Insert input parameters
    cursor.execute('''
        INSERT INTO BlackScholesInput 
        (StockPrice, StrikePrice, InterestRate, Volatility, TimeToMaturity)
        VALUES (?, ?, ?, ?, ?)
    ''', (
        input_params['StockPrice'],
        input_params['StrikePrice'],
        input_params['InterestRate'],
        input_params['Volatility'],
        input_params['TimeToMaturity']
    ))
    
    calculation_id = cursor.lastrowid
    
    # Insert heatmap output data
    for data_point in heatmap_data:
        cursor.execute('''
            INSERT INTO BlackScholesOutput 
            (VolatilityShock, StockPriceShock, OptionPrice, IsCall, CalculationID)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            data_point['VolatilityShock'],
            data_point['StockPriceShock'],
            data_point['OptionPrice'],
            1 if data_point['IsCall'] else 0,
            calculation_id
        ))
    
    conn.commit()
    return calculation_id

