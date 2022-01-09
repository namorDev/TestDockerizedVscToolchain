# pytest how to:
# 0. install pytest: pip3 install pytest
# 1. the file must be named with test_xxx.py
# 2. run the test with 'pytest' in the terminal

def func(x):
    return x+1

def test_answer():
    assert func(3) == 4