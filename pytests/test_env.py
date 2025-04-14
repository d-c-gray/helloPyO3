import pyo3_example
import inspect

def test_sum_as_string():
    val = pyo3_example.sum_as_string(5, 20)
    assert val == '25'

if __name__ == '__main__':
    print(inspect.getsourcefile(pyo3_example))
    print(pyo3_example.sum_as_string.__doc__)