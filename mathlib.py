import sample

def test_cal_square_1():
    result = sample.calc(5)
    assert result == 25

def test_cal_square_2():
    result = sample.calc(6)
    assert result == 36

def test_cal_square_3():
    result = sample.calc(7)
    assert result == 49

def test_cal_square_4():
    result = sample.calc(8)
    assert result == 64
