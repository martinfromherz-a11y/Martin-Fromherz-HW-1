from energy_market_calculation import (
    calculate_cost,
    calculate_revenue,
    calculate_profit,
)


def test_calculate_cost():
    assert calculate_cost(100, 0.2) == 20


def test_calculate_revenue():
    assert calculate_revenue(200, 0.1) == 20


def test_calculate_profit():
    assert calculate_profit(50, 30) == 20