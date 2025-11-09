"""
Calculation utilities for PnL grid generation
"""

import numpy as np
from black_scholes import calculate_call_price, calculate_put_price


def calculate_pnl_grids(spot_prices, volatilities, strike_price, time_to_maturity, 
                        risk_free_rate, purchase_price):
    """
    Calculate PnL grids for both call and put options.
    
    Args:
        spot_prices (np.array): Array of spot prices
        volatilities (np.array): Array of volatilities
        strike_price (float): Strike price
        time_to_maturity (float): Time to maturity in years
        risk_free_rate (float): Risk-free interest rate
        purchase_price (float): Purchase price of the option
        
    Returns:
        tuple: (call_pnl_grid, put_pnl_grid) as numpy arrays
    """
    grid_size = len(spot_prices)
    call_pnl_grid = np.zeros((grid_size, grid_size))
    put_pnl_grid = np.zeros((grid_size, grid_size))
    
    for i, spot in enumerate(spot_prices):
        for j, vol in enumerate(volatilities):
            call_price = calculate_call_price(
                spot, strike_price, time_to_maturity, risk_free_rate, vol
            )
            put_price = calculate_put_price(
                spot, strike_price, time_to_maturity, risk_free_rate, vol
            )
            
            call_pnl_grid[i, j] = call_price - purchase_price
            put_pnl_grid[i, j] = put_price - purchase_price
    
    return call_pnl_grid, put_pnl_grid

