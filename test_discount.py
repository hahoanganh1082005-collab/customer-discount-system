from discount import calculate_discount

def test_TC01_vip_customer():
    assert calculate_discount(60000000) == 0.1

def test_TC02_normal_customer():
    assert calculate_discount(30000000) == 0

def test_TC03_boundary_non_vip_customer():
    assert calculate_discount(59999999) == 0
