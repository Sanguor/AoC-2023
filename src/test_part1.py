from calibrate import calculate_sum

yacine = "./src/Yacine_input.txt"
paul = "./src/Paul_input.txt"

def test_calculate_sum():
    expected_result = 55607
    result = calculate_sum(yacine)
    assert result == expected_result