from find import calibrate_superior

yacine = "./src/Yacine_input.txt"
paul = "./src/Paul_input.txt"

def test_calculate_sum1():
    assert calibrate_superior('./src/__tests__/data_1.txt') == 29

def test_calculate_example2():
    assert calibrate_superior('./src/__tests__/data_2.txt') == 83
    
def test_calculate_example3():
    assert calibrate_superior('./src/__tests__/data_3.txt') == 13
    
def test_calculate_example4():
    assert calibrate_superior('./src/__tests__/data_4.txt') == 24
    
def test_calculate_example5():
    assert calibrate_superior('./src/__tests__/data_5.txt') == 42
    
def test_calculate_example6():
    assert calibrate_superior('./src/__tests__/data_6.txt') == 14
    
def test_calculate_example7():
    assert calibrate_superior('./src/__tests__/data_7.txt') == 76

def test_calculate_example_full():
    assert calibrate_superior('./src/__tests__/example_full.txt') == 281