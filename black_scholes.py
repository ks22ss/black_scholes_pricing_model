"""
Black-Scholes Option Pricing Model
Implements the Black-Scholes formula for European call and put options
"""

import numpy as np
from scipy.stats import norm


def calculate_call_price(S, K, T, r, sigma):
    """
    Calculate Black-Scholes call option price
    
    Parameters:
    S (float): Current stock/asset price
    K (float): Strike price
    T (float): Time to maturity (in years)
    r (float): Risk-free interest rate (annualized)
    sigma (float): Volatility (annualized)
    
    Returns:
    float: Call option price
    """
    if T <= 0 or sigma <= 0:
        return max(S - K, 0)
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    
    return max(call_price, 0)  # Ensure non-negative


def calculate_put_price(S, K, T, r, sigma):
    """
    Calculate Black-Scholes put option price using put-call parity
    
    Parameters:
    S (float): Current stock/asset price
    K (float): Strike price
    T (float): Time to maturity (in years)
    r (float): Risk-free interest rate (annualized)
    sigma (float): Volatility (annualized)
    
    Returns:
    float: Put option price
    """
    call_price = calculate_call_price(S, K, T, r, sigma)
    
    # Put-call parity: P = C - S + K * e^(-r*T)
    put_price = call_price - S + K * np.exp(-r * T)
    
    return max(put_price, 0)  # Ensure non-negative

