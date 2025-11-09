"""
Heatmap generation and visualization utilities
"""

import numpy as np
import plotly.graph_objects as go


def create_colorscale(pnl_grid):
    """
    Create a custom colorscale based on PnL values.
    Negative values = red (lighter near 0, darker for lower)
    Positive values = green (lighter near 0, darker for higher)
    
    Args:
        pnl_grid (np.array): 2D array of PnL values
        
    Returns:
        list: Plotly colorscale format
    """
    min_pnl = np.min(pnl_grid)
    max_pnl = np.max(pnl_grid)
    
    # Create colorscale with 0 as the breakpoint
    if min_pnl < 0 and max_pnl > 0:
        # Both negative and positive values exist - normalize to find where 0 is
        zero_pos = -min_pnl / (max_pnl - min_pnl) if max_pnl != min_pnl else 0.5
        custom_colorscale = [
            [0.0, '#ff6666'],           # Darker red for most negative
            [zero_pos * 0.7, '#ff9999'], # Medium red
            [zero_pos, '#ffcccc'],      # Light red at zero
            [zero_pos + (1 - zero_pos) * 0.3, '#ccffcc'],  # Light green
            [1.0, '#66ff66']            # Darker green for most positive
        ]
    elif max_pnl <= 0:
        # All negative values - lighter red near 0, darker red for lower values
        custom_colorscale = [
            [0.0, '#ff6666'],  # Darker red for most negative
            [0.5, '#ff9999'],  # Medium red
            [1.0, '#ffcccc']   # Light red for least negative (closest to 0)
        ]
    else:
        # All positive values - lighter green near 0, darker green for higher values
        custom_colorscale = [
            [0.0, '#ccffcc'],   # Light green for least positive (closest to 0)
            [0.5, '#99ff99'],  # Medium green
            [1.0, '#66ff66']   # Darker green for most positive
        ]
    
    return custom_colorscale


def generate_hover_text(spot_prices, volatilities, pnl_grid):
    """
    Generate hover text for heatmap cells with black color.
    
    Args:
        spot_prices (np.array): Array of spot prices
        volatilities (np.array): Array of volatilities
        pnl_grid (np.array): 2D array of PnL values
        
    Returns:
        np.array: 2D array of hover text strings
    """
    grid_size = len(spot_prices)
    hover_text = np.empty((grid_size, grid_size), dtype=object)
    
    for i in range(grid_size):
        for j in range(grid_size):
            hover_text[i, j] = (
                f"<span style='color: black;'>Spot Price: ${spot_prices[i]:.2f}<br>"
                f"Volatility: {volatilities[j]:.2%}<br>"
                f"PnL: ${pnl_grid[i, j]:.2f}</span>"
            )
    
    return hover_text


def create_heatmap_figure(pnl_grid, spot_prices, volatilities, title="PnL ($)"):
    """
    Create a Plotly heatmap figure with custom styling.
    
    Args:
        pnl_grid (np.array): 2D array of PnL values
        spot_prices (np.array): Array of spot prices for y-axis
        volatilities (np.array): Array of volatilities for x-axis
        title (str): Title for the colorbar
        
    Returns:
        go.Figure: Plotly figure object
    """
    grid_size = len(spot_prices)
    
    # Generate hover text
    hover_text = generate_hover_text(spot_prices, volatilities, pnl_grid)
    
    # Create colorscale
    custom_colorscale = create_colorscale(pnl_grid)
    
    # Create figure
    fig = go.Figure(data=go.Heatmap(
        z=pnl_grid,
        x=[f"{v:.2%}" for v in volatilities],
        y=[f"${s:.2f}" for s in spot_prices],
        colorscale=custom_colorscale,
        text=[[f"${pnl_grid[i, j]:.2f}" for j in range(grid_size)] for i in range(grid_size)],
        texttemplate='%{text}',
        textfont={"size": 16, "color": "black"},
        hovertext=hover_text,
        hoverinfo='text',
        colorbar=dict(title=title)
    ))
    
    # Update layout
    fig.update_layout(
        xaxis_title="Volatility(%)",
        yaxis_title="Spot Price($)",
        height=700,
        width=700,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#fafafa', size=14),
        autosize=False,
        xaxis=dict(
            showgrid=False, 
            constrain='domain',
            title_font=dict(size=18, color='#fafafa'),
            tickfont=dict(size=14, color='#fafafa'),
            fixedrange=True
        ),
        yaxis=dict(
            showgrid=False, 
            constrain='domain',
            title_font=dict(size=18, color='#fafafa'),
            tickfont=dict(size=14, color='#fafafa'),
            fixedrange=True
        )
    )
    
    # Update colorbar separately using update_traces
    fig.update_traces(
        colorbar=dict(
            title=dict(text=title, font=dict(size=16, color='#fafafa')),
            tickfont=dict(size=14, color='#fafafa')
        )
    )
    
    return fig

