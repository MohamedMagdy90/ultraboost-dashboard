"""
UltraBoost Dashboard Theme
Powered by BoostNova
"""
def get_default_layout(title=None, height=800, width=1800):
    layout = {
        "template": "plotly_dark",
        "plot_bgcolor": 'rgba(0, 0, 0, 0)',
        "paper_bgcolor": 'rgba(26, 26, 46, 0.8)',
        "font": {"color": '#fafafa', "size": 12},
        "height": height,
        "width": width,
        "margin": {"l": 20, "r": 20, "t": 50, "b": 20},
        "xaxis_rangeslider_visible": False,
        "hovermode": "x unified",
        "showlegend": False,
    }
    if title:
        layout["title"] = title
    return layout
def get_color_scheme():
    """BoostNova color scheme for UltraBoost Dashboard"""
    return {
        'primary': '#FF8C00',
        'secondary': '#FFD700',
        'upper_band': '#FFD700',
        'middle_band': '#FF8C00',
        'lower_band': '#FFA500',
        'buy_signal': '#4CAF50',
        'sell_signal': '#FF5252',
        'buy': '#4CAF50',
        'sell': '#FF5252',
        'macd_line': '#FF8C00',
        'macd_signal': '#FFD700',
        'macd_histogram_positive': '#4CAF50',
        'macd_histogram_negative': '#FF5252',
        'spread': '#00BFFF',
        'break_even': '#FFD700',
        'take_profit': '#4CAF50',
        'order_amount': '#FF8C00',
        'cum_amount': '#FFD700',
        'stop_loss': '#FF5252',
        'cum_unrealized_pnl': '#FFA07A',
        'volume': '#FFD700',
        'price': '#FF8C00',
    }