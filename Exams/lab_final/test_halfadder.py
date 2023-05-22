import halfadder

def test_half_adder():
    
    output = halfadder.half_adder_output(1, 1)
    assert output == [0, 1]
    
test_half_adder()



# Main file name: halfadder.py
# Test file name: test_halfadder.py
# Command for test: pytest