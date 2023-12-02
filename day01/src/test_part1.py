from trebuchet import calibrate

yacine = "./src/Yacine_input.txt"
paul = "./src/Paul_input.txt"

def test_calibrate():
    expected_result = 55607
    result = calibrate(yacine)
    assert result == expected_result