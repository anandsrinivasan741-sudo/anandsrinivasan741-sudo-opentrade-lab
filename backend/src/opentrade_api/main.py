from fastapi import FastAPI

from .analytics import calculate_pnl
from .schemas import PnLRequest, PnLResponse

app = FastAPI(
    title="OpenTrade Lab API",
    version="0.1.0",
    description="Research and market-analysis API. Not financial advice.",
)


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "opentrade-api"}


@app.get("/api/v1", tags=["system"])
def api_info() -> dict[str, str]:
    return {"status": "ok", "data_mode": "historical-or-live", "disclaimer": "Research only"}


@app.post("/api/v1/analytics/pnl", response_model=PnLResponse, tags=["analytics"])
def pnl(request: PnLRequest) -> PnLResponse:
    return calculate_pnl(request)
