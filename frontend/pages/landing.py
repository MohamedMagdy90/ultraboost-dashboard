import random
from datetime import datetime, timedelta
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from frontend.st_utils import initialize_st_page
initialize_st_page(
    layout="wide",
    show_readme=False
)
# Custom CSS for enhanced styling with BoostNova branding
st.markdown("""
<style>
    .metric-card {
        background: linear-gradient(135deg, #FF8C00 0%, #FFD700 100%);
        padding: 1rem;
        border-radius: 10px;
        color: #1a1a2e;
        margin: 0.5rem 0;
    }
    .feature-card {
        background: rgba(255, 140, 0, 0.1);
        border: 1px solid rgba(255, 215, 0, 0.3);
        border-radius: 15px;
        padding: 1.5rem;
        backdrop-filter: blur(10px);
        margin: 1rem 0;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #FF8C00;
    }
    .pulse {
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    .status-active {
        color: #4CAF50;
        font-weight: bold;
    }
    .status-inactive {
        color: #ff6b6b;
        font-weight: bold;
    }
    .boostnova-gradient {
        background: linear-gradient(135deg, #FF8C00 0%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
</style>
""", unsafe_allow_html=True)
# Hero Section
st.markdown("""
<div style="text-align: center; padding: 2rem 0;">
    <h1 style="font-size: 3rem; margin-bottom: 0.5rem;">
        <span style="background: linear-gradient(135deg, #FF8C00 0%, #FFD700 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">UltraBoost Dashboard</span>
    </h1>
    <p style="font-size: 1.2rem; color: #888; margin-bottom: 0.5rem;">
        Your Command Center for Algorithmic Trading Excellence
    </p>
    <p style="font-size: 0.9rem; color: #FFD700;">
        Powered by BoostNova
    </p>
</div>
""", unsafe_allow_html=True)
# Generate sample data for demonstration
def generate_sample_data():
    """Generate sample trading data for visualization"""
    dates = pd.date_range(start=datetime.now() - timedelta(days=30), end=datetime.now(), freq='D')
    # Sample portfolio performance
    portfolio_values = []
    base_value = 10000
    for i in range(len(dates)):
        change = random.uniform(-0.02, 0.03)  # -2% to +3% daily change
        base_value *= (1 + change)
        portfolio_values.append(base_value)
    return pd.DataFrame({
        'date': dates,
        'portfolio_value': portfolio_values,
        'daily_return': [random.uniform(-0.05, 0.08) for _ in range(len(dates))]
    })
# Quick Stats Dashboard
st.markdown("## Live Dashboard Overview")
# Mock data warning
st.warning("""
**Demo Data Notice**: The metrics, charts, and statistics shown below are simulated/mocked data for demonstration purposes.
This showcases how real trading data would be presented in the dashboard once connected to live UltraBoost trading bots.
""")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>Active Bots</h3>
        <div class="stat-number pulse" style="color: #1a1a2e;">3</div>
        <p>Currently Trading</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>Total Portfolio</h3>
        <div class="stat-number" style="color: #1a1a2e;">$12,847</div>
        <p style="color: #2e7d32;">+2.3% Today</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>Win Rate</h3>
        <div class="stat-number" style="color: #1a1a2e;">74.2%</div>
        <p>Last 30 Days</p>
    </div>
    """, unsafe_allow_html=True)
with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>Total Trades</h3>
        <div class="stat-number" style="color: #1a1a2e;">1,247</div>
        <p>This Month</p>
    </div>
    """, unsafe_allow_html=True)
