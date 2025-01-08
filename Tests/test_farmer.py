from app.services.farmer_service import calculate_price

def test_calculate_price():
    assert calculate_price(10000, 40, True, "first") == 18000.0
    assert calculate_price(12000, 60, False, "second") == 23160.0