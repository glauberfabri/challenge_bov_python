from app.services.production_service import is_bonus_applicable, get_semester

def test_is_bonus_applicable():
    assert is_bonus_applicable(15000) == True
    assert is_bonus_applicable(8000) == False

def test_get_semester():
    assert get_semester("2025-01-15") == "first"
    assert get_semester("2025-07-15") == "second"