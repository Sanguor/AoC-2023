from calibrate import calculate_sum


test_data_54 ='''
    xt36five77\n
    two8five6zfrtjj\n
    eightthree8fiveqjgsdzgnnineeight\n
    7chmvlhnpfive\n
'''

def test_calculate_sum():
    expected_result = 54
    result = calculate_sum(test_data_54)
    assert result == expected_result