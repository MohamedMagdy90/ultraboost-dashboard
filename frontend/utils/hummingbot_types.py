"""
Local implementation of Hummingbot types to avoid hummingbot dependency.
These are simple enums and classes used by the dashboard.
"""
from enum import Enum
from typing import Optional, Any
from dataclasses import dataclass


class OrderType(Enum):
    """Order type enum."""
    LIMIT = "LIMIT"
    MARKET = "MARKET"
    LIMIT_MAKER = "LIMIT_MAKER"

    def __str__(self):
        return self.value


class TradeType(Enum):
    """Trade type enum."""
    BUY = "BUY"
    SELL = "SELL"

    def __str__(self):
        return self.value


class PositionMode(Enum):
    """Position mode enum for futures trading."""
    ONEWAY = "ONEWAY"
    HEDGE = "HEDGE"

    def __str__(self):
        return self.value


@dataclass
class ExecutorInfo:
    """Executor info model for tracking trade executions."""
    id: str
    timestamp: float
    type: str
    status: str
    config: dict
    net_pnl_pct: float = 0.0
    net_pnl_quote: float = 0.0
    cum_fees_quote: float = 0.0
    filled_amount_quote: float = 0.0
    is_active: bool = False
    is_trading: bool = False
    custom_info: Optional[dict] = None
    controller_id: Optional[str] = None
    side: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> "ExecutorInfo":
        """Create ExecutorInfo from dictionary."""
        return cls(
            id=data.get("id", ""),
            timestamp=data.get("timestamp", 0.0),
            type=data.get("type", ""),
            status=data.get("status", ""),
            config=data.get("config", {}),
            net_pnl_pct=data.get("net_pnl_pct", 0.0),
            net_pnl_quote=data.get("net_pnl_quote", 0.0),
            cum_fees_quote=data.get("cum_fees_quote", 0.0),
            filled_amount_quote=data.get("filled_amount_quote", 0.0),
            is_active=data.get("is_active", False),
            is_trading=data.get("is_trading", False),
            custom_info=data.get("custom_info"),
            controller_id=data.get("controller_id"),
            side=data.get("side"),
        )
