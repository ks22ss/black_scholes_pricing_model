"""
Sidebar input components for the Option Pricing and Risk Analyzer application
"""

import streamlit as st


def render_sidebar():
    """
    Renders the sidebar with all input parameters and returns a dictionary
    containing all input values.
    
    Returns:
        dict: Dictionary containing:
            - current_asset_price (float)
            - strike_price (float)
            - time_to_maturity_days (int)
            - time_to_maturity (float) - converted to years
            - volatility (float)
            - risk_free_rate (float)
            - purchase_price (float)
            - min_spot_price (float)
            - max_spot_price (float)
            - min_volatility (float)
            - max_volatility (float)
    """
    with st.sidebar:
        st.header("Input Parameters")
        
        # Main input parameters
        current_asset_price = st.number_input(
            "Current Asset Price",
            min_value=0.01,
            value=100.0,
            step=0.01,
            format="%.2f"
        )
        
        strike_price = st.number_input(
            "Strike Price",
            min_value=0.01,
            value=100.0,
            step=0.01,
            format="%.2f"
        )
        
        time_to_maturity_days = st.number_input(
            "Time to Maturity (days)",
            min_value=1,
            value=365,
            step=1,
            format="%d"
        )
        
        # Convert days to years for calculations (1 year = 365 days)
        time_to_maturity = time_to_maturity_days / 365.0
        
        volatility = st.number_input(
            "Volatility",
            min_value=0.0,
            max_value=1.0,
            value=0.2,
            step=0.01,
            format="%.2f"
        )
        
        risk_free_rate = st.number_input(
            "Risk Free Rate",
            min_value=0.0,
            value=0.05,
            step=0.01,
            format="%.2f"
        )
        
        purchase_price = st.number_input(
            "Purchase Price",
            min_value=0.0,
            value=10.0,
            step=0.01,
            format="%.2f"
        )
        
        st.divider()
        st.header("Heatmap Range Settings")
        
        # Min/Max Spot Price sliders
        min_spot_price = st.slider(
            "Min Spot Price",
            min_value=0.01,
            max_value=500.0,
            value=80.0,
            step=0.01,
            format="%.2f"
        )
        
        max_spot_price = st.slider(
            "Max Spot Price",
            min_value=0.01,
            max_value=500.0,
            value=120.0,
            step=0.01,
            format="%.2f"
        )
        
        # Min/Max Volatility sliders
        min_volatility = st.slider(
            "Min Volatility",
            min_value=0.0,
            max_value=1.0,
            value=0.04,
            step=0.01,
            format="%.2f"
        )
        
        max_volatility = st.slider(
            "Max Volatility",
            min_value=0.0,
            max_value=1.0,
            value=0.30,
            step=0.01,
            format="%.2f"
        )
    
    return {
        'current_asset_price': current_asset_price,
        'strike_price': strike_price,
        'time_to_maturity_days': time_to_maturity_days,
        'time_to_maturity': time_to_maturity,
        'volatility': volatility,
        'risk_free_rate': risk_free_rate,
        'purchase_price': purchase_price,
        'min_spot_price': min_spot_price,
        'max_spot_price': max_spot_price,
        'min_volatility': min_volatility,
        'max_volatility': max_volatility
    }

