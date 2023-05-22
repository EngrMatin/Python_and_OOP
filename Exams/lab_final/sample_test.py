import halfadder

def test_half_adder():
    
    output = halfadder.half_adder_output(1, 1)
    assert output == [0, 1]
    
test_half_adder()


# Main file name: sample.py
# Test file name: sample_test.py
# Command for test: pytest

# pytest expects the test file name to be in the format: ‘*_test.py’ or ‘test_*.py’
# In order to run the test functions, remain in the same directory, and run the `pytest`, `py.test`, `py.test test_func.py` or `pytest test_func.py`.
# Use `py.test -v` to see the detailed output of each test case.
# 