st.divider()
# Performance Chart
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("### Portfolio Performance (30 Days)")
    # Generate and display sample performance chart
    df = generate_sample_data()
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df['date'],
        y=df['portfolio_value'],
        mode='lines+markers',
        line=dict(color='#FF8C00', width=3),
        fill='tonexty',
        fillcolor='rgba(255, 140, 0, 0.1)',
        name='Portfolio Value'
    ))
    fig.update_layout(
        template='plotly_dark',
        height=400,
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,215,0,0.1)')
    )
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.markdown("### Strategy Status")
    strategies = [
        {"name": "Market Making", "status": "active", "pnl": "+$342"},
        {"name": "Arbitrage", "status": "active", "pnl": "+$156"},
        {"name": "Grid Trading", "status": "active", "pnl": "+$89"},
        {"name": "DCA Bot", "status": "inactive", "pnl": "+$234"},
    ]
    for strategy in strategies:
        status_class = "status-active" if strategy["status"] == "active" else "status-inactive"
        status_icon = "Active" if strategy["status"] == "active" else "Inactive"
        status_color = "#4CAF50" if strategy["status"] == "active" else "#ff6b6b"
        st.markdown(f"""
        <div style="background: rgba(255,140,0,0.1); padding: 1rem; border-radius: 8px; margin: 0.5rem 0; border: 1px solid rgba(255,215,0,0.2);">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <strong>{strategy['name']}</strong><br>
                    <span style="color: {status_color}; font-weight: bold;">{status_icon}</span>
                </div>
                <div style="text-align: right;">
                    <span style="color: #4CAF50; font-weight: bold;">{strategy['pnl']}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
st.divider()
# Feature Showcase
st.markdown("## Platform Features")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="feature-card">
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="font-size: 3rem; color: #FF8C00;">Strategy</div>
            <h3>Strategy Development</h3>
        </div>
        <ul style="list-style: none; padding: 0;">
            <li>Visual Strategy Builder</li>
            <li>Advanced Configuration</li>
            <li>Custom Parameters</li>
            <li>Testing Environment</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="feature-card">
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="font-size: 3rem; color: #FFD700;">Analytics</div>
            <h3>Analytics & Insights</h3>
        </div>
        <ul style="list-style: none; padding: 0;">
            <li>Real-time Performance</li>
            <li>Advanced Backtesting</li>
            <li>Detailed Reports</li>
            <li>Interactive Charts</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div class="feature-card">
        <div style="text-align: center; margin-bottom: 1rem;">
            <div style="font-size: 3rem; color: #FF8C00;">Trading</div>
            <h3>Live Trading</h3>
        </div>
        <ul style="list-style: none; padding: 0;">
            <li>Automated Execution</li>
            <li>Real-time Monitoring</li>
            <li>Risk Management</li>
            <li>Smart Alerts</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
st.divider()
# Quick Actions
st.markdown("## Quick Actions")
# Alert for mocked navigation
st.info("**Note**: This is the dashboard landing page. Use the sidebar navigation to access different features.")
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Deploy Strategy", use_container_width=True, type="primary"):
        st.info("Navigate to 'Launch Bot' in the sidebar to deploy strategies.")
with col2:
    if st.button("View Performance", use_container_width=True):
        st.info("Navigate to 'Bot Performance' in the sidebar to view performance.")
with col3:
    if st.button("Backtesting", use_container_width=True):
        st.info("Navigate to strategy configuration pages to run backtests.")
with col4:
    if st.button("Archived Bots", use_container_width=True):
        st.info("Navigate to 'Archived Bots' in the sidebar to view history.")
st.divider()
# Resources Section
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("### Getting Started")
    st.markdown("""
    Welcome to **UltraBoost Dashboard**, your comprehensive platform for algorithmic trading.
    **Key Features:**
    - Configure and deploy trading strategies
    - Monitor bot performance in real-time
    - Backtest strategies against historical data
    - Manage exchange credentials securely
    Use the sidebar navigation to explore different sections of the dashboard.
    """)
with col2:
    st.markdown("### Resources")
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FF8C00 0%, #FFD700 100%);
                padding: 1.5rem; border-radius: 15px; color: #1a1a2e;">
        <h4>UltraBoost Documentation</h4>
        <p>Learn how to configure and optimize your trading bots.</p>
        <br>
        <a href="https://github.com/MohamedMagdy90/UltraGrid" target="_blank"
           style="background: rgba(0,0,0,0.2); padding: 0.5rem 1rem;
                  border-radius: 8px; text-decoration: none; color: #1a1a2e; font-weight: bold;">
           View on GitHub
        </a>
    </div>
    """, unsafe_allow_html=True)
# Footer stats
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Supported Exchanges", "20+")
with col2:
    st.metric("Trading Strategies", "10+")
with col3:
    st.metric("Active Connectors", "30+")
with col4:
    st.metric("Open Source", "Apache 2.0")
# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem 0; color: #666;">
    <p><strong>UltraBoost Dashboard</strong> - Built with BoostNova</p>
</div>
""", unsafe_allow_html=True)