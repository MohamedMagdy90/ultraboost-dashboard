"""
Performance Data Source stub for dashboard compatibility.
This is a placeholder that allows the dashboard to function without the full backend.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import pandas as pd


@dataclass
class PerformanceDataSource:
    """Data source for bot performance metrics."""
    
    executors: List[Dict[str, Any]] = field(default_factory=list)
    processed_data: Optional[pd.DataFrame] = None
    
    def __init__(self, executors: List[Dict[str, Any]] = None):
        self.executors = executors or []
        self.processed_data = pd.DataFrame()
    
    @classmethod
    def from_backtesting_results(cls, backtesting_results: Dict[str, Any]) -> "PerformanceDataSource":
        """Create from backtesting results."""
        executors = backtesting_results.get("executors", [])
        processed_data = backtesting_results.get("processed_data", {})
        
        instance = cls(executors=executors)
        if processed_data:
            instance.processed_data = pd.DataFrame(processed_data)
        return instance
    
    @classmethod
    def from_controller_data(cls, controller_data: Dict[str, Any]) -> "PerformanceDataSource":
        """Create from controller performance data."""
        return cls(executors=controller_data.get("executors", []))
    
    def get_executors_df(self) -> pd.DataFrame:
        """Get executors as DataFrame."""
        if not self.executors:
            return pd.DataFrame()
        return pd.DataFrame(self.executors)
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """Get summary statistics."""
        df = self.get_executors_df()
        if df.empty:
            return {
                "total_executors": 0,
                "total_pnl": 0.0,
                "win_rate": 0.0,
                "avg_pnl": 0.0,
            }
        
        return {
            "total_executors": len(df),
            "total_pnl": df.get("net_pnl_quote", pd.Series([0])).sum(),
            "win_rate": (df.get("net_pnl_quote", pd.Series([0])) > 0).mean() * 100,
            "avg_pnl": df.get("net_pnl_quote", pd.Series([0])).mean(),
        }
