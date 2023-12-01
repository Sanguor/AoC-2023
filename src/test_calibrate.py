from calibrate import calculate_sum


test_data_54 ='''
    xt36five77\n
    two8five6zfrtjj\n
    eightthree8fiveqjgsdzgnnineeight\n
    7chmvlhnpfive\n
'''

yacine = "./src/Yacine_input.txt"
paul = "./src/Paul_input.txt"

def test_calculate_sum():
    expected_result = 55607
    result = calculate_sum(yacine)
    assert result == expected_result