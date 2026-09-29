import pytest
from fastapi.testclient import TestClient

from opentrade_api.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_health(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_long_pnl_includes_costs(client: TestClient) -> None:
    response = client.post(
        "/api/v1/analytics/pnl",
        json={
            "side": "LONG",
            "entry_price": 100,
            "exit_price": 110,
            "quantity": 2,
            "fee_rate": 0.001,
            "slippage_rate": 0.0005,
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["gross_pnl"] == 20.0
    assert body["net_pnl"] < body["gross_pnl"]


def test_invalid_price_is_rejected(client: TestClient) -> None:
    response = client.post(
        "/api/v1/analytics/pnl",
        json={"side": "LONG", "entry_price": 0, "exit_price": 10, "quantity": 1},
    )
    assert response.status_code == 422
