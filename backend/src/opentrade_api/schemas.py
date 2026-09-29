from enum import StrEnum
from pydantic import BaseModel, Field


class DataStatus(StrEnum):
    LIVE = "LIVE"
    DELAYED = "DELAYED"
    HISTORICAL = "HISTORICAL"
    SIMULATED = "SIMULATED"
    ERROR = "ERROR"


class PnLRequest(BaseModel):
    side: str = Field(pattern="^(LONG|SHORT)$")
    entry_price: float = Field(gt=0)
    exit_price: float = Field(gt=0)
    quantity: float = Field(gt=0)
    fee_rate: float = Field(default=0.001, ge=0, lt=1)
    slippage_rate: float = Field(default=0, ge=0, lt=1)


class PnLResponse(BaseModel):
    side: str
    gross_pnl: float
    fees: float
    slippage: float
    net_pnl: float
    break_even_exit_price: float


class IndicatorResponse(BaseModel):
    symbol: str
    interval: str
    status: DataStatus
    values: list[dict[str, float | int | str]]
    message: str | None = None
