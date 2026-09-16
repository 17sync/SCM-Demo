from calculator import calculate_discount

def test_regular_customer():
    assert calculate_discount(100, False)==10

def test_member_customer():
    assert calculate_discount(100, True)==20