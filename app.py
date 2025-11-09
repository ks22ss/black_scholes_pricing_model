"""
Option Pricing and Risk Analyzer
Main Streamlit application with Black-Scholes pricing model
"""

import streamlit as st
import numpy as np
from black_scholes import calculate_call_price, calculate_put_price
from database import init_database, save_calculation

# UI imports
from ui.styling import get_dark_mode_css
from ui.sidebar import render_sidebar
from ui.components import render_title, render_parameters_table, render_value_box

# Utils imports
from utils.calculations import calculate_pnl_grids
from utils.heatmap import create_heatmap_figure

# Page configuration
st.set_page_config(
    page_title="Option Pricing and Risk Analyzer",
    page_icon="📊",
    layout="wide"
)

# Apply dark mode CSS
st.markdown(get_dark_mode_css(), unsafe_allow_html=True)

# Initialize database
if 'db_conn' not in st.session_state:
    st.session_state.db_conn = init_database()

# Render sidebar and get input parameters
params = render_sidebar()

# Main dashboard
render_title()

# Calculate option prices
call_value = calculate_call_price(
    params['current_asset_price'], 
    params['strike_price'], 
    params['time_to_maturity'], 
    params['risk_free_rate'], 
    params['volatility']
)
put_value = calculate_put_price(
    params['current_asset_price'], 
    params['strike_price'], 
    params['time_to_maturity'], 
    params['risk_free_rate'], 
    params['volatility']
)

# Display input parameters table
render_parameters_table(params)

# Generate heatmap data
# Create 10x10 grid
grid_size = 10
spot_prices = np.linspace(params['min_spot_price'], params['max_spot_price'], grid_size)
volatilities = np.linspace(params['min_volatility'], params['max_volatility'], grid_size)

# Calculate PnL grids
call_pnl_grid, put_pnl_grid = calculate_pnl_grids(
    spot_prices,
    volatilities,
    params['strike_price'],
    params['time_to_maturity'],
    params['risk_free_rate'],
    params['purchase_price']
)

# Create heatmaps
col1, col2 = st.columns(2)

with col1:
    # Display Call Value box
    render_value_box(call_value, 'call')
    
    # Create and display heatmap
    fig_call = create_heatmap_figure(
        call_pnl_grid,
        spot_prices,
        volatilities,
        "PnL ($)"
    )
    st.plotly_chart(fig_call, width='content')

with col2:
    # Display Put Value box
    render_value_box(put_value, 'put')
    
    # Create and display heatmap
    fig_put = create_heatmap_figure(
        put_pnl_grid,
        spot_prices,
        volatilities,
        "PnL ($)"
    )
    st.plotly_chart(fig_put, width='content')

# Save to database button
st.markdown("<br>", unsafe_allow_html=True)
if st.button("Save to Database", type="primary"):
    # Prepare input parameters
    input_params = {
        'StockPrice': params['current_asset_price'],
        'StrikePrice': params['strike_price'],
        'InterestRate': params['risk_free_rate'],
        'Volatility': params['volatility'],
        'TimeToMaturity': params['time_to_maturity']
    }
    
    # Prepare heatmap data
    heatmap_data = []
    
    # Add call option data
    for i, spot in enumerate(spot_prices):
        for j, vol in enumerate(volatilities):
            call_price = calculate_call_price(
                spot, params['strike_price'], params['time_to_maturity'], 
                params['risk_free_rate'], vol
            )
            heatmap_data.append({
                'VolatilityShock': vol,
                'StockPriceShock': spot,
                'OptionPrice': call_price,
                'IsCall': True
            })
    
    # Add put option data
    for i, spot in enumerate(spot_prices):
        for j, vol in enumerate(volatilities):
            put_price = calculate_put_price(
                spot, params['strike_price'], params['time_to_maturity'], 
                params['risk_free_rate'], vol
            )
            heatmap_data.append({
                'VolatilityShock': vol,
                'StockPriceShock': spot,
                'OptionPrice': put_price,
                'IsCall': False
            })
    
    # Save to database
    try:
        calculation_id = save_calculation(
            st.session_state.db_conn, 
            input_params, 
            heatmap_data
        )
        st.success(f"✅ Calculation saved successfully! Calculation ID: {calculation_id}")
    except Exception as e:
        st.error(f"❌ Error saving to database: {str(e)}")
