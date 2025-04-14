import hello_pyo3 as mymod
import inspect
from importlib.metadata import version
def test_sum_as_string():
    val = mymod.sum_as_string(5, 20)
    assert val == '25'

if __name__ == '__main__':
    print(inspect.getsourcefile(mymod))
    print(mymod.sum_as_string.__doc__)
    print(version('hello-pyo3'))