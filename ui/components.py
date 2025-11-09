"""
Reusable UI components for the Option Pricing and Risk Analyzer application
"""

import streamlit as st
from .styling import get_title_css, get_params_box_css


def render_title():
    """Renders the main title with compact styling"""
    st.markdown(get_title_css(), unsafe_allow_html=True)
    st.title("Black-Scholes Pricing Model")


def render_parameters_table(params):
    """
    Renders the input parameters in a styled dark blue box.
    
    Args:
        params (dict): Dictionary containing:
            - current_asset_price (float)
            - volatility (float)
            - strike_price (float)
            - risk_free_rate (float)
            - time_to_maturity_days (int)
            - purchase_price (float)
    """
    st.markdown(get_params_box_css(), unsafe_allow_html=True)
    
    params_html = f"""
    <div class="params-box">
        <div class="params-row">
            <div class="param-item">
                <div class="param-label">Current Asset Price</div>
                <div class="param-value">${params['current_asset_price']:.2f}</div>
            </div>
            <div class="param-item">
                <div class="param-label">Volatility</div>
                <div class="param-value">{params['volatility']:.2%}</div>
            </div>
            <div class="param-item">
                <div class="param-label">Strike Price</div>
                <div class="param-value">${params['strike_price']:.2f}</div>
            </div>
            <div class="param-item">
                <div class="param-label">Risk Free Rate</div>
                <div class="param-value">{params['risk_free_rate']:.2%}</div>
            </div>
            <div class="param-item">
                <div class="param-label">Time To Maturity</div>
                <div class="param-value">{params['time_to_maturity_days']} days</div>
            </div>
            <div class="param-item">
                <div class="param-label">Purchase Price</div>
                <div class="param-value">${params['purchase_price']:.2f}</div>
            </div>
        </div>
    </div>
    """
    st.markdown(params_html, unsafe_allow_html=True)


def render_value_box(value, option_type='call'):
    """
    Renders a value display box for Call or Put option values.
    
    Args:
        value (float): The option value to display
        option_type (str): Either 'call' or 'put'
    """
    if option_type.lower() == 'call':
        st.markdown(
            f'<div class="call-value-box">CALL VALUE: ${value:.2f}</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="put-value-box">PUT VALUE: ${value:.2f}</div>',
            unsafe_allow_html=True
        )

