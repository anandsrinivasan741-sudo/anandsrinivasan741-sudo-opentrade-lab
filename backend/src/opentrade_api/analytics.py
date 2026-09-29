from .schemas import PnLRequest, PnLResponse


def calculate_pnl(request: PnLRequest) -> PnLResponse:
    entry_value = request.entry_price * request.quantity
    exit_value = request.exit_price * request.quantity
    gross = exit_value - entry_value if request.side == "LONG" else entry_value - exit_value
    slippage = exit_value * request.slippage_rate
    fees = (entry_value + exit_value) * request.fee_rate
    net = gross - fees - slippage
    total_cost_rate = 2 * request.fee_rate + request.slippage_rate
    break_even = request.entry_price * (1 + total_cost_rate) if request.side == "LONG" else request.entry_price * (1 - total_cost_rate)
    return PnLResponse(side=request.side, gross_pnl=round(gross, 8), fees=round(fees, 8), slippage=round(slippage, 8), net_pnl=round(net, 8), break_even_exit_price=round(break_even, 8))
