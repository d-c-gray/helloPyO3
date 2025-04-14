import numpy as np
import pyo3_example
import inspect

def test_numpy():
    a = np.array([1,2,3])
    print(a)
    assert a[0] == 1

def test_sum_as_string():
    val = pyo3_example.sum_as_string(5, 20)
    assert val == '25'

if __name__ == '__main__':
    print(inspect.getsourcefile(pyo3_example